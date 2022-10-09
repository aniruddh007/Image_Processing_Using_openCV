# take an image and use the functions like size shape type and dtype on that image and show the output

import cv2 as cv 
import numpy as np 


img = cv.imread("D:\\openCV\\collage.jpg")

# using the shape function
print("Shape function : " , img.shape)

# using the size function 
print("Total number of pixels in the image :" , img.size)

# using the type and dtype function 

print("Type of image : " , type(img)) 

frame = img.dtype 
print("Dataype of the elements stored in the array : " , frame)

cv.destroyAllWindows()
