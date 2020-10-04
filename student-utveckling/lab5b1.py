import cv2
from cvlib import greyscale_list_to_cvimg

# ----------------------------------------------------------------------------------
def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
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
# ------------------------------------------------------------------------------

is_black = pixel_constraint(0, 255, 0, 255, 0, 10)
print(is_black((231, 82, 4)))
print(is_black((231, 82, 199)))

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

def test():
    hsv_plane = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV)
    plane_list = cvimg_to_list(hsv_plane)

    is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
    sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))

    cv2.imshow('sky', greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
    cv2.waitKey(0)
