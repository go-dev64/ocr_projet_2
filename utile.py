import requests
from bs4 import BeautifulSoup





def download_book_page(url):
    """fonction de recuparation et de parsage de la page HTML
        Args:
            url : adresse URL d'un livre
        Returns:
            : contenu de la page html en question
     """
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.content, "html.parser")
    return soup , reponse


def replace_special_caractere(my_str):
    special_caractere = "}’{!@#$%^&*'()¨^\[]};,./<>?\|`~-=_+:‽"
    for element in special_caractere:
        my_str = my_str.replace(element, "_").replace("é","e").replace("è","e").replace('"'," ")
    return my_str


