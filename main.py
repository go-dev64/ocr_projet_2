from export import get_category_information

url = "http://books.toscrape.com/catalogue/category/books_1/index.html"


def main():
    reponse = input("Veuillez choisr le mode d'exécution : \n"
                    "1 - Export d'un livre\n"
                    "2 - Choix d'une catégorie\n"
                    "3 - Tout")
    if reponse == "1":
        book_url = input("Merci de saisir l'url du livre")
        get_page_information(book_url)
    elif reponse == "2":
        categories = get_categories()
        choosen_category = input("Choisissez une catégorie :\n" + categories)
        get_category_information(choosen_category)
    elif reponse == "3":
        get_all_books_information()

    print("C'est fait, merci")


if __name__ == "__main__":
    main()
