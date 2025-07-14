#* website
from bs4 import BeautifulSoup
import requests


class Cheeses:
    def __init__(self, Url):
        self.Url = Url 
        self.request = requests.get(Url)
        self.state = self.request.status_code
        self.html = self.request.text
        if self.state == 200:
            self.soup = BeautifulSoup(self.html, 'html.parser')
        else: 
            self.soup = None

    def information(self):
        if self.soup:
            for tag in self.soup.find_all(["h1", "h2", "p"]):
                print(tag.text)
        else:
            print("No se puede pa, pagina de mrd")
        return "dime si quieres algo mas"

url = "https://es.wikipedia.org/wiki/Adolf_Hitler"
cheese1 = Cheese(url)
cheese1.information()   

#! la de abajo es la de antes y la arriba es la nueva

class Cheese:
    def __init__(self, url: str, name: str):
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

    def spoiled(self)
        return self.__url.state() != good

    def extratinformation(self):
        raise NotImplementError

    def __str__(self):
        return f"Cheese: Name = {self.__name}, URL = {self.__url}, Creation Date = {self.__creation_date})"



#cheese's children

#static

class wiki(Cheese):
    def __init__def __init__(self, url: str, name: str)
        super().__init__(url, name)

    def contents(self):
        pass #todo ver como extraer subtitulos (con beatiful soups)

    def extractinformation(self):
        pass # contents extract the information

    def export_information(self):
        pass #contest extrac information

class OnlineStore(Cheese):
    def __init__def __init__(self, name: str, url: str)
        super().__init__(url, name)

    def contents(self):
        pass #despues ver (con beatiful soups)

    def extractinformation(self):
        pass # despues ver

    def export_information(self):
        pass #despues ver
    


