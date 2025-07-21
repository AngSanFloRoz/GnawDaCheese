from bs4 import BeautifulSoup
import requests

class Cheese:
    """
    This class represents the page to be scraped. Its attributes are a URL, a
    creation date and a name.
    """
    
    def __init__(self, url: str, creation_date: str):
        """
        Initializes an instance of Cheese.
        """
        self.__url = url
        self.__creation_date = creation_date
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        self.__name = soup.find('span', class_='mw-page-title-main').get_text()

    def get_url(self):
        """
        Gets the URL.
        """
        return self.__url
        
    def set_url(self, url: str):
        """
        Sets the URL.
        """
        self.__url = url
        
    def get_name(self):
        """
        Gets the name of the page.
        """
        return self.__name
        
    def set_name(self, name: str):
        """
        Sets the name of the page.
        """
        self.__name = name

    def get_creation_date(self):
        """
        Gets the creation date.
        """
        return self.__creation_date
        
    def set_creation_date(self, creation_date: str):
        """
        Sets the creation date.
        """
        self.__creation_date = creation_date

    def __str__(self):
        """
        Defines how a Cheese object (web page) behaves when using
        print(<object>) to print to the console.
        """
        return (
            f"Cheese: Name = {self.__name}, "
            f"URL = {self.__url}, "
            f"Creation Date = {self.__creation_date})"
        )
    
    def status_code_verification(self):
        """
        Verify that the status code has a value of 200 (client request received,
        understood, and processed successfully).
        """
        response = requests.get(self.__url)
        if response.status_code == 200:
            return True
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return False
