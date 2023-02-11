import requests
from bs4 import BeautifulSoup

url = "https://www.mbank.pl/serwis-ekonomiczny/kursy-walut/"
resp = requests.get(url)
soup = BeautifulSoup(resp.content, "html.parser")

# tag informs from which day the exchange rate is
tag = soup.find("div", class_="table_0")
tag = tag.find("p", class_="title")
tag = tag.get_text().strip()
tag = tag.split("\t")
tag = tag[-1]
print(f"{tag}:\n")

# finding the exchange rate table
soup = soup.find("tbody")
soup = soup.find_all("tr", class_="")

# getting informations from each table row
for tr in soup:
    row = tr.find_all("td")
    name = row[0].get_text().strip()
    curr = row[1].get_text().strip()
    buyR = row[4].get_text().strip()
    sellR = row[5].get_text().strip()
    avgR = row[6].get_text().strip()
    print(f"Currency: {curr} ({name})")
    print(f"Buy rate: {buyR}")
    print(f"Sell rate: {sellR}")
    print(f"Average rate: {avgR}")
    print("-" * 18)
    




