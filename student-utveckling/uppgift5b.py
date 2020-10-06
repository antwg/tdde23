import cv2
import random
import math
import numpy as np
from cvlib import *


def rgblist_to_cvimg(lst, height, width):
    """Return a width x height OpenCV image with specified pixels."""
    # A 3d array that will contain the image data
    img = np.zeros((height, width, 3), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            pixel = lst[y * width + x]
            img[y, x, 0] = pixel[0]
            img[y, x, 1] = pixel[1]
            img[y, x, 2] = pixel[2]

    return img


def rgblist_to_cvimg(lst, height, width):
    """Return a width x height OpenCV image with specified pixels."""
    # A 3d array that will contain the image data
    img = numpy.zeros((height, width, 3), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            pixel = lst[y * width + x]
            img[y, x, 0] = pixel[0]
            img[y, x, 1] = pixel[1]
            img[y, x, 2] = pixel[2]

    return img

#5a
def cvimg_to_list(img):
    """Takes an OpenCV picture and returns a list with BGR tuples."""
    pixlar = []
    rader = img.shape[0]
    kolumn = img.shape[1]

    for x in range(rader):
        for y in range(kolumn):
            pixel = img[x, y]
            pixlar.append((pixel[0], pixel[1], pixel[2]))

    return pixlar

#5b1
def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """Checks if a given pixel is in the correct range of saturation, hue and
    value."""
    def pixel_checker(pixel):
        h = pixel[0]
        s = pixel[1]
        v = pixel[2]

        if hlow < h and h < hhigh and slow < s and s < shigh and vlow < v \
        and v < vhigh:
            return 1

        else:
            return 0

    return pixel_checker

#5b2
def generator_from_image(orig_list):
    """Converts an image in list form to a function returning the
        color of a given pixel."""
    def gen_func(pixel):
        return orig_list[pixel]
    return gen_func


#5b3
def combine_images(hsv_list, condition, generator1, generator2):
    sky_pixels = list(map(lambda x: x * 255, map(condition, hsv_list)))
    final_image = []
    for i in range(len(hsv_list)):
        if sky_pixels[i] == 1:
            final_image.append(generator1())
        else:
            final_image.append(generator2(i))
    print(sky_pixels)
    return final_image

def test():
    # Lä?s in en bild
    plane_img = cv2.imread("plane.jpg")

    # Skapa ett filter som identifierar himlen
    condition = pixel_constraint(100, 150, 50, 200, 100, 255)

    # Omvandla originalbilden till en lista med HSV-fä?rger
    hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
    plane_img_list = cvimg_to_list(plane_img)

    # Skapa en generator som gö?r en stjä?rnhimmel
    def generator1(index):
        val = random.random() * 255 if random.random() > 0.99 else 0
        return (val, val, val)

    # Skapa en generator fö?r den inlä?sta bilden
    generator2 = generator_from_image(plane_img_list)

    # Kombinera de två? bilderna till en, alltså? anvä?nd himmelsfiltret som mask
    result = combine_images(hsv_list, condition, generator1, generator2)

        # Omvandla resultatet till en riktig bild och visa upp den
    new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
    cv2.imshow('Final image', new_img)
    cv2.waitKey(0)
