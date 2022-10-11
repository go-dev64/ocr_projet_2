"""Module category: 
    - list of categories
   - creating categories folders.
   - recovery of book url links(book, category, site)
"""


import utile
import os


def get_url_books_from_a_single_page(soupe, url):
    """get all books links of page.
    Args:
        Parsing of html page / url page
    Returns:
        list of links of books from a page.
    """
    url_domaine = utile.name_of_domain(url)
    list_of_books_from_single_page = []
    for i in soupe.find_all("h3"):
        href = i.find("a")["href"]
        book_name = href.split("/").pop(-2)
        list_of_books_from_single_page.append(url_domaine
                                              + book_name + "/index.html")
    return list_of_books_from_single_page


def get_books_links_from_all_pages(url, reponse):
    """loop through all pages for a category or site and
    return all available books.
    Args:
        url of category or site .
        response : response (requests).
    Returns:
        list of links of books from a category or site.
    """
    list_of_all_links_of_books = []
    x = 0
    while reponse.ok:
        x += 1
        url_var = url + "page-" + str(x) + ".html"
        reponse = utile.download_book_page(url_var)[1]
        list_of_all_links_of_books.extend(
            get_url_books_from_a_single_page(
                soupe=utile.download_book_page(url_var)[0], url=url
                )
        )

    return list_of_all_links_of_books


def select_case_of_application(url):
    """selects the application case according to the url entered by the user.
    Args:
        url of category or site or book.
    Returns:
        list of links of books (one book,category or site).
    """
    list_of_links = []
    url_modifie = url[:-10]
    reponse = utile.download_book_page(url_modifie + "page-1.html")[1]

    if reponse.ok:
        """case of application for a request for:
        a category of several pages or the site."""
        list_of_links.extend(
            get_books_links_from_all_pages(
                url=url_modifie,
                reponse=utile.download_book_page(url_modifie)[1]
            )
        )

    elif utile.download_book_page(url)[0].find("ol", class_="row"):
        """case of application for a request for:
        a single page category."""
        list_of_links.extend(get_url_books_from_a_single_page(
            soupe=utile.download_book_page(url)[0], url=url
            )
        )

    else:
        """case of application for a request for a book."""
        list_of_links.append(url)
    return list_of_links


def category():
    """get all categories of the site.

    Returns:
        list of categories
    """
    soup = utile.download_book_page(
        "http://books.toscrape.com/catalogue/category/books_1/index.html"
    )[0]
    categories = soup.find("ul", class_="nav").find("ul").find_all("a")
    all_category = []
    for category in categories:
        all_category.append(category.string.strip())
    return all_category


def creating_folders_by_categories():
    """Creating Data directory and folder categories
    in the current work directory
    """
    list_of_category = category()
    if not os.path.exists("Data"):
        os.makedirs("Data")

    for i in list_of_category:
        if not os.path.exists("Data/" + i):
            os.makedirs("Data/" + i)

    print("Les dossiers categories ont été créés dans le rep :Data")


# creating_folders_by_categories()
