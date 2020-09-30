import cv2
def cvimg_to_list(img):
    """Takes an OpenCV picture and returns a list with BGR tuples"""
    pixlar = []
    rader = img.shape[0]
    kolumn = img.shape[1]

    for x in range(rader):
        for y in range(kolumn):
            pixel = img[x, y]
            pixlar.append((pixel[0], pixel[1], pixel[2]))

    return pixlar
