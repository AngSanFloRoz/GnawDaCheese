import requests

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