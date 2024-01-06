import cv2
import numpy as np
import imutils
from imutils import contours


def process_image_and_array(image):
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    array = []

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)
        if (w>=4 and h>=4 and ar>=.5 and ar<= 2):
           array.append(c)

    cnt = contours.sort_contours(array,method="left-to-right")[0]
    bubbled = None
    count = 0

    for c in cnt:
        mask = np.zeros(thresh.shape, dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        mask = cv2.bitwise_and(thresh, thresh, mask=mask)
        total = cv2.countNonZero(mask)


        if bubbled is None or total > bubbled[0]:
           bubbled = (total, count)

        count += 1
    return bubbled[1]



# print(process_image_and_array(img))



# cv2.imshow("asd",img)
# cv2.waitKey(0)