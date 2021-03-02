import cv2

image = cv2.imread("image.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert_image = 255 - gray_image
blur_image = cv2.GaussianBlur(invert_image, (21, 21), 0)
inverted_blur_image = 255 - blur_image
sketch_image = cv2.divide(gray_image, inverted_blur_image, scale=256.0)
# Saving Image
cv2.imwrite("sketch.jpg", sketch_image)
