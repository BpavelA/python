from requests import get
from math import ceil
from pathlib import Path

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.721 YaBrowser/23.9.5.721 (corp) Yowser/2.5 Safari/537.36"}

# Тема 4.7 Деревья решений

mins = [1]
secs = [4]
urls = ['https://river-mskm9rtk-352.rutube.ru/hls-vod/IDwYAm-iyhGzj4Hj_kjWlg/1739871484/2556/0x5000039ce863a681/454619470d714aafa46e7065bd1b9db7.mp4/segment']


iters = 1

for x in range(iters):
 
  y = ceil((mins[x] * 60 + secs[x]))

  for i in range(0, y):
   
   if y <= 10 or (y <= 100 and i > 9) or (y > 100 and i >= 100):
    j = ''
   elif y > 100 and i < 10:
    j = '00'
   elif y > 100 and 9 < i < 100 or (y < 100 and  i < 10):
    j = '0'
   
   video_part = get(f'{urls[x]}-{i}-v1-a1.ts', headers=headers)
   Path(f'Python/Parsing/js_course/{x}').mkdir(parents=True, exist_ok=True)
   with open (f'Python/Parsing/js_course/{x}/part_{j}{i}.ts', "wb") as file:
    file.write(video_part.content)
   
   print(f'Загружено {i+1} из {y}')
   if i == y-1:
    print('Загрузка всех частей успешно завершена!')
