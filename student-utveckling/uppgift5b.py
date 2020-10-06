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
    mask = list(map(condition, hsv_list))
    final_image = []
    for i in range(len(hsv_list)):
        colour = mask[i]
        pixel1 = generator1(i)
        pixel2 = generator2(i)
        hue = pixel1[0] * colour + pixel2[0] * (1 - colour)
        saturation = pixel1[1] * colour + pixel2[1] * (1 - colour)
        value = pixel1[2] * colour + pixel2[2] * (1 - colour)
        final_image.append((hue, saturation, value))
    return final_image

def gradient_condition(pixel):
    return pixel[2]/255

def test1():
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

def test2():
    plane_img = cv2.imread("plane.jpg")
    flower_img = cv2.imread("flowers.jpg")
    gradient_img = cv2.imread("gradient.jpg")


    hsv_list = cvimg_to_list(cv2.cvtColor(gradient_img, cv2.COLOR_BGR2HSV))
    plane_img_list = cvimg_to_list(plane_img)
    flower_img_list = cvimg_to_list(flower_img)

    generator1 = generator_from_image(flower_img_list)
    generator2 = generator_from_image(plane_img_list)

    result = combine_images(hsv_list, gradient_condition, generator1, generator2)

    new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
    cv2.imshow('Final image', new_img)
    cv2.waitKey(0)
