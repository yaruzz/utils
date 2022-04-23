from matplotlib.cm import get_cmap
import numpy as np
import torch 

def psudo_color(Array2d,colormap = 'plasma', percent = 95):
    array2d = Array2d.copy()
    cm = get_cmap(colormap)
    normalizer = np.percentile(array2d,percent)
    array2d /= (normalizer + 1e-6)
    array3d = cm(np.clip(array2d, 0., 1.0))[:, :, :3]*255#[:,:,::-1] #[H,W,3]
    array3d = np.uint8(array3d)
    #array3d = np.transpose(array3d, (2, 0, 1))

    return array3d