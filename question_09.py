# take the video and show the size and the current date and time on the video 

import cv2 as cv 
import datetime

video = cv.VideoCapture("D:\\openCV\\video.mp4")

print( "Width : " , video.get( cv.CAP_PROP_FRAME_WIDTH) )
print( "Height : " , video.get(cv.CAP_PROP_FRAME_HEIGHT) )

while (video.isOpened()):
    ret , frame = video.read() 
    
    if( ret == True ) :
        #ret , frame = video.read() 
        frame = cv.resize( frame , (1000 , 550))
        font = cv.FONT_HERSHEY_COMPLEX_SMALL
        text = 'height :' + str(video.get(cv.CAP_PROP_FRAME_HEIGHT)) + '  width :' + str(video.get(cv.CAP_PROP_FRAME_WIDTH))
        
        date = str(datetime.datetime.now()) 
        frame = cv.putText(frame , date , (10,50) , font , 2 , (255,255,255) , 1, cv.LINE_AA)
        cv.imshow( 'frame' , frame )
        frame = cv.putText( frame , text , (10,100) , font , 2 , (255,255,255) , 1, cv.LINE_AA)
        cv.imshow( 'frame' , frame)
    
        key = cv.waitKey(30) 
        if key == 27 :
            break 
    else :
        break
cv.destroyAllWindows()
