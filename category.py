import requests
from bs4 import BeautifulSoup
import utile

def get_links_of_page(soupe):
    """recupere tous les liens des livres d'une page.

    Args:
        Parsage d'une page html.

    Returns:
        une liste des liens des livres de la page html links[].
    """
    links = []   
    for i in soupe.find_all('h3'):
        links.append("http://books.toscrape.com/catalogue"+ i.find("a")['href'][8:])
    return links                     
                               
               

def links_all_pages(url, reponse):
    
    """boucle sur toutes les pages disponibles pour la categorie ou sur le site et retourne un liste des liens des livres.
    Args:
        url des la categorie ou du site .
        reponse : reponse de la requette http (requests)
    Returns:
        une liste contenant tous les liens des livres. books_url
    """
    
    links_of_books_pages = []      
    x = 0
    while reponse.ok:
        x += 1
        url_var = url + "page-" + str(x) + '.html'
        reponse = utile.download_book_page(url_var)[1]  
        links_of_books_pages.extend(get_links_of_page(utile.download_book_page(url_var)[0]))    
        
                            
    return links_of_books_pages



   
def get_all_links_of_all_pages (url): 
    """Fonction des recuperations de tous les liens.
    Args:
        url de la categorie ou du site
    Returns:
        liste des url des livres.
    """
    all_books_url = []      
    url_modifie = url[:-10]
    reponse = utile.download_book_page(url_modifie + "page-1.html")[1]
    
    if reponse.ok:
        """verifie si plusieurs pages sont disponible, et les parcours pour retourner les liens des livres de chaque pages"""
        all_books_url.extend(links_all_pages(url= url_modifie, reponse= utile.download_book_page(url_modifie)[1]))
    
    elif utile.download_book_page(url)[0].find("ol", class_="row"):
        """verifie si il y a des liens de livres sur la page et retournent tous les liens de cette page. """
        all_books_url.extend(get_links_of_page(soupe= utile.download_book_page(url)[0]))
        
    else:   
        """retournent le lien d'un livre""" 
        all_books_url.append(url)
        
    return all_books_url   
        
        