import cv2

image = './smallgray.png'

im_g = cv2.imread(image, 1)
print(im_g)