"""list_pages =[]
            for i in range(1,6):
            
                url_var ='http://books.toscrape.com/catalogue/category/books/fiction_10/' + "page-" + str(i) + '.html'
                reponse = requests.get(url_var)
                if reponse.ok :
                    print ("ok")
                else:
                    print(error)
             
list = []
x = 0
reponse = requests.get(url)
while reponse.ok == True:
    x += 1
    url_var = url + "page-" + str(x) + '.html'
    reponse = requests.get(url_var)
    list.append(url_var)
            
    if len(list) < 1:
        list.append(url_page)   
    else: 
        list.pop()
                
            """  

