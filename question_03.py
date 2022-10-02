# Q.3 : take the url of the image , convert it into the grayscale and show the output window for only 5 seconds 

import cv2 as cv 

img = cv.imread("D:\openCV\collage.jpg" , 0 )

cv.imshow( "output image " , img )

cv.waitKey( 5000 )
cv.destroyAllWindows()
 
