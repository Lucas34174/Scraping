import requests as rq 
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv("../.env")
article = []
index = 1

URL=os.getenv("WEB_PAGE_URL")+ "/pagination/"

while True:
    response = rq.get(next_url if index > 1 else URL)
    soup = bs(response.text, "html.parser")
    items = soup.find_all("div",class_="product-info self-start text-left w-full")
    for item in items:
        product_name = item.find("span",class_="product-name").text.strip()
        product_price = item.find("span",class_="product-price text-slate-600").text.strip()
        article.append({"page": index, "product": product_name, "price": product_price})

    next = soup.find("a",class_="next-page px-2 sm:px-4 py-2 mx-1 rounded text-black hover:bg-[#0A2BFF] hover:text-white")
    if not next:
        break
    next_url = next.get("href")
    index += 1

df = pd.DataFrame(article)
print(df)
df.to_csv("data.csv", index=False, encoding="utf-8", header=["Page", "Product", "Price"])