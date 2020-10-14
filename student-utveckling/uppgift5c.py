import cv2
import random
import math
import numpy as np
from cvlib import *
from lab5_a import *
from uppgift5b import *


def test_pixel_constraint():
    """ performs several test on the pixel constraint function """

    #the first element in then tuple is the in data and the second is result
    test_data = (((101, 101, 101), 1), \
        ((99, 99, 99), 0),\
        ((100000, 100000, 100000), 0),\
        ((100, 100, 100), 0),\
        ((102, 102, 102), 0))

    #test if the variabel is a function
    test_function = pixel_constraint(100, 102, 100, 102, 100, 102)
    assert(callable(test_function) == True)

    #test if the given a specific data gives the expected result
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
    """Test the combine_images function"""

        test_data_1 = (([(1,1,226), (23,24,224), (55,65,227)],\
         [(123, 123, 123), (50, 50, 50), (123, 123, 123)]),\
         ([(34,24,224), (54,23,226), (5,98,230)],\
          [(50, 50, 50), (123, 123, 123), (123, 123, 123)]))

        test_data_2 = (([(0,0,226), (0,0,224), (0,0,228)],\
         [(114.69803921568626, 114.69803921568626, 114.69803921568626),\
         (114.12549019607843, 114.12549019607843, 114.12549019607843),\
         (115.27058823529413, 115.27058823529413, 115.27058823529413)]),\
         ([(0,0,300), (0,0,0), (0,0,1000)],\
         [(135.8823529411765, 135.8823529411765, 135.8823529411765),\
         (50.0, 50.0, 50.0),\
         (336.27450980392155, 336.27450980392155, 336.27450980392155)]))

        def generator1(index):
            return(123, 123, 123)

        def generator2(index):
            return(50, 50, 50)

        condition_1 = pixel_constraint(0, 255, 0, 255, 225, 255)

        def condition_2(pixel):
            return pixel[2]/255

        for test in test_data_1:
            assert combine_images(test[0], condition_1, generator1, generator2) == test[1]

        for test in test_data_2:
            assert combine_images(test[0], condition_2, generator1, generator2) == test[1]

        print("combine_images passed all the test!")

def generator_from_image(orig_list):
    """Converts an image in list form to a function returning the
        color of a given pixel."""
    def gen_func(pixel):
        """Returns the rgb value of a pixel."""
        try:
            return orig_list[pixel]
        except IndexError:
            return "That pixel does not exist please input anumber between 0 and "\
             + str(len(orig_list) - 1)
    return gen_func

def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """Returns a function that checks if a given pixel is range of given hsv
    parameters."""
    def pixel_checker(pixel):
        """Checks if a given pixel is in the correct range of saturation, hue
        and value."""
        try:

            h = pixel[0]
            s = pixel[1]
            v = pixel[2]

            test_if_numeric = h + s + v

            if  hlow < h and h < hhigh\
            and slow < s and s < shigh\
            and vlow < v and v < vhigh:
                return 1

            else:
                return 0

        except IndexError:
            return ("The given tuple " + str(pixel) +\
            " could not be interperted as a pixel please input tuples with"
            " atleast 3 elements")

        except TypeError:
            return ("The given tuple " + str(pixel) + " had one or more element"
             " which were not an interger or float")

    return pixel_checker

plane_img = cv2.imread("plane.jpg")
condition = pixel_constraint(100, 150, 50, 200, 100, 255)

hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
plane_img_list = cvimg_to_list(plane_img)

def generator1(index):
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)

generator2 = generator_from_image(plane_img_list)

result = combine_images([(0,0,0)], condition, generator1, generator2)
