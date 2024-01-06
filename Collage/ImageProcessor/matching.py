import cv2
import numpy as np
import imutils
from imutils import contours
import process
import process_test
from process import ar
from process_test import br
from process import new_crop as img1
from process_test import new_crop as img2



chemistry = 0
physics = 0
math = 0
english = 0
analytical = 0

for i in range(0,25):
    physics +=  (ar[i] == br[i])

for i in range(25,40):
    chemistry +=  (ar[i] == br[i])

for i in range(40, 70):
    math += (ar[i] == br[i])

for i in range(70, 85):
    english += (ar[i] == br[i])

for i in range(85, 100):
    analytical += (ar[i] == br[i])


print(physics)
print(chemistry)
print(math)
print(english)
print(analytical)
cv2.waitKey(0)
cv2.destroyAllWindows()