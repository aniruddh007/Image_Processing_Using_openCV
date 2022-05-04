# Q.1 : Take the url of image and show it as the output 

import cv2 as cv # importing cv2 library in code 

img = cv.imread("D:\openCV/collage.jpg") # taking the image as the input 

print(img) # printing the image array

cv.imshow( "output" , img ) # to show the output window 

cv.waitKey() # decides for how much time the window will appear 

cv.destroyAllWindows() # for termination 
