from Project.lets_gnaw import Cheese

if __name__ == "__main__":
    cheddar = Cheese(
        "https://es.wikipedia.org/wiki/Tabla_(informaci%C3%B3n)",
        "Tabla",
        "Unknown"
    )
    print(cheddar)
    cheddar.save_to_json("Wikipedia_Tabla.json")
    cheddar.save_to_xlsx("Wikipedia_Tabla.xlsx", "Wikipedia_Tabla.json")
    print("Cheese gnawing completed.")

    mozzarella = Cheese(
        "https://es.wikipedia.org/wiki/COVID-19",
        "COVID-19",
        "2019"
    )
    print(mozzarella)

    print("Cheese gnawing completed.")

    example_cheese = Cheese(
        "https://onepiece.fandom.com/es/wiki/One_Piece_Wiki",
        "One Piece Wiki",
        "2000"
    )
    print(example_cheese)
    example_cheese.save_to_json("One_Piece_Wiki.json")
    example_cheese.save_to_xlsx("One_Piece_Wiki.xlsx", "One_Piece_Wiki.json")

    print("Cheese gnawing completed.")