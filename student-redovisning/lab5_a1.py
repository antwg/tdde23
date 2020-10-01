import cv2
import math
import numpy as np

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

def negativ_gaussiks_blur(x, y):
    """
    Does the negativ gaussiks blur formula,
    but if both x and y are equal to 0 then return 1.5
    """
    if x == 0 and y == 0:
        return 1.5

    else:
        return (-1)*(1/(2*math.pi*(4.5**2)))*math.exp((-1)*((x**2 + y**2)/(2*(4.5**2))))

def unsharp_mask(N):
    """Returns a 2d-list used as in data for array-converting"""
    mask = []
    #find the coordinate for the middle of the array
    middle = N // 2


    mask = [[negativ_gaussiks_blur(x - middle, y - middle) for y in range(N)]for x in range(N)]

    return np.array(mask)


def test():
    img = cv2.imread('landscape.jpeg')
    kernel = np.array(unsharp_mask(11))
    filtered_img = cv2.filter2D(img, -1, kernel)
    cv2.imshow("filtered", filtered_img)
    cv2.waitKey(0)
