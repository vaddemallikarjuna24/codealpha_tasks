import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()

    data.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })

df = pd.DataFrame(data)

print(df)

df.to_csv("products.csv", index=False)

print("\nProject Completed Successfully!")