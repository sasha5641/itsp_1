import cv2


image_path = 'cat.jpeg'

image = cv2.imread(image_path)
cv2.imshow('CAT', image)
cv2.waitKey()

