import requests
from bs4 import BeautifulSoup


url ="http://books.toscrape.com/catalogue/we-love-you-charlie-freeman_954/index.html"

def download_book_page(url):
    """fonction de recuparation et de parsage de la page HTML
        Args:
            url : adresse URL d'un livre
        Returns:
            : contenu de la page html en question
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup