import os
import sys
import subprocess


path_to_root = "/media/dharani/62e5bcf5-360d-4eaa-96fd-12679ba22eaf/home/dharani/PycharmProjects/VIBE/data/vibe_db/mpi_inf_3dhp"
user_list = range(1, 9)
seq_list = range(1, 3)
vid_list = list(range(3)) + list(range(4, 9))

def convert_video_to_frames(video_path):
    if not os.path.exists(video_path):
        os.makedirs(video_path)
    # Construct the paths and names
    path_to_video = f"{video_path}.avi"
    output_template = f"{video_path}/_%06d.jpg"
    

    # Run the ffmpeg command
    command = [
        'ffmpeg',
        '-i', path_to_video,
        '-qscale:v', '1',
        output_template
    ]
    
    subprocess.run(command)


for user_i in user_list:
    for seq_i in seq_list:
        seq_path = os.path.join(path_to_root,'S' + str(user_i),'Seq' + str(seq_i)+"/imageSequence")
        for j,vid_i in enumerate(vid_list):
            imgs_path = seq_path + ('/video_' + str(vid_i))

            print(imgs_path)
            convert_video_to_frames(imgs_path)