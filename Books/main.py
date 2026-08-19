import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd

URL="https://books.toscrape.com/"

response = rq.get(URL)
books = []
if(response.status_code >= 200 and response.status_code < 300):
    soup =  bs(response.text,"html.parser")
    items = soup.find_all("article", class_="product_pod") 
    for item in items:
        book_title = item.find("h3").find("a")["title"]
        book_price = item.find("p", class_="price_color").text.strip().replace("Â", "")
        book_availability = item.find("p", class_="instock availability").text.strip()
        book_star_rating = item.find("p")["class"][1]
        books.append({"title": book_title, "price": book_price, "availability": book_availability, "star_rating": book_star_rating})
    
    df = pd.DataFrame(books)
    print(df)
    df.to_csv("books.csv",  encoding="utf-8", header=["Title", "Price", "Availability", "Star Rating"])
else:
    print("Erreur lors de la requête HTTP:", response.status_code)