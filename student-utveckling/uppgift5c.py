import cv2
import random
import math
import numpy as np
from cvlib import *
from lab5_a import *
from uppgift5b import *


def test_pixel_constraint():
    """ performs several test on the pixel constraint function """

    test_data = (((101, 101, 101), 1), \
        ((99, 99, 99), 0),\
        ((100000, 100000, 100000), 0),\
        ((100, 100, 100), 0),\
        ((102, 102, 102), 0))

    test_function = pixel_constraint(100, 102, 100, 102, 100, 102)
    assert(callable(test_function) == True)

    for test in test_data:
        assert test_function(test[0]) == test[1]


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
