# Q.4 : take the url of the image , resize it and show both the input and the output image 

import cv2 as cv 

img = cv.imread("D:\openCV\collage.jpg")

cv.imshow( "orignal image " , img )

img = cv.resize( img , ( 700 , 500 ) ) # width . height 

cv.imshow("resized image " , img )

cv.waitKey()
cv.destroyAllWindows() 
