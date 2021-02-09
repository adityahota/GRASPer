import cv2
vc = cv2.VideoCapture(0)
if vc.isOpened():
    rval, frame = vc.read() 
else:    
    rval = False

while rval: 
    cv2.imshow("Image Preview", frame) 
    rval, frame = vc.read() 
    key = cv2.waitKey(16) 
    if key == 27: # exit on ESC 
        break
    elif key == 32:
        cv2.imwrite("test.png", frame);

cv2.destroyWindow("Image Preview")