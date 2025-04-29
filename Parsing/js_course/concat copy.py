from moviepy.editor import *
from os import *

path_directory = 'Python/Parsing/js_course/1'

clip_in_dir = os.listdir(path_directory)
clip_to_merge = []

for clip in clip_in_dir:
    VideoFileClip(os.path.join(path_directory, clip))
    clip_to_merge.append(VideoFileClip(os.path.join(path_directory, clip)))
        
    merge_final = concatenate_videoclips(clip_to_merge, method="compose")
    merge_final.write_videofile(os.path.join(os.getcwd(), 'full_clip.ts'))