from Project.lets_gnaw import Cheese

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
    mozzarella.gnaw_text()
    mozzarella.gnaw_hyperlinks()
    print("Cheese gnawing completed.")
