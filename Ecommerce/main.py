import os
from dotenv import load_dotenv
import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd

load_dotenv("../.env")

URL="/ecommerce/"

def get_url(page):
    return os.getenv("WEB_PAGE_URL")+page

response = rq.get(get_url(URL))

# with open("web.html","w",encoding="utf-8") as f:
#     f.write(response.text)

soup = bs(response.text, "html.parser")

article = []
items = soup.find_all("a",class_="woocommerce-LoopProduct-link woocommerce-loop-product__link")
for item in items:
    product_name = item.find("h2",class_="product-name woocommerce-loop-product__title").text.strip()
    product_price = item.find("span",class_="price").find("bdi").text.strip()
    article.append({"product": product_name, "price": product_price})
    print("Product:", product_name, "Price:", product_price)

data = pd.DataFrame(article)
print(data)
data.to_csv("data.csv", index=False, encoding="utf-8", header=["Product","Price"])
