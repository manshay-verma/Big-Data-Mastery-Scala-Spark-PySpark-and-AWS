#request and beautifulsoup4 1st lecture 

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# quotes = soup.select("div.quote span.text")
# authors = soup.select("div.quote small.text")

for quote, author in zip(quotes, authors):
    print(f"Quote : {quote.text} \n Authos: {author.text}")
    
for quote in soup.select("div.quote"):
    text = quote.select_one("span.text").text
    author = quote.select_one("small.author").text
    tags = [tag.text for tag in quote.select("div.tags a.tags")]
    print(f"{text} - {author} \n Tag :- {','.join(tags)}")