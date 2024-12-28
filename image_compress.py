import cv2

from cv2 import imwrite

def image_compression(image_file):
    img = cv2.imread(image_file)
    imwrite("Compressd.jpg", img, [cv2.IMWRITE_JPEG_QUALITY,10])
    print("Image is compressed")

image_compression("image2.jpg")