import cv2
import random
import math
import numpy as np
from cvlib import *
from lab5_a import *
from uppgift5b import *


def test_pixel_constraint():
    #Test for pixel_constraint.
    def pixel_checker(pixel):
        """Checks if a given pixel is in the correct range of saturation, hue
        and value."""
        h = pixel[0]
        s = pixel[1]
        v = pixel[2]

        if 100 < h and h < 150 and 50 < s and s < 200 and 100 < v \
        and v < 255:
            return 1

        else:
            return 0
    hsv_plane = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV)
    plane_list = cvimg_to_list(hsv_plane)
    sky_pixels_result = cv2.cvtColor(cv2.imread("filtered_plane.jpg"), cv2.COLOR_BGR2HSV)
    sky_pixels_result_list = cvimg_to_list(sky_pixels_result)

    is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
    sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))
    def greyscale_to_tuple(list):
        result = []
        for i in list:
            result.append((0, 0, i))
        return result
    #print(greyscale_to_tuple(sky_pixels))
    #print(sky_pixels_result_list)
    def pixel_test(list1, list2):
        res = 0
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                res = res + 1
        print(res)
    pixel_test(greyscale_to_tuple(sky_pixels), sky_pixels_result_list)
    #assert(greyscale_to_tuple(sky_pixels) == sky_pixels_result_list)


"""
def test_generator_from_image():
    #Test for generator_from_image
    orig_img = cv2.imread("plane.jpg")
    orig_list = cvimg_to_list(orig_img)

    generator = generator_from_image(orig_list)

    new_list = [generator(i) for i in range(len(orig_list))]

    cv2.imshow('new', rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1]))
    cv2.waitKey(0)


    def test_combine_images():
        #Test for combine images

        # Läs in en bild
        plane_img = cv2.imread("plane.jpg")

        # Skapa ett filter som identifierar himlen
        condition = pixel_constraint(100, 150, 50, 200, 100, 255)

        # Omvandla originalbilden till en lista med HSV-fä?rger
        hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
        plane_img_list = cvimg_to_list(plane_img)

        # Skapa en generator som gör en stjärnhimmel
        def generator1(index):
            val = random.random() * 255 if random.random() > 0.99 else 0
            return (val, val, val)

        # Skapa en generator fö?r den inlä?sta bilden
        generator2 = generator_from_image(plane_img_list)

        # Kombinera de två bilderna till en, alltså anvä?nd himmelsfiltret som mask
        result = combine_images(hsv_list, condition, generator1, generator2)

            # Omvandla resultatet till en riktig bild och visa upp den
        new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
        cv2.imshow('Final image', new_img)
        cv2.waitKey(0)
"""
