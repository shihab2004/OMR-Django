import cv2
import numpy as np
import imutils
from imutils import contours
import four_point
import crop_ans


#answer_img
image= cv2.imread("omr4.jpg")
# img = cv2.imread('omr4.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)
cnts = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
docCnt = None

if len(cnts) > 0:
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        if (len(approx) == 4):
            docCnt = approx
            break

# find the four point of a page ...here use four_point.py file
paper = four_point.four_point_transform(image, docCnt.reshape(4, 2))
warped = four_point.four_point_transform(gray, docCnt.reshape(4, 2))
#warped = warped[100:325,20:65]

th2 =  cv2.adaptiveThreshold(warped,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
thresh = cv2.threshold(th2, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts,_ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = max(cnts, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(cnts)
crop = warped[y:y+h, x:x+w]
crop = cv2.resize(crop,(388,388))
new_crop = crop.copy()

cv2.imshow("asdad",new_crop)
cv2.waitKey(0)

# ar = []

# #first_column_20-75

# ar.append(crop_ans.process_image_and_array(crop[20:50,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[45:70,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[65:90,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[85:110,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[100:120,20:75]))

# ar.append(crop_ans.process_image_and_array(crop[120:140,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[140:160,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[160:180,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[175:195,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[190:215,20:75]))

# ar.append(crop_ans.process_image_and_array(crop[210:230,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[225:250,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[245:265,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[260:285,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[280:300,20:75]))

# ar.append(crop_ans.process_image_and_array(crop[295:320,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[315:340,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[335:355,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[350:375,20:75]))
# ar.append(crop_ans.process_image_and_array(crop[370:385,20:75]))

# #Second_column_95-150

# ar.append(crop_ans.process_image_and_array(crop[5:25,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[25:50,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[45:70,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[65:90,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[80:105,95:150]))

# ar.append(crop_ans.process_image_and_array(crop[120:140,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[140:160,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[160:180,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[175:195,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[190:215,95:150]))

# ar.append(crop_ans.process_image_and_array(crop[210:230,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[225:250,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[245:265,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[260:285,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[280:300,95:150]))

# ar.append(crop_ans.process_image_and_array(crop[295:320,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[315:340,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[335:355,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[350:375,95:150]))
# ar.append(crop_ans.process_image_and_array(crop[370:388,95:150]))


# #Third_column_175-230


# ar.append(crop_ans.process_image_and_array(crop[20:50,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[45:70,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[65:90,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[85:110,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[100:120,175:230]))

# ar.append(crop_ans.process_image_and_array(crop[120:140,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[140:160,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[160:180,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[175:195,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[190:215,175:230]))

# ar.append(crop_ans.process_image_and_array(crop[210:230,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[225:250,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[245:265,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[260:285,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[280:300,175:230]))

# ar.append(crop_ans.process_image_and_array(crop[295:320,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[315:335,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[335:355,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[350:370,175:230]))
# ar.append(crop_ans.process_image_and_array(crop[370:388,175:230]))

# #fourth_column_250-305

# ar.append(crop_ans.process_image_and_array(crop[5:25,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[25:50,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[45:70,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[65:90,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[80:105,250:305]))

# ar.append(crop_ans.process_image_and_array(crop[100:120,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[120:140,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[140:160,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[160:180,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[180:200,250:305]))

# ar.append(crop_ans.process_image_and_array(crop[210:230,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[225:250,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[245:265,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[260:285,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[280:300,250:305]))

# ar.append(crop_ans.process_image_and_array(crop[295:320,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[315:335,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[335:355,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[350:370,250:305]))
# ar.append(crop_ans.process_image_and_array(crop[370:388,250:305]))

# #fifth_column_325-385

# ar.append(crop_ans.process_image_and_array(crop[5:25,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[25:45,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[45:70,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[65:85,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[80:105,325:385]))


# ar.append(crop_ans.process_image_and_array(crop[120:140,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[140:160,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[160:180,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[175:195,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[190:215,325:385]))

# ar.append(crop_ans.process_image_and_array(crop[210:230,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[225:245,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[245:265,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[260:285,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[280:300,325:385]))

# ar.append(crop_ans.process_image_and_array(crop[295:315,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[315:335,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[333:350,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[345:370,325:385]))
# ar.append(crop_ans.process_image_and_array(crop[370:388,325:385]))
