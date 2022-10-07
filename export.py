import csv
import book as b
import os
import category as cat
       

def create_csv_file(list):
        list_of_books = list    #b.all_books (b.url)
        """ creer un fichiers csv avec les data de chaque livre.
                data_ book = b.all_books (b.url)
                un fichiers csv par category
        """
        en_tete = ["product_page_url", 
                   "universal_product_code",
                   "title",
                   "price_including_tax",
                   "price_excluding_tax",
                   "number_available",
                   "product_description",
                   "category",
                   "review_rating",
                   "image_url"
                   ]

        with open (list_of_books[0]["category"] + ".csv", "w", encoding="UTF-16LE") as f:
        
                writer = csv.writer(f, delimiter= ',')
                writer.writerow(en_tete)
        
                for book in list_of_books:
                        ligne_book = [book["product_page_url"],
                                      book["upc"],
                                      book["title"],
                                      book["price_including_tax"],
                                      book["price_excluding_tax"],
                                      book["number_available"],
                                      book["product_description"],
                                      book["category"],
                                      book["review_rating"],
                                      book["image_url"]
                                      ]    
                        print(ligne_book)
                        writer.writerow(ligne_book)
                        b.download_img(url_img=book["image_url"], name=book["title"])
        
        print("Le fichier :" + list_of_books[0]["category"] + ".csv est créé")
        
      

def tri():
        
        list_category = cat.category()
        list_books = b.all_dictionnary (b.url)
        
        print("tot",list_category)
        print("lolo:",list_books, len(list_books))
        
        for element in list_category:
                books_of_element = []
                print(element)
                
                for book in list_books:
                        if book['category'] == element:
                                books_of_element.append(book)    
                                
                if len(books_of_element) > 0:
                        os.chdir("Data/" + element)
                        create_csv_file(books_of_element)
                        os.chdir("../../")
            
                
   
                
