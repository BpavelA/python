from bs4 import BeautifulSoup
with open("Mimo/idx.html", encoding="utf8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

# title = soup.title
# print(title.text)

# .find()
# .find_all()

all_p = soup.find_all("p")

for p in all_p:
    print(p.text)