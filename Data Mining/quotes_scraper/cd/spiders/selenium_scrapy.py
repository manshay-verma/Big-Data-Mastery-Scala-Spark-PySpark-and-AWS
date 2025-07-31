from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# driver.get("https://www.google.com")
# print("✅ Selenium is working without manual driver setup!")
# driver.quit()

driver.get("https://quotes.toscrape.com/js/")

time.sleep(2)

quotes = driver.find_elements(By.CLASS_NAME, "quote")
for quote in quotes:
    text = quote.find_element(By.CLASS_NAME,"text").text
    author = quote.find_element(By.CLASS_NAME,"author").text
    print(f"{text} - {author}")

driver.quit()