import json
import os
import pandas
import requests

from bs4 import BeautifulSoup
from Project.cheese import Cheese

class Wikipedia(Cheese):
    """
    This subclass inherits from Cheese and represents a page from the Wikipedia
    website. It has the attributes of Cheese, as well as its own attributes:
    Titles, tables, hyperlinks, and paragraphs.
    """
    
    def __init__(self, url: str, name: str, creation_date: str):
        """
        Initializes a Wikipedia instance.
        """
        super().__init__(url, name, creation_date)
        self.__url = url
        self.__name = name
        self.__creation_date = creation_date

    def status_code_verification(self):
        """
        Verify that the status code has a value of 200 (client request received,
        understood, and processed successfully).
        """
        return super().status_code_verification()

    def gnaw_titles(self):
        """
        Gets all the titles on the page, stores them as a list attribute of the
        object, and prints them to the console.
        """
        self.titles = []
        if self.status_code_verification():
            soup = BeautifulSoup(
                requests.get(self.get_url()).text, 'html.parser'
                )
            self.titles = [
                title.get_text(strip = True) for title in soup.find_all('h2')
                ]
            print(f"Remi has just gnawed on {self.get_name()} cheese!")
            print("Titles found on the page:")
            for title in self.titles:
                print(title)
        else:
            print(
                f"Failed to retrieve the page. "
                f"Status code: {requests.get(self.__url).status_code}"
            )

    def gnaw_tables(self):
        """
        Obtains all the tables on the page, along with their respective rows and
        cells, and stores them as a list attribute of the object. Finally, it
        prints the tables to the console.
        """
        self.tables = []
        if self.status_code_verification():
            soup = BeautifulSoup(requests.get(self.__url).text, 'html.parser')
            tables = soup.find_all('table', {'class': 'wikitable'})
            self.tables = tables
            all_rows = []
            all_boxes = []
            for table in tables:
                rows = table.find_all('tr')
                all_rows.append(rows)
                table_boxes = []
                for row in rows:
                    boxes = row.find_all(['td', 'th'])
                    table_boxes.append(boxes)
                all_boxes.append(table_boxes)
            print(f"Remi has just gnawed on {self.__name} cheese!")
            print(f"Tables found on the page: {len(tables)}")
            print("Rows and boxes in each table:")
            for i, table in enumerate(tables):
                print(f"\nTable {i + 1}:")
                for j, row in enumerate(all_rows[i]):
                    print(f"Row {j + 1}:")
                    for box in all_boxes[i][j]:
                        print(box.get_text(strip = True))
            return self.tables, all_rows, all_boxes
        else:
            print(
                f"Failed to retrieve the page."
                f"Status code: {requests.get(self.__url).status_code}"
            )
            return None

    def gnaw_hyperlinks(self):
        """
        Gets all hyperlinks on the page, stores them as a list attribute of the
        object, and prints them to the console.
        """
        self.hyperlinks = []
        if self.status_code_verification():
            soup = BeautifulSoup(requests.get(self.__url).text, 'html.parser')
            self.hyperlinks = [
                link['href'] for link in soup.find_all('a', href = True)
                if link.get('href') and link['href'].startswith('http')
            ]
            #links = soup.find_all('a', href = True)
            #print(f"Remi has just gnawed on {self.__name} cheese!")
            #print("Hyperlinks found on the page:")
            for hyperlink in self.hyperlinks:
                print(hyperlink)
        else:
            print(
                f"Failed to retrieve the page. "
                f"Status code: {requests.get(self.__url).status_code}"
            )

    def gnaw_text(self):
        """
        Gets all the paragraphs on the page, stores them as a list attribute of
        the object, and prints them to the console.
        """
        self.paragraphs = []
        if self.status_code_verification():
            soup = BeautifulSoup(requests.get(self.__url).text, 'html.parser')
            self.paragraphs = [
                paragraph.get_text(strip = True)
                for paragraph in soup.find_all('p')
                ]
            print(f"Remi has just gnawed on {self.__name} cheese!")
            print("Text found on the page:")
            for paragraph in self.paragraphs:
                print(paragraph)
        else:
            print(
                f"Failed to retrieve the page. "
                f"Status code: {requests.get(self.__url).status_code}"
            )

    def save_to_json(self, filename: str):
        """
        It creates a dictionary (data) in which it stores all of the object's
        attributes (obtained using the previous methods) as follows: key =
        <attribute name>, value = <attribute content>. It then creates a JSON
        file with the specified name in which it stores the data in a 
        human-readable manner (indented by 4 spaces).
        """
        print(f"Remi is saving data to {filename}...")
        self.json_filename = filename

        base_dir = os.path.dirname(__file__)

        json_dir = os.path.join(base_dir, "..", "jsonfilesstatic")
        os.makedirs(json_dir, exist_ok = True)

        json_path = os.path.join(json_dir, f"{filename}.json")
        
        data = {
            "url": self.__url,
            "name": self.__name,
            "creation_date": self.__creation_date,
        }
        if self.status_code_verification():

            self.gnaw_titles()
            data["titles"] = [title for title in self.titles]

            tables_data = []
            tables_result = self.gnaw_tables()
            if tables_result:
                all_boxes = tables_result[2]
                for boxes in all_boxes:
                    table_data = []
                    for row_boxes in boxes:
                        row_data = [
                            box.get_text(strip = True) for box in row_boxes
                            ]
                        table_data.append(row_data)
                    tables_data.append(table_data)
            data["tables"] = tables_data

            self.gnaw_hyperlinks()
            data["hyperlinks"] = [link for link in self.hyperlinks]

            self.gnaw_text()
            data["paragraphs"] = [paragraph for paragraph in self.paragraphs]

            with open(json_path, 'w', encoding = 'utf-8') as file:
                json.dump(data, file, ensure_ascii = False, indent = 4)
        else:   
            print("Failed to retrieve the page. Data not saved.")


    def save_to_xlsx(self, xlsx_filename: str):
        """
        Access the contents of the created JSON file and convert tables,
        headings, hyperlinks, and paragraphs to an XLSX file, where they are
        separated into sheets.
        """
        print(f"Remi is saving data to {xlsx_filename}...")

        base_dir = os.path.dirname(__file__)
        json_path = os.path.join(base_dir, "..", "jsonfilesstatic", f"{self.json_filename}.json")

        try:
            with open(json_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            wb = Workbook()

            # Función para crear una hoja con formato
            def add_sheet_with_format(sheet_name, headers, rows):
                ws = wb.create_sheet(title=sheet_name)
                ws.append(headers)
                for cell in ws[1]:
                    cell.font = Font(bold=True)

                for row in rows:
                    ws.append(row)

                # Alinear, ajustar ancho y congelar fila
                for col in ws.columns:
                    max_length = max((len(str(cell.value)) for cell in col if cell.value), default=0)
                    col_letter = col[0].column_letter
                    for cell in col:
                        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
                    ws.column_dimensions[col_letter].width = max_length + 2
                ws.freeze_panes = "A2"

            # Agregar tablas
            for i, table in enumerate(data.get("tables", [])):
                if table:
                    headers = table[0] if len(table) > 1 else [f"Columna {j+1}" for j in range(len(table[0]))]
                    rows = table[1:] if len(table) > 1 else table
                    add_sheet_with_format(f"Tabla_{i+1}", headers, rows)

            # Agregar títulos
            if data.get("titles"):
                add_sheet_with_format("Títulos", ["Título"], [[t] for t in data["titles"]])

            # Agregar hipervínculos
            if data.get("hyperlinks"):
                add_sheet_with_format("Links", ["Hipervínculo"], [[l] for l in data["hyperlinks"]])

            # Agregar párrafos
            if data.get("paragraphs"):
                add_sheet_with_format("Párrafos", ["Párrafo"], [[p] for p in data["paragraphs"]])

            # Eliminar la hoja por defecto vacía
            if "Sheet" in wb.sheetnames:
                wb.remove(wb["Sheet"])

            excel_dir = os.path.join(base_dir, "..", "excelfilesstatic")
            os.makedirs(excel_dir, exist_ok=True)
            excel_path = os.path.join(excel_dir, f"{xlsx_filename}.xlsx")
            wb.save(excel_path)
            print(f"Archivo Excel guardado en: {excel_path}")

        except FileNotFoundError:
            print(f"JSON file '{self.json_filename}' not found.")
