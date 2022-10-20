import os
import pickle
import subprocess
from tqdm import tqdm

data_path = './data/TED_gesture-type_dataset.pickle'
video_dir = './videos/raw_videos/'
save_dir = "./videos/gesture_videos/"
fps = 25

data = pickle.load(open(data_path, "rb"))
os.makedirs(save_dir, exist_ok=True)

gesture_ids = data['gesture_id']

for i in tqdm(range(len(gesture_ids))):
    video_path = video_dir + data['vid_id'][i] + '.mp4'

    if not os.path.exists(video_path):
        continue

    save_path = save_dir + data['vid_id'][i] + '/' + gesture_ids[i] + '.mp4'
    if os.path.exists(save_path):
        continue
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    start = data['start_frame_no'][i]
    end = data['end_frame_no'][i]
    duration = end - start
    cmd = []
    cmd.append('ffmpeg')
    cmd.append('-ss')
    cmd.append(str(start/fps))
    cmd.append('-i')
    cmd.append(video_path)
    cmd.append('-t')
    cmd.append(str(duration/fps))
    cmd.append(save_path)
    cmd.append('-y')
    subprocess.call(cmd)


