from bs4 import BeautifulSoup
import requests

class Cheese:
    """
    Esta es la página a roer (scrapear).
    """
    
    def __init__(self, url: str, creation_date: str):
        """
        Inicializa una instancia de Cheese.
        """
        self.__url = url
        self.__creation_date = creation_date
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        self.__name = soup.find('span', class_='mw-page-title-main').get_text()

    def get_url(self):
        """
        Obtener la URL.
        """
        return self.__url
        
    def set_url(self, url: str):
        """
        Establecer la URL.
        """
        self.__url = url
        
    def get_name(self):
        """
        Obtener el nombre de la página.
        """
        return self.__name
        
    def set_name(self, name: str):
        """
        Establecer el nombre de la página.
        """
        self.__name = name

    def get_creation_date(self):
        """
        Obtener la fecha de creación.
        """
        return self.__creation_date
        
    def set_creation_date(self, creation_date: str):
        """
        Establecer la fecha de creación.
        """
        self.__creation_date = creation_date

    def __str__(self):
        """
        Define cómo se comporta un objeto Cheese (página) al utilizar
        print(<objeto>) para imprimir en la consola.
        """
        return (
            f"Cheese: Name = {self.__name}, "
            f"URL = {self.__url}, "
            f"Creation Date = {self.__creation_date})"
        )
    
    def status_code_verification(self):
        """
        Verifica que el código de estado tenga un valor de 200 (solicitud del
        cliente recibida, entendida y procesada con éxito).
        """
        response = requests.get(self.__url)
        if response.status_code == 200:
            return True
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return False
