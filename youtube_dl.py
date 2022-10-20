import os
import pickle
import subprocess
import numpy as np
from tqdm import tqdm
from pytube import YouTube
 

data_path = './data/TED_gesture-type_dataset.pickle'
save_dir = './videos/raw_videos/'

data = pickle.load(open(data_path, "rb"))
len(os.makedirs(save_dir, exist_ok=True))

video_ids = list(set(data['vid_id']))

for i in tqdm(range(len(video_ids))):
    video_id = video_ids[i]
    url = 'https://www.youtube.com/watch?v={}'.format(video_id)
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(save_dir, video_id+'.mp4')
    video_id =  video_id
    command = []
    command.append('youtube-dl')
    command.append('-o')
    command.append(save_dir + video_id + '.mp4')
    command.append('-f')
    command.append('mp4')
    command.append(video_id)
    subprocess.call(command)