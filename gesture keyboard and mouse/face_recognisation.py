# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 13:37:31 2021

@author: srcdo
"""

# import the modules
import cv2

# now we have the haarcascades files 
# to detect the face and eyes to detect the face
faces=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# to detect the eyes
eyes=cv2.CascadeClassifier('haarcascade_eye.xml')

# capture the frame through webcam
capture=cv2.VideoCapture(0)

# now running the loop for the webcam
while True:
    # reading the webcam
    ret,frame=capture.read()
    frame = cv2.flip(frame,1)
    # now the face is in the frame
    # the detection is done with the gray scale frame
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=faces.detectMultiScale(gray_frame,1.3,5)

    # now getting into the face and its position
    for (x,y,w,h) in face:
        # drawing the rectangle on the face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),thickness=4)

        # now the eyes are on the face
        # so we have to make the face frame gray
        gray_face=gray_frame[y:y+h,x:x+w]

        # make the color face also
        color_face=frame[y:y+h,x:x+w]

        # check the eyes on this face
        eye=eyes.detectMultiScale(gray_face,1.3,5)

        # get into the eyes with its position
        for (a,b,c,d) in eye:
            # we have to draw the rectangle on the
            # coloured face
            cv2.circle(color_face,(a,b),(a+c,b+d),(0,255,0),thickness=4)

    # show the frame
    cv2.imshow("Face Recognisation Frame",frame)
    if cv2.waitKey(1)==27:
        break

# after ending the loop release the frame
capture.release()
cv2.destroyAllWindows()
