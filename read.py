import cv2 as cv2

img = cv.imread('photos/cat.jpg')

cv.imShow('Cat', img)

cv.waitKey(0)