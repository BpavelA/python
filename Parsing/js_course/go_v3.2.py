from requests import get
from math import ceil
from pathlib import Path
from moviepy.editor import *
from os import *

# определяем путь до файлов

# for i in range(1):

path_to_files = f'Python/Parsing/js_course/1'

# получаем список файлов в папке
file_list = listdir(path_to_files)

# создаём список с объектами 
r_videos = []
for video in file_list:
  full_path = path_to_files + '/' + video
  v = VideoFileClip(full_path)
  r_videos.append(v)

# собираем
  final_clip = concatenate_videoclips(r_videos, method="compose")
  final_clip.write_videofile(f'{path_to_files}/final_video.mp4')

####################################################################

