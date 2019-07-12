import numpy as np
import cv2
import time

COLORS = [
        (0,255,0),      #green
        (255,0,0),      #red
        (0,0,255),      #blue
        (255,0,255),    #purple
        (0,255,255),    #yellow 
        (255,255,0),    #orange
        ]

def detect(cascades, test_image, scaleFactor = 1.2):

    image_copy = test_image.copy()

    #convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

    height, width, depth = image_copy.shape
    segment_width = int(width/3)
    cv2.line(image_copy, (segment_width,0), (int(width/3),height), (255,255,255), thickness=2, lineType=8, shift=0)
    cv2.line(image_copy, (2*segment_width,0), (int(2*width/3),height), (255,255,255), thickness=2, lineType=8, shift=0)

    all_boxes = []
    for idx,cascade in enumerate(cascades):
        rects = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=5)
        all_boxes.extend(rects)
        
        for (x, y, w, h) in rects:
            cv2.rectangle(image_copy, (x, y), (x+w, y+h), COLORS[idx%len(COLORS)], 1)
    
    output=[0,0,0]
        
    for box in all_boxes:
        x1,y1,x2,y2 = box
        center_x = int(x1+(x2/2))
        center_y = int(y1+(y2/2))
        #cv2.circle(image_copy, (center_x,center_y), 3, (255,255,255), thickness=2, lineType=8, shift=0) 
    
        segment = center_x//segment_width
        output[segment]+=1
        
    print(output)
    return output, image_copy

cap = cv2.VideoCapture(0)

#classifiers
haar_cascade_face = cv2.CascadeClassifier('D:/Anaconda3/envs/py36/Library/etc/haarcascades/haarcascade_frontalface_default.xml')
#haar_cascade_upperbody = cv2.CascadeClassifier('D:/Anaconda3/envs/py36/Library/etc/haarcascades/haarcascade_frontalface_alt.xml')
#haar_cascade_fullbody = cv2.CascadeClassifier('D:/Anaconda3/envs/py36/Library/etc/haarcascades/haarcascade_profileface.xml')

cascades = [haar_cascade_face]   #, haar_cascade_upperbody,haar_cascade_fullbody]

i = 0
buffer = []
while(True):
    time.sleep(0.4)
    i += 1
    if i%5 == 0:
        result = [0,0,0]
        for cl in buffer:
           result = [sum(x) for x in zip(result, cl)]
        buffer = []
        print("--------",result)
    
    # time.sleep(0.5)
    # Capture frame-by-frame
    ret, frame = cap.read()

    output, face_img = detect(cascades,  cv2.flip( frame, 1 ))
    buffer.append(output)
    
    # Display the resulting frame
    #cv2.imshow('frame',face_img)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
