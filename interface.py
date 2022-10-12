import utile


def get_list_categories():
    soup = utile.download_book_page(
        "http://books.toscrape.com/catalogue/category/books_1/index.html"
    )[0]
    categories = soup.find("ul", class_="nav").find("ul").find_all("a")
    list_of_url_categories = []
    list_of_name_of_categories = []
    for cat in categories:
        list_of_url_categories.append(cat["href"][2:])
        list_of_name_of_categories.append(cat.string.strip())
    return list_of_url_categories, list_of_name_of_categories


def category_choice(list_names):

    list_names = list_names
    for i in list_names:
        print(i, "=", list_names.index(i), end=" ; ")

    choice_of_category = int(
        input("\nEntrer le numero de la catégorie choisie :"))
    print("Vous avez choisi la categorie :" + list_names[choice_of_category])
    return choice_of_category


def url_category(number_of_category, list_url):
    list_url = list_url
    url_domain = "http://books.toscrape.com/catalogue/category"
    print(list_url[number_of_category])
    url_of_the_chosen_category = url_domain + list_url[number_of_category]
    print(url_of_the_chosen_category)

    return url_of_the_chosen_category


def user_choice():
    list_of_url_categories = get_list_categories()[0]
    list_of_name_of_categories = get_list_categories()[1]
    choice = int(
        input(
            "    Pour exporter les données d'un livre, Taper 1\n\
    Pour exporter les données d'une catégorie de livre, Taper 2\n\
    Pour exporter les données du site, Taper 3\n\
    Indiquer votre choix: "
        )
    )

    if choice == 1:
        url_livre = input("Veuillez renseigner l'url du livre :")
        print("Export du livre en cours...")
        return url_livre

    elif choice == 2:
        choice_of_category = category_choice(
            list_names=list_of_name_of_categories
        )
        url_of_category = url_category(
            number_of_category=choice_of_category,
            list_url=list_of_url_categories
        )

        print("Export de la categorie: "
              + list_of_name_of_categories[choice_of_category] + " en cours...")
        return url_of_category

    else:
        url_site = "http://books.toscrape.com/catalogue/category/books_1/index.html"
        print("Export du site en cours...")
        return url_site
