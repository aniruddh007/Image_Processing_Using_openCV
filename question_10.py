# create the function which helps to find the coordinates of any pixel and its color value .

import cv2 as cv 

def mouse_events( event , x , y , flag , param ):
        
        
        font = cv.FONT_HERSHEY_PLAIN
        if( event == cv.EVENT_LBUTTONDOWN):
                
                print( "x : " , x , " y : " , y )
                coordinates = ". ( " + str(x) + " , " + str(y) + " )" 
                cv.putText( img , coordinates , (x,y) , font , 1 , (155 , 125 , 0) , 2 )
                
        
cv.namedWindow( winname = "res" )
img = cv.imread("D:\openCV\collage.jpg")
cv.setMouseCallback( 'res' , mouse_events)
while True :
    cv.imshow( 'res' , img )
    if cv.waitKey(1) == 27 :
        break 
cv.destroyAllWindows() 
