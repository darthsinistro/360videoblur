import cv2 as cv

capture = cv.VideoCapture('sample_video\PXL_20230211_235835765.TS.mp4')

# How many frames are there in the video anyway?
print(capture.get(cv.CAP_PROP_FRAME_COUNT))

# Let's print a specific face only
capture.set(cv.CAP_PROP_POS_FRAMES, 500)
res, frame = capture.read()

cv.imshow('frame',frame)

cv.waitKey(0)