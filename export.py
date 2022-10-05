import csv
import book as b

def export_csv():
        list_of_books = b.all_books (b.url)
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

        with open (list_of_books[0]["category"] + ".csv", "w") as f:
        
                writer = csv.writer(f, delimiter= ',')
                writer.writerow(en_tete)
        
                for book in list_of_books:
                        ligne_book = [book["product_page_url"],
                                      book["upc"], book["title"],
                                      book["price_including_tax"],
                                      book["price_excluding_tax"],
                                      book["number_available"],
                                      book["product_description"],
                                      book["category"],
                                      book["review_rating"],
                                      book["image_url"]
                                      ]    
                        writer.writerow(ligne_book)
        
        print("Le fichier :" + b.all_books(b.url)[0]["category"] + ".csv est créé")
        
      

      



