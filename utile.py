# utile

import requests
from bs4 import BeautifulSoup


def download_book_page(url):
    """parsing of html page
        Args:
            url : url of book
        Returns:
            : content of page 
     """
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.content, "html.parser")
    return soup, reponse


def replace_special_caractere(my_str):
    """replace special caractere
    Args:
        my_str (_type_): _description_
    Returns:
        _type_: _description_(without cspecial caractere)
    """
    special_caractere = "}’{!@#$%^&*'()¨^\[]};,./<>?|`~-=_+:‽"
    for element in special_caractere:
        my_str = my_str.replace(element, "_").replace(
            "é", "e").replace("è", "e").replace('"', " ")
    return my_str


def name_of_domain(url):
    """ return the domain name
    Args:
        url (_type_): _description_
    Return:
        Url of domaine("http://books.toscrape.com/catalogue/")
    """
    
    url_domain = url[:36]
    
    return url_domain

