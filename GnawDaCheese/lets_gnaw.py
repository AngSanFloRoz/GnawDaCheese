import requests
from bs4 import BeautifulSoup


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
        if self.status_code_verification():
            soup = BeautifulSoup(requests.get(self.__url).text, 'html.parser')
            titles = soup.find_all('h2')
            print(f"Remi has just gnawed on {self.__name} cheese!")
            print("Titles found on the page:")
            for title in titles:
                print(title.get_text(strip=True))
        else:
            print(
                f"Failed to retrieve the page. "
                f"Status code: {requests.get(self.__url).status_code}"
            )

    def gnaw_tables(self):
        if self.status_code_verification():
            soup = BeautifulSoup(requests.get(self.__url).text, 'html.parser')
            tables = soup.find_all('table', {'class': 'wikitable'})
            print(f"Remi has just gnawed on {self.__name} cheese!")
            print("Tables found on the page:")
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    cols = row.find_all('td')
                    if cols:
                        print([col.get_text(strip=True) for col in cols])
        else:
            print(
                f"Failed to retrieve the page. "
                f"Status code: {requests.get(self.__url).status_code}"
            )


if __name__ == "__main__":
    cheddar = Cheese(
        "https://es.wikipedia.org/wiki/Anexo:Presidentes_de_los_Estados_Unidos",
        "Presidentes de los Estados Unidos",
        "Unknown"
    )
    print(cheddar)
    cheddar.gnaw_titles()
    cheddar.gnaw_tables()
    print("Cheese gnawing completed.")

    mozzarella = Cheese(
        "https://es.wikipedia.org/wiki/COVID-19",
        "COVID-19",
        "2019"
    )
    print(mozzarella)
    mozzarella.gnaw_titles()
    mozzarella.gnaw_tables()
    print("Cheese gnawing completed.")
