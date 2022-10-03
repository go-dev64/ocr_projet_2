from http.client import responses
import book 
import requests
from bs4 import BeautifulSoup

"""on veut recuperer les liens a href d 'une categorie de livres:
        -   1 categorie peut etre sur une seul page:
            = il faut recuperer tous le lien sur cette page
        - elle peut etre sur plusieur pages :
            = il faudra recuperer les liens de chasue page
            
"""
url ="http://books.toscrape.com/catalogue/category/books/fiction_10/index.html" 




def soup(url):
    """  realise une soup de la page html."""
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.content, "html.parser")
    return soup , reponse


def get_links_of_page(soupe):
    """recupere tous les liens des livres d'une page.

    Args:
        Parsage d'une page html.

    Returns:
        une liste des liens des livres de la page html.
    """
    links = []   
    for i in soupe.find_all('h3'):
        links.append("http://books.toscrape.com/catalogue"+ i.find("a")['href'][8:])
    return links                     
                               
               

   
def get_all_links (url): 
    books_url = []      
    url = url[:-10]
    x = 0
    reponse = requests.get(url)
    while reponse.ok:
        x += 1
        url_var = url + "page-" + str(x) + '.html'
        reponse = soup(url_var)[1]  
        soup_url_var = soup(url_var)[0]
        print(reponse)
        if soup(url_var)[1].ok:
           books_url.extend(get_links_of_page(soup_url_var))    
            
    return books_url
      
        


print(get_all_links(url))