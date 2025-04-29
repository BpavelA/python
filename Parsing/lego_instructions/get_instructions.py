from requests import get
from bs4 import BeautifulSoup
import os

#Step 1

url = "https://lencodigitexer.github.io/wedo/index.html"

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.721 YaBrowser/23.9.5.721 (corp) Yowser/2.5 Safari/537.36"}

# src = get(url, headers=headers)

# site = src.text

# with open("page.html", "w", encoding="utf8") as file:
#     file.write(site)

# Step 2

# with open("page.html", "r", encoding="utf8") as file:
#     src = file.read()

# soup = BeautifulSoup(src, "lxml")

# all_listItems = soup.find_all("a")

# result = {}

# for row in all_listItems:
#     name = row.text.strip()
#     signs = [' ']
#     for sign in name:
#        if sign in signs:
#           name = name.replace(sign, '_')
#     link = row.get("href")
#     result[name] = "https://lencodigitexer.github.io/wedo/" + link

# Делаем черновой список с ссылками и вручную его затем подчищаем (нужно отключить всякое форматирование файла html, иначе возникают непонятные разрывы)   

# with open('links.html', 'w', encoding='utf8') as file:
#    for key, value in result.items():
#        file.write(f'{key} {value} ')

# Снова считываем отредактированный файл и превращаем его в словарь

with open('Python/Parsing/lego_instructions/links_edited.html', 'r', encoding='utf8') as file:
    src = file.readlines()

links = {}
names = []
values = []

for line in src:
    key, value = line.split()
    names.append(key)
    values.append(value)

links = dict(zip(names, values))

# Прохожу по каждой ссылке, создаю папку и сохраняю туда страницу

# for name, url in links.items():
#     if not os.path.isdir(f'Python/Parsing/lego_instructions/{name}'):
#         os.mkdir(f'Python/Parsing/lego_instructions/{name}')
#     src = get(url, headers=headers)
#     page = src.text
#     with open(f'Python/Parsing/lego_instructions/{name}/{name}.html', 'w', encoding='utf8') as file:
#         file.write(page)

# Снова прохожусь по скачанным файлам и папкам. считываю и парсю

for name, url in links.items():
    new_dict ={}
    with open(f'Python/Parsing/lego_instructions/{name}/{name}.html', 'r', encoding='utf8') as file:
        src = file.read()
        soup = BeautifulSoup(src, "lxml")
        all_pdfNames = soup.find_all('big')
        all_pdfLinks = soup.find_all(class_ = "man")
        # print(all_pdfNames)

# Если имена совпадают, переименовываем
        counter = 0
        new_allPdfNames = []
        for item in all_pdfNames:
            if item.text not in new_allPdfNames:
                new_allPdfNames.append(item.text)
            else:    
                counter += 1
                new_allPdfNames.append(item.text + str(counter))

        new_dict = dict(zip(new_allPdfNames, all_pdfLinks))
        # print(new_dict)

        for key, value in new_dict.items():
            signs = [' ', ',', '"']
            pdf_url = value.get("href")
            pdf = get(pdf_url, headers=headers)
            for sign in key:
                if sign in signs:
                    key = key.replace(sign, '_')

            with open(f'Python/Parsing/lego_instructions/{name}/{key}.pdf', 'wb') as file:
                file.write(pdf.content)
