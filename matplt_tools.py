from matplotlib.cm import get_cmap
import numpy as np
import cv2

def psudo_color(Array2d,colormap = 'plasma', percent = 95):
    array2d = Array2d.copy()
    cm = get_cmap(colormap)
    normalizer = np.percentile(array2d,percent)
    array2d /= (normalizer + 1e-6)
    array3d = cm(np.clip(array2d, 0., 1.0))[:, :, :3]*255#[:,:,::-1] #[H,W,3]
    array3d = np.uint8(array3d)
    #array3d = np.transpose(array3d, (2, 0, 1))

    return array3d

def draw_lidar(gt,img):
    # Keep valid pixels (min/max depth and crop)
    valid = (gt > 0) 


    y,x = np.where(valid==True)
    x= np.expand_dims(x,0)
    y =np.expand_dims(y,0)
    coor = np.concatenate((x,y),axis=0).transpose()

    gt = gt.clip(0,250)
    gt = ((gt - gt.min()) / (gt.max() - gt.min())* 255).astype(np.uint8)
    gt = np.array(cv2.applyColorMap(gt, cv2.COLORMAP_JET))  # 是蓝色的3通道heatmap
    depth_value = gt[valid]
    v_shape = depth_value.shape[0]
    for i in range(v_shape):
        cv2.circle(img,tuple(coor[i]),2,tuple(depth_value[i].tolist()),-1)
    return img