from Project.Cheeses.wikipedia_cheese import Wikipedia
from Project.Cheeses.Mercadolibre_cheese import Onlinecommerce

if __name__ == "__main__":
    cheddar = Wikipedia(
        "https://es.wikipedia.org/wiki/Tabla_(informaci%C3%B3n)",
        "Tabla",
        "Unknown"
    )
    print(cheddar)
    cheddar.save_to_json("Wikipedia_Tabla.json")
    cheddar.save_to_xlsx("Wikipedia_Tabla.xlsx")
    print("Cheese gnawing completed.")

    mozzarella = Wikipedia(
        "https://es.wikipedia.org/wiki/COVID-19",
        "COVID-19",
        "2019"
    )
    print(mozzarella)
    mozzarella.save_to_json("COVID-19.json")
    mozzarella.save_to_xlsx("COVID-19.xlsx")
    print("Cheese gnawing completed.")

    webd1 = Onlinecommerce("https://www.mercadolibre.com.co/")
    webd1.scrapped("sans", "e_e_e")

