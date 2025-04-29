from moviepy.editor import *

path_to_files = 'Python/Parsing/js_course/'

r_videos = []
videos = ['Python/Parsing/js_course/part_001.ts','Python/Parsing/js_course/part_002.ts']



for video in videos:
    v = VideoFileClip(video)
    r_videos.append(v)
    try:
        final_clip = concatenate_videoclips(r_videos, method="compose")
        final_clip.write_videofile(f"Python/Parsing/js_course/final.mp4")
    except Exception as ex:
        print("Ничего не вышло :(")
        print(ex)