from requests import get

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.721 YaBrowser/23.9.5.721 (corp) Yowser/2.5 Safari/537.36"}

with open("Python/Parsing/lists/projects.txt", "r", encoding="utf8") as file:
    src = file.read().split("\n")

counter = 1
for link in src:
    project = get(link, headers=headers)
    with open(f'Python/Parsing/lists/files/{counter}.sb3', "wb") as file:
        file.write(project.content)
    counter += counter