# pagination learning using next page
import requests
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com"
next_page = "/"

while next_page:
    response = requests.get(base_url + next_page)
    soup = BeautifulSoup(response.text, "html.parser")

    for quote in soup.select("div.quote"):
        text = quote.select_one("span.text").text
        author = quote.select_one("small.author").text
        print(f"{text}{author}")

    next_btn = soup.select_one("li.next>a")
    if next_btn:
        next_page = next_btn["href"]
    else:
        next_page = None