# data extraction and transformation.


import requests
import category
import utile


def data_of_table_part(url):
    soup = utile.download_book_page(url)[0]
    """"getting the information of <th> from the table
    "table table-striped".
            Returns:
            : dictionary with information <th>:
            (UPC, price_including_tax, price_excluding_tax, number_available,)
    """

    key_of_obj = []
    value_of_obj = []
    for element in soup.find(
                "table", class_="table table-striped").find_all("th"):
        key_of_obj.append(element.string)
    for element in soup.find(
                "table", class_="table table-striped").find_all("td"):
        value_of_obj.append(element.string)
    result = {x: y for x, y in zip(key_of_obj, value_of_obj)}
    return result


def img(url):
    """transform relative url to absolute url"""

    image = str(
        utile.download_book_page(url)[0]
        .find("div", class_="item active")
        .find("img")["src"]
    )[6:]
    image_url_absolu = "http://books.toscrape.com/" + str(image)
    return image_url_absolu


def download_img(url_img, name):
    """download picture of book"""

    title_name = utile.replace_special_caractere(name)
    with open(title_name + ".jpg", "wb") as f:
        response = requests.get(url_img)
        f.write(response.content)
        print("Telechargement de l'image du livre: " + name)


def scrap_book(url):
    """creating of the book information dictionary"""

    result = data_of_table_part(url)
    soup = utile.download_book_page(url)[0]
    dict_data = {
        "product_page_url": url,
        "upc": result["UPC"],
        "title": soup.h1.string,
        "price_including_tax": result["Price (incl. tax)"].replace("Â", ""),
        "price_excluding_tax": result["Price (excl. tax)"].replace("Â", ""),
        "number_available": int(
            "".join([str(i) for i in result["Availability"] if i.isnumeric()])
        ),
        "product_description": soup.h2.find_next("p").text,
        "category": soup.find(
            "ul", class_="breadcrumb").find_all("a")[2].string,
        "review_rating": soup.find_all(
            "p", class_="star-rating")[0]["class"][1],
        "image_url": img(url),
    }

    return dict_data


def all_dictionnary(url):
    """creating of list of information dictionnary for all books

    Args:
        url (_type_): url

    Returns:
        _type_: list of books information dictionnary
    """
    all_books = category.select_case_of_application(url)
    list_of_books = []
    for book in all_books:
        list_of_books.append(scrap_book(book))
        print(len(list_of_books), ":livres traités")

    return list_of_books
