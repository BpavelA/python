from requests import get
from math import ceil
from pathlib import Path
from moviepy.editor import *

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.721 YaBrowser/23.9.5.721 (corp) Yowser/2.5 Safari/537.36"}

mins = [35, 43, 35, 68, 47, 11]
secs = [17, 38, 16, 16, 49, 52]
urls = ['https://stream2.1t.ru/hls/22/%D0%94%D0%B5%D0%BC%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F/%D0%94%D0%B6%D0%B0%D0%B2%D0%B0/%D0%92%D0%B5%D0%B1%D0%B8%D0%BD%D0%B0%D1%80%D1%8B_1%D0%BF%D0%BE%D1%82%D0%BE%D0%BA/3_4/270824_JS.IRPO_01.mp4/segment', 'https://stream2.1t.ru/hls/22/%D0%94%D0%B5%D0%BC%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F/%D0%94%D0%B6%D0%B0%D0%B2%D0%B0/%D0%92%D0%B5%D0%B1%D0%B8%D0%BD%D0%B0%D1%80%D1%8B_1%D0%BF%D0%BE%D1%82%D0%BE%D0%BA/3_4/270824_JS.IRPO_02.mp4/segment', 'https://stream2.1t.ru/hls/22/%D0%94%D0%B5%D0%BC%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F/%D0%94%D0%B6%D0%B0%D0%B2%D0%B0/%D0%92%D0%B5%D0%B1%D0%B8%D0%BD%D0%B0%D1%80%D1%8B_1%D0%BF%D0%BE%D1%82%D0%BE%D0%BA/3_4/270824_JS.IRPO_03.mp4/segment', 'https://stream2.1t.ru/hls/22/%D0%94%D0%B5%D0%BC%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F/%D0%94%D0%B6%D0%B0%D0%B2%D0%B0/%D0%92%D0%B5%D0%B1%D0%B8%D0%BD%D0%B0%D1%80%D1%8B_1%D0%BF%D0%BE%D1%82%D0%BE%D0%BA/3_4/280824_JS.IRPO_01.mp4/segment', 'https://stream2.1t.ru/hls/22/%D0%94%D0%B5%D0%BC%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F/%D0%94%D0%B6%D0%B0%D0%B2%D0%B0/%D0%92%D0%B5%D0%B1%D0%B8%D0%BD%D0%B0%D1%80%D1%8B_1%D0%BF%D0%BE%D1%82%D0%BE%D0%BA/3_4/280824_JS.IRPO_02.mp4/segment', 'https://stream2.1t.ru/hls/22/%D0%94%D0%B5%D0%BC%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F/%D0%94%D0%B6%D0%B0%D0%B2%D0%B0/%D0%92%D0%B8%D0%B4%D0%B5%D0%BE/%D0%9C%D0%BE%D0%B4%D1%83%D0%BB%D1%8C%203/%D0%A5%D0%B8%D1%82%D0%B1%D0%BE%D0%BA%D1%81%D1%8B%20%D0%B8%20%D1%81%D1%82%D0%BE%D0%BB%D0%BA%D0%BD%D0%BE%D0%B2%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20%D0%B8%D0%B3%D1%80%D0%B0%D1%85.mp4/segment']

iters = 6

path_to_videos = 'Python/Parsing/js_course/'

file_list = []

for x in range(iters):
 
  y = ceil((mins[x] * 60 + secs[x])/9)

  for i in range(0, y):
   
   if y <= 10 or (y <= 100 and i > 9) or (y > 100 and i >= 100):
    j = ''
   elif y > 100 and i < 10:
    j = '00'
   elif y > 100 and 9 < i < 100 or (y < 100 and  i < 10):
    j = '0'
   
   file_name = f'{path_to_videos}{x}/part_{j}{i+1}.ts'
   
   file_list.append(file_name)
   
   video_part = get(f'{urls[x]}{i+1}-v1-a1.ts', headers=headers)
   Path(f'{path_to_videos}{x}').mkdir(parents=True, exist_ok=True)
   with open (file_name, "wb") as file:
    file.write(video_part.content)
   
   print(f'Загружено {i+1} из {y}')
   if i == y-1:
    print('Загрузка всех частей успешно завершена!')
    print(f'Начинается сборка {x+1}-го видео')
  
  r_videos = []

  for video in file_list:
    v = VideoFileClip(video)
    r_videos.append(v)
    try:
        final_clip = concatenate_videoclips(r_videos, method="compose")
        final_clip.write_videofile(f'{path_to_videos}/{x}_final_video.mp4')
    except Exception as ex:
        print("Ничего не вышло :(")
        print(ex)