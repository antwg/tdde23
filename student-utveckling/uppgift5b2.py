"""cvlib module, helper functions for image and tuple manipulation."""

import cv2
import numpy

# ------------------------------------------
#  Helper functions
# ------------------------------------------


def multiply_tuple(tpl, mult):
    """Return a tuple where all elements are scaled by factor 'mult'.

    (a,b,c) * k = (a*k, b*k, c*k)
    """
    return tuple(map(lambda x: x*mult, tpl))


def add_tuples(tpl1, tpl2):
    """
    Return a the element-wise sum of tpl1 and tpl2.

    (a,b,c) + (d,e,f) = (a+d, b+e, c+f)
    """
    return tuple(map(lambda t1, t2: t1+t2, tpl1, tpl2))


# -------------------------------------------
#  Converting between python list and images
# -------------------------------------------


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


def greyscale_list_to_cvimg(lst, height, width):
    """Return a width x height grayscale OpenCV image with specified pixels."""
    img = numpy.zeros((height, width), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            img[y, x] = lst[y * width + x]

    return img

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

def generator_from_image(orig_list):
    """Converts an image in list form to a function returning the
    color of a given pixel"""
    def gen_func(pixel):
        return orig_list[pixel]
    return gen_func

"""
orig_img = cv2.imread("plane.jpg")
orig_list = cvimg_to_list(orig_img)

generator = generator_from_image(orig_list)

new_list = [generator(i) for i in range(len(orig_list))]

cv2.imshow('original', orig_img)
cv2.imshow('new', rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1]))
cv2.waitKey(0)
"""
