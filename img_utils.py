import os 
import numpy as np
import imageio
import cv2
from dir_utils import read_dir_as_list
    
def create_gif(image_list, gif_name):
    frames = []
    for image_path in image_list:
        frames.append(imageio.imread(image_path))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.1)
    
def create_video(img_root_path,video_path,fps=20):
    img_list = read_dir_as_list(img_root_path)
    H,W = cv2.imread(img_list[0]).shape[0],cv2.imread(img_list[0]).shape[1]
    size = (W,H)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videowriter = cv2.VideoWriter(video_path,fourcc,fps,size)

    for path in img_list:
        frame= cv2.imread(path)
        videowriter.write(frame)
    videowriter.release()

def tensor2rgb(tensor):
    # Normalization Parameters
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]
    mean = np.array(mean).reshape(3,1,1)
    std = np.array(std).reshape(3,1,1)    
    # De-Normalization 
    image = tensor * std + mean 
    image = np.clip(image.numpy() * 255, 0, 255) #(C,H,W)
    #image = image[::-1,:,:] 
    image = image.transpose(1,2,0) #(H,W,C)
    return image