import book 
import requests
from bs4 import BeautifulSoup

"""on veut recuperer les liens a href d 'une categorie de livres:
        -   1 categorie peut etre sur une seul page:
            = il faut recuperer tous le lien sur cette page
        - elle peut etre sur plusieur pages :
            = il faudra recuperer les liens de chasue page
            
"""
url ="http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-2.html" 
reponse = requests.get(url)



soup = BeautifulSoup(reponse.content, "html.parser")
links = soup.find('div', class_='row')
links2 = links.find_all_next_("li")
print(links)





"""

url = book.url[:-10]
print(url)
list = []
def all_links ():           
    
    x = 0
    reponse = requests.get(url)
    while reponse.ok == True:
        x += 1
        url_var = url + "page-" + str(x) + '.html'
        reponse = requests.get(url_var)
        if reponse.ok:
            soup = BeautifulSoup(reponse.content, "html.parser")
            links = soup.find
            list.append(url_var)
    
        
   
    
    

    
links()       
  
print(list)"""
"""
for i in range(1,6):

    url_var = url + "page-" + str(i) + '.html'
    reponse = requests.get(url_var)
    if reponse.ok :
        print ("ok")
    else:
        print(error)"""