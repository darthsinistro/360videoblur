import cv2 as cv
import numpy as np

# # capture = cv.VideoCapture('sample_video\PXL_20230211_235835765.TS.mp4')
capture = cv.VideoCapture(1)

# # How many frames are there in the video anyway?
# print(capture.get(cv.CAP_PROP_FRAME_COUNT))

# # Let's print a specific face only
# capture.set(cv.CAP_PROP_POS_FRAMES, 500)
# res, frame = capture.read()

# cv.imshow('frame',frame)

# cv.waitKey(0)

# # Reading in the live video

haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    isTrue, frame = capture.read()

    if isTrue:    
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # blurred = cv.GaussianBlur(frame, (3,3), 0)
        
        # mask = np.zeros((gray.shape[0],gray.shape[1],3), dtype='uint8')
        
        faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

        for (x,y,w,h) in faces_rect:
            # mask = cv.rectangle(mask, (x,y), (x+w,y+h), (255,255,255), thickness=-1)
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,0), thickness=-1)
        
        # final_frame = np.where(mask==(255,255,255), blurred, frame)

        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()