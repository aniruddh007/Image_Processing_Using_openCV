# Q.7 : take the url of the image as the input and convert it into the grayscale and flip vertically and resize the image
# and save the image by pressing ' s' from the keyboaard..

import cv2 as  cv 

url = input("Enter the url of the image :  \n")
image = cv.imread(url)
cv.imshow(" input image " , image )

output = cv.imread( url , 0 )
output = cv.resize(output , (700 , 300 ))
cv.imshow("output image" , output)

key = cv.waitKey()
if key == ord('s'):
    cv.imwrite("D:\openCV\q_07_output.jpg" , output)

cv.destroyAllWindows()

