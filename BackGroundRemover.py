import cv2
import numpy as np

from cvzone.SelfiSegmentationModule import SelfiSegmentation

cap = cv2.VideoCapture(0)

background = None

new_background_path = 'image2.jpg'
new_background = cv2.imread(new_background_path)
segmentor = SelfiSegmentation()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if new_background is not None:
        new_background = cv2.resize(new_background, (frame.shape[1], frame.shape[0]))


    imout = segmentor.removeBG(frame, new_background, cutThreshold= 0.5)

    cv2.imshow('Background Removal', imout)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()