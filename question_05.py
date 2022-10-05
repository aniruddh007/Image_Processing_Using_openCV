# Q.4 : Take the url of image as an input form the user and convert the given image into the grayscale 
# and save it in the jpg format .

import cv2 as cv 

url = input("Enter the url of the image ..... \n")

image = cv.imread(url)
cv.imshow("input" , image )

out = cv.imread( url , 0 )
cv.imshow("output image " , out )

cv.imwrite("D:\openCV\q_05_output.jpg" , out )

cv.waitKey(0)
cv.destroyAllWindows() 
