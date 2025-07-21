import json
import pandas
import requests

from bs4 import BeautifulSoup
from Project.cheese import Cheese

class Wikipedia(Cheese):
    """
    Esta subclase hereda de Cheese y represente una página del sitio web
    Wikipedia. Tiene los atributos de Cheese, además de atributos propios:
    Títulos, tablas, hipervínculos y párrafos.
    """
    
    def __init__(self, url: str, name: str, creation_date: str):
        """
        Inicializa una instancia de Wikipedia.
        """
        super().__init__(url, creation_date)
        self.__url = url
        self.__name = name
        self.__creation_date = creation_date

    def status_code_verification(self):
        """
        Verifica que el código de estado tenga un valor de 200 (solicitud del
        cliente recibida, entendida y procesada con éxito).
        """
        return super().status_code_verification()

    def gnaw_titles(self):
        """
        Obtiene todos los títulos de la página, los almacena como un atributo
        de tipo list del objeto y los imprime en la consola.
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
        Obtiene todas las tablas de la página, con sus respectivas filas y
        celdas, y las almacena como un atributo de tipo list del objeto.
        Por último, imprime en la consola las tablas.
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
        Obtiene todos los hipervínculos de la página, los almacena como un atributo
        de tipo list del objeto y los imprime en la consola.
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
        Obtiene todos los párrafos de la página, los almacena como un atributo
        de tipo list del objeto y los imprime en la consola.
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
        Crea un diccionario (data), en el que guarda todos los atributos del
        objeto (obtenidos por medio de los anteriores métodos) de la siguiente
        manera: clave = <nombre del atributo>, valor = <contenido del atributo>.
        Posteriormente, crea un archivo JSON con el nombre específicado en el
        que guarda data de manera que sea legible (indentación de 4 espacios).
        """
        print(f"Remi is saving data to {filename}...")
        self.json_filename = filename
        
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

            with open(filename, 'w', encoding = 'utf-8') as file:
                json.dump(data, file, ensure_ascii = False, indent = 4)
        else:   
            print("Failed to retrieve the page. Data not saved.")


    def save_to_xlsx(self, xlsx_filename: str):
        """
        Accede al contenido del archivo JSON creado y convierte tablas,
        títulos, hipervínculos y párrafos  a un archivo XLSX donde se
        separan en distintas hojas.
        """
        print(f"Remi is saving data to {xlsx_filename}...")

        try:
            with open(self.json_filename, 'r', encoding='utf-8') as file:
                data = json.load(file)

                tables = data.get("tables", [])
                titles = data.get("titles", [])
                hyperlinks = data.get("hyperlinks", [])
                paragraphs = data.get("paragraphs", [])

                if not tables:
                    print("No tables found in the JSON file to export.")

                with pandas.ExcelWriter(
                    xlsx_filename, engine = "openpyxl"
                    ) as writer:
                    
                    try:
                        for i, table in enumerate(tables):
                            if len(table) > 1:
                                df = pandas.DataFrame(
                                    table[1:], columns = table[0]
                                )
                            else:
                                df = pandas.DataFrame(table)
                            df.to_excel(
                                writer, sheet_name = f"Tabla_{i + 1}", index = False
                                )
            
                    except Exception as e:
                        print(
                            f"An error occurred while saving tables to Excel: {e}"
                        )

                    try:
                        if titles:
                            df_titles = pandas.DataFrame(
                                {"Títulos": titles}
                            )
                            df_titles.to_excel(
                                writer, sheet_name = "Títulos", index = False
                            )

                    except Exception as e:
                        print(
                            f"An error occurred while saving titles to Excel: {e}"
                             )

                    try:
                        if hyperlinks:
                            df_links = pandas.DataFrame(
                                {"Hipervínculos": hyperlinks}
                            )
                            df_links.to_excel(
                                writer, sheet_name = "Links", index = False
                            )

                    except Exception as e:
                        print(
                            f"An error occurred while saving hyperlinks to Excel: {e}"
                        )

                    try:
                        if paragraphs:
                            df_paragraphs = pandas.DataFrame(
                                {"Párrafos": paragraphs}
                                                            )
                            df_paragraphs.to_excel(
                                writer, sheet_name = "Párrafos", index = False
                            )

                    except Exception as e:
                        print(
                            f"An error occurred while saving paragraphs to Excel: {e}"
                             )
                
                print(
                    f"Excel file saved successfully as '{xlsx_filename}'."
                     )

        except FileNotFoundError:
            print(f"JSON file '{self.json_filename}' not found.")
