import os
from dotenv import load_dotenv
import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd

load_dotenv()

URL="/ecommerce/"

def get_url(page):
    return os.getenv("WEB_PAGE_URL")+page

response = rq.get(get_url(URL))

with open("web.html","w",encoding="utf-8") as f:
    f.write(response.text)

print("Statut code:", response.status_code)