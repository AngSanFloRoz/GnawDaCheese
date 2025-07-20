import json
import pandas
import requests

from bs4 import BeautifulSoup
from Project.cheese import Cheese

class Wikipedia(Cheese):
    def __init__(self, url: str, name: str, creation_date: str):
        super().__init__(url, name, creation_date)
        self.__url = url
        self.__name = name
        self.__creation_date = creation_date

    def status_code_verification(self):
        return super().status_code_verification()

    def gnaw_titles(self):
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
            return list(tables), all_rows, all_boxes
        else:
            print(
                f"Failed to retrieve the page."
                f"Status code: {requests.get(self.__url).status_code}"
            )
            return None

    def gnaw_hyperlinks(self):
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
        print(f"Remi is saving data to {filename}...")
        data = {
            "url": self.__url,
            "name": self.__name,
            "creation_date": self.__creation_date,
        }
        if self.status_code_verification():

            self.gnaw_titles()
            data["titles"] = getattr(self, "titles", [])
            soup = BeautifulSoup(requests.get(self.__url).text, 'html.parser')

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


    def save_to_xlsx(self, xlsx_filename: str, json_filename: str = None):

        print(f"Remi is saving data to {xlsx_filename}...")

        if json_filename is None:
            json_filename = f"{self.__name.replace(' ', '_').lower()}_data.json"

        try:
            with open(json_filename, 'r', encoding='utf-8') as file:
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
                                df = pandas.DataFrame(table[1:], columns = table[0])
                            else:
                                df = pandas.DataFrame(table)
                            df.to_excel(
                                writer, sheet_name = f"Tabla_{i + 1}", index = False
                                )
            
                    except Exception as e:
                        print(f"An error occurred while saving tables to Excel: {e}")

                    try:
                        if titles:
                            df_titles = pandas.DataFrame({"Títulos": titles})
                            df_titles.to_excel(
                                writer, sheet_name = "Títulos", index = False
                            )

                    except Exception as e:
                        print(f"An error occurred while saving titles to Excel: {e}")

                    try:
                        if hyperlinks:
                            df_links = pandas.DataFrame({"Hipervínculos": hyperlinks})
                            df_links.to_excel(
                                writer, sheet_name = "Links", index = False
                            )

                    except Exception as e:
                        print(f"An error occurred while saving hyperlinks to Excel: {e}")

                    try:
                        if paragraphs:
                            df_paragraphs = pandas.DataFrame({"Párrafos": paragraphs})
                            df_paragraphs.to_excel(
                                writer, sheet_name = "Párrafos", index = False
                            )

                    except Exception as e:
                        print(f"An error occurred while saving paragraphs to Excel: {e}")
                
                print(f"Excel file saved successfully as '{xlsx_filename}'.")

        except FileNotFoundError:
            print(f"JSON file '{json_filename}' not found.")
        