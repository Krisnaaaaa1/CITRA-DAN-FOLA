import cv2
from cv2 import waitKey

img=cv2.imread("boy1.jpg")

#konversi BGR dari variabel img ke colorpace HSV

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);
h, s, v = cv2.split(hsv)

#menampilkan band hue

cv2.imshow("hasil",hsv)
waitKey(0)
cv2.imshow("hsail",img)
waitKey(0)
