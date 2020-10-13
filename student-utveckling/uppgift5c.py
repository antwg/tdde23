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


def test_generator_from_image():
    test_if_function()
    test_pixel_rgb_values([(0,0,0), (0,128,255), (255,0,128)], 0)
    test_pixel_rgb_values([(0,0,0), (0,128,255), (255,0,128)], 1)
    test_pixel_rgb_values([(0,0,0), (0,128,255), (255,0,128)], 2)
    print('Passed all tests')


def test_if_function():
    """Tests if a function returns a function"""
    var = generator_from_image('list')
    assert(callable(var) == True)


def test_pixel_rgb_values(image_list, pixel):
    """Tests if function returns the correct rgb values of a pixel"""
    func = generator_from_image(image_list)
    assert(func(pixel) == (image_list[pixel][0], image_list[pixel][1],
    image_list[pixel][2]))


def test_combine_images():
    pass
