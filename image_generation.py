from typing import Union
import numpy as np
from PIL import Image

def generate_image(resolution: Union[int, tuple, list], noise=True, gray_scale=False, return_type='cv'):
    
    if isinstance(resolution, int):
        pass
    elif isinstance(resolution, tuple):
        pass
    elif isinstance(resolution, list):
        pass
    
    cvtype = ['cv']
    torchtype = ['pt']
    
    
    canverse = np.random.randint(0, 255, resolution, dtype=np.uint8)
    
    if return_type in cvtype:
        return canverse
    elif return_type in torchtype:
        return canverse
    else:
        return None