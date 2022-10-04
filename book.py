import requests
from bs4 import BeautifulSoup
import category


url ="http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"

def download_book_page(url):
    """fonction de recuparation et de parsage de la page HTML
        Args:
            url : adresse URL d'un livre
        Returns:
            : contenu de la page html en question
    """
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.content, "html.parser")
    return soup


def scrap_book(url):
    soup = download_book_page(url)
       
    def th():
        
        """"Fonct de recuperation des informations les <th> de la "table table-striped"  de la page html
                Returns:
                : 1 dictionnaire contenant les information du livres (UPC, prix avec taxes, prix sans taxe, nombre disponible)
        """
        soup = download_book_page(url)
        key_of_obj = []
        value_of_obj = []
        for element in soup.find('table', class_ ='table table-striped').find_all('th'):
          key_of_obj.append(element.string)
        for element in soup.find('table', class_ ='table table-striped').find_all('td'):
          value_of_obj.append(element.string)
        result = {x: y for x, y in zip(key_of_obj, value_of_obj)}
        return result
    
       
    def img ():
        
        '''recuperation de l'url relative de la couverture du livre et convertion en url absolue''' 
        image = list(soup.find("div", class_= "item active").find('img')['src'])
        del image[0:6]
        image_url_absolu = "http://books.toscrape.com/"+"".join(image)  
        return image_url_absolu 
    
    result = th() 
    
    """creation du dictionnaire de données du livre dict_data"""
    
    dict_data = {"product_page_url": url,
                "upc" : result["UPC"],
                "title": soup.h1.string,
                "price_including_tax" : result["Price (incl. tax)"].replace("Â",""),
                "price_excluding_tax" : result["Price (excl. tax)"].replace("Â",""),
                "number_available" : int(''.join([str(i) for i in result["Availability"] if i.isnumeric()])),
                "product_description": soup.h2.find_next("p").text,
                "category": soup.find("ul", class_="breadcrumb").find_all("a")[2].string,
                "review_rating" : soup.find_all("p", class_="star-rating")[0]["class"][1],
                "image_url": img()}
    return dict_data




def all_books (url):
    list_of_books = []
    for book in category.get_all_links_of_all_pages(url):
        list_of_books.append(scrap_book(book))
        
    return list_of_books


