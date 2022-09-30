import csv
import book as b

def export_csv():
    """ creer un fichiers csv depuis le dict_ data du module book.py
    """
    book = b.scrap_book()
    """Creation de l en-tete du fichiers csv"""
    
    en_tete = ["product_page_url", "universal_product_code",
            "title", "price_including_tax", "price_excluding_tax",
            "number_available", "product_description", "category",
            "review_rating", "image_url"]
    
    """Ligne type du fichier csv"""
    
    ligne_book = [book["product_page_url"], book["upc"], book["title"], book["price_including_tax"], book["price_excluding_tax"],
            book["number_available"], book["product_description"], book["category"], book["review_rating"], book["image_url"]]

    """ecriture du csv"""
    with open ("{book['title']}.csv", "w") as f:
        
        writer = csv.writer(f, delimiter= ',')
        writer.writerow(en_tete)
        writer.writerow(ligne_book)
        
        print("fichier csv creer")