import cv2
import os

output_dir = "output_images"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

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
        print("Writing image...")
        output_filename = "test.png"
        cv2.imwrite(os.path.join(output_dir, output_filename), frame);
        print(f"Image '{output_filename}' written.\n")

cv2.destroyWindow("Image Preview")