import requests
from bs4 import BeautifulSoup
import category
import utile


url ="http://books.toscrape.com/catalogue/category/books_1/index.html"
   
def data_of_table_part(url):  
    soup = utile.download_book_page(url)[0] 
    """"Fonct de recuperation des informations les <th> de la "table table-striped"  de la page html
            Returns:
            : 1 dictionnaire contenant les information du livres (UPC, prix avec taxes, prix sans taxe, nombre disponible)
    """
    
    key_of_obj = []
    value_of_obj = []
    for element in soup.find('table', class_ ='table table-striped').find_all('th'):
        key_of_obj.append(element.string)
    for element in soup.find('table', class_ ='table table-striped').find_all('td'):
        value_of_obj.append(element.string)
    result = {x: y for x, y in zip(key_of_obj, value_of_obj)}
    return result


def img (url):   
    '''recuperation de l'url relative de la couverture du livre et convertion en absolue'''
    
    image = list(utile.download_book_page(url)[0].find("div", class_= "item active").find('img')['src'])
    del image[0:6]
    image_url_absolu = "http://books.toscrape.com/"+"".join(image)  
    return image_url_absolu 


def download_img(url_img, name): 
    """telechargement de l image du livre"""    
    
    title_name = utile.replace_special_caractere(name)
    with open (title_name + ".jpg", "wb") as f:
        response = requests.get(url_img)
        f.write(response.content) 
        print("download " + name + ".jpg successful")
     

def scrap_book(url):  
    """creation du dictionnaire de données du livre dict_data"""    
    
    result = data_of_table_part(url)
    soup = utile.download_book_page(url)[0]
    dict_data = {"product_page_url": url,
                "upc" : result["UPC"],
                "title" : soup.h1.string,
                "price_including_tax" : result["Price (incl. tax)"].replace("Â",""),
                "price_excluding_tax" : result["Price (excl. tax)"].replace("Â",""),
                "number_available" : int(''.join([str(i) for i in result["Availability"] if i.isnumeric()])),
                "product_description": soup.h2.find_next("p").text,  # replace("‽","_").replace(" ","_")
                "category": soup.find("ul", class_="breadcrumb").find_all("a")[2].string,
                "review_rating" : soup.find_all("p", class_="star-rating")[0]["class"][1],
                "image_url": img(url)
                }
    print("dict_data of" , dict_data["title"])
    return dict_data 
    
    

def all_dictionnary(url):
    all_books = category.get_all_links_of_all_pages(url)
    print(all_books)
    print(len(all_books))
    list_of_books = []
    for book in all_books:
        list_of_books.append(scrap_book(book))
        print(len(list_of_books),":livres traités")   
    print(len(list_of_books),":livres traités")    
    return list_of_books


