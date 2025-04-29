# import requests
from bs4 import BeautifulSoup

# url = "https://kvantorium37.ru/"

# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60"
# }
# req = requests.get(url, headers=headers)

# src = req.text

# with open("Parsing/index3.html", "w", encoding="utf8") as file:
#     file.write(src)

with open("Parsing/index3.html", "r", encoding="utf8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

# find all function by tag
def find_all(tag):
    tag = soup.find_all(tag)
    for i in tag:
        print(i)

# get all links
def get_all_links():
    tags = soup.find_all("a")
    for tag in tags:
        link_text = tag.text
        link = tag.get("href")
        print(f"{link_text}:, {link}")

# get all alts
def get_all_alts_from_images():
    tags = soup.find_all("img")
    for tag in tags:
        alt = tag.get("alt")
        print(alt)

