# take the url of the video and convert it into the frames and save them in a folder 

import cv2 as cv 

vidcap = cv.VideoCapture("D:\\openCV\\test.mp4")

ret , image = vidcap.read() 
count = 0 
while True :
    if ret == True :
        cv.imwrite("D:\\openCV\\frames_q_08\imgN%d.jpg" %count , image )
        vidcap.set(cv.CAP_PROP_POS_MSEC,(count*60))
        ret,image = vidcap.read()
        cv.imshow("video", image )
        count+=1   
        if cv.waitKey(1) == ord('q'):
            break 
            cv.destroyAllWindows()
vidcap.release()
cv.destroyAllWindows()

