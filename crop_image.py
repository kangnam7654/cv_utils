import cv2

def crop_image(image):
    crop_x1 = 0
    crop_x2 = 100
    crop_y1 = 0
    crop_y2 = 100
    
    cropped_image = image[crop_x1: crop_x2, crop_y1: crop_y2, :]
    return cropped_image