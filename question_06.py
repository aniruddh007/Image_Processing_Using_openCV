# Q.5 : Take the url of image as an input form the user and convert the given image into the grayscale 
# and save it in the jpg format when the ' s ' is pressed form the keyboard .

import cv2 as cv 

url = input( " Enter the url of the image \n" )
image = cv.imread( url )
cv.imshow( "input" , image )

output = cv.imread( url , 0 )
cv.imshow( "output" , output )

key = cv.waitKey(0)
if key == ord('s') :
    cv.imwrite("D:\openCV\q_06_output.jpg" , output)
cv.destroyAllWindows()
