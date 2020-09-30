import cv2
# ======================================================================
def range_product(x, y):
    """
    multiplies the product of a specified range of numbers
    """
    #if x is equals to why stop the recursion
    if x == y:
        return x

    else:
        # print(x, y)
        return x * range_product((x + 1), y)

def factorial(x):
    """
    Return the factorial of a given number
    """
    #if 0 then return 1 becasue 0! = 1
    if x == 0:
        return 1

    else:
        return range_product(1, x)

def choose(x, y):
    """
    determined the amount of combination of two given parameters
    """
    print('meh')
    print(x, y)
    if y == 0:
        y = x
    # if they are both the same then return 1
    if x == y:
        return 1
    #if x double as large than y. This convert the combination first to its corresponding combination ie.( 1000c998 = 1000c2)
    elif x/2 > y:
        return (range_product((x - y + 1), x))//factorial(y)
    #other wise if y is larger
    else:
        return (range_product((y + 1), x))//factorial(x-y)
# =========================================================================

def remove_blue(image):
    """ remove the blue colour of an image"""

    img = cv2.imread(image)
    rader = img.shape[0]
    kolumner = img.shape[1]

    for x in range(rader):
        for y in range(kolumner):
            pixel = img[x, y]
            img[x, y] = (0, pixel[1], pixel[2])

    cv2.imshow("Blue removed from image", img)
    cv2.waitKey(0)

def double_elements(list):
    return [element*2 for element in list]

def all_pairs_ordered(number):
    return [(x,y) for y in range(number+1) for x in range(number+1)]

def distribute(str, list):
    return  [element + [str] for element in list]

def pascal(number):
    meh = [[choose(x, y) for y in range(x+1)] for x in range(number)]
    print(meh)

print(distribute('k', [['o'], [0, 1, 2], ['o', 'o']]))
print(all_pairs_ordered(2))
print(double_elements([1, 2, 3, 4]))
pascal(3)
print(choose(0,0))
