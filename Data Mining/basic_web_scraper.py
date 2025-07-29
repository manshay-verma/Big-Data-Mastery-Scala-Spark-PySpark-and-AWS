import requests
from bs4 import BeautifulSoup

# step 1: Website access karo
url = "https://rupesh.vercel.app/"
response = requests.get(url)

# step 2: soup object banao
soup = BeautifulSoup(response.text,'html.parser')

# step 3: Sare quotes find karo
quotes = soup.find_all('span',class_= 'text')
auother_name = soup.find_all('small', class_='author')

# step 4: print each quote
for i,quote in enumerate(quotes ,start=1):
    print(f"{i}. {quote.text}")
