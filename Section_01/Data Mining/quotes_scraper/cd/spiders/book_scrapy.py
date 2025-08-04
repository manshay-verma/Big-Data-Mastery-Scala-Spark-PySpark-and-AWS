import requests
from bs4 import BeautifulSoup
import csv
import json

base_url = "http://books.toscrape.com/catalogue/"
start_url = "http://books.toscrape.com/catalogue/page-1.html"

books = []

while start_url:
    print(f"Scraping:{start_url}")
    response = requests.get(start_url)
    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one("p.price_color").text
        availability = book.select_one("p.instock.availability").text.strip()
        rating = book.p["class"][1]

        books.append({
            "title":title,
            "price":price,
            "availability": availability,
            "rating": rating
        })

    next_btn = soup.select_one("li.next > a")
    if next_btn:
        start_url = base_url + next_btn["href"]
    else:
        start_url = None
with open("book.json", "w",encoding="utf-8") as f:
    json.dump(books, f, indent=4, ensure_ascii=False)
print(f'Scraped {len(books)} books!')