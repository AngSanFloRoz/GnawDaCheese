import requests
from bs4 import BeautifulSoup
import json


class Cheese:
    def __init__(self, url: str, name: str, creation_date: str):
        self.__url = url
        self.__name = name
        self.__creation_date = creation_date

    def get_url(self):
        return self.__url

    def set_url(self, url: str):
        self.__url = url

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_creation_date(self):
        return self.__creation_date

    def set_creation_date(self, creation_date: str):
        self.__creation_date = creation_date

    def __str__(self):
        return (
            f"Cheese: Name = {self.__name}, "
            f"URL = {self.__url}, "
            f"Creation Date = {self.__creation_date})"
        )
    
    def status_code_verification(self):
        response = requests.get(self.__url)
        if response.status_code == 200:
            return True
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return False

    def gnaw_titles(self):
        self.titles = []
        if self.status_code_verification():
            soup = BeautifulSoup(requests.get(self.__url).text, 'html.parser')
            self.titles = [title.get_text(strip=True) for title in soup.find_all('h2')]
            print(f"Remi has just gnawed on {self.__name} cheese!")
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
                        print(box.get_text(strip=True))
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
            links = soup.find_all('a', href=True)
            print(f"Remi has just gnawed on {self.__name} cheese!")
            print("Hyperlinks found on the page:")
            for link in links:
                href = link['href']
                self.hyperlinks.append(href)
                print(href)
        else:
            print(
                f"Failed to retrieve the page. "
                f"Status code: {requests.get(self.__url).status_code}"
            )

    def gnaw_text(self):
        if self.status_code_verification():
            soup = BeautifulSoup(requests.get(self.__url).text, 'html.parser')
            paragraphs = soup.find_all('p')
            print(f"Remi has just gnawed on {self.__name} cheese!")
            print("Text found on the page:")
            for para in paragraphs:
                print(para.get_text(strip=True))
        else:
            print(
                f"Failed to retrieve the page. "
                f"Status code: {requests.get(self.__url).status_code}"
            )

    def save_to_file(self, filename: str):
        data = {
            "url": self.__url,
            "name": self.__name,
            "creation_date": self.__creation_date,
        }
        if self.status_code_verification():
            # Use existing methods to extract data
            # Titles
            self.gnaw_titles()
            data["titles"] = getattr(self, "titles", [])
            soup = BeautifulSoup(requests.get(self.__url).text, 'html.parser')

            # Tables
            tables_data = []
            tables_result = self.gnaw_tables()
            if tables_result:
                _, all_rows, all_boxes = tables_result
                for table_boxes in all_boxes:
                    table_data = []
                    for row_boxes in table_boxes:
                        row_data = [box.get_text(strip=True) for box in row_boxes]
                        table_data.append(row_data)
                    tables_data.append(table_data)
            data["tables"] = tables_data

            # Hyperlinks
            self.gnaw_hyperlinks()
            data["hyperlinks"] = getattr(self, "hyperlinks", [])

            # Paragraphs
            paragraphs = [para.get_text(strip=True) for para in soup.find_all('p')]
            data["paragraphs"] = paragraphs

            # Save to JSON file
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        else:
            print("Failed to retrieve the page. Data not saved.")

if __name__ == "__main__":
    cheddar = Cheese(
        "https://es.wikipedia.org/wiki/Anexo:Presidentes_de_los_Estados_Unidos",
        "Presidentes de los Estados Unidos",
        "Unknown"
    )
    print(cheddar)
    cheddar.gnaw_titles()
    cheddar.gnaw_tables()
    print("\nCheese gnawing completed.")

    mozzarella = Cheese(
        "https://es.wikipedia.org/wiki/COVID-19",
        "COVID-19",
        "2019"
    )
    print(mozzarella)
    mozzarella.gnaw_titles()
    mozzarella.gnaw_tables()
    print("\nCheese gnawing completed.")

    cheddar.save_to_file("cheddar_data.json")
    mozzarella.save_to_file("mozzarella_data.json")

    print("Data saved to JSON files.")