import cv2
import time

SLICES = 3

def detect(cascades, test_image, scaleFactor = 1.2):
    #convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
    height, width, depth = test_image.shape
    segment_width = int(width/3)

    #find the bounding boxes for each classifier in the cascades list
    all_boxes = []
    for idx,cascade in enumerate(cascades):
        rects = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=5)
        all_boxes.extend(rects)

    #initialize output list
    output=[0] * SLICES
    
    #check the position (left,mid,right) for every detected bounding box
    for box in all_boxes:
        x1,y1,x2,y2 = box
        center_x = int(x1+(x2/2))
        segment = center_x//segment_width
        output[segment]+=1
    return output


def start(myAWSIoTMQTTClient, run_event):
    cap = cv2.VideoCapture(0)

    #define classifiers 
    haar_cascade_face = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
    #haar_cascade_upperbody = cv2.CascadeClassifier('D:/Anaconda3/envs/py36/Library/etc/haarcascades/haarcascade_frontalface_alt.xml')
    #haar_cascade_fullbody = cv2.CascadeClassifier('D:/Anaconda3/envs/py36/Library/etc/haarcascades/haarcascade_profileface.xml')

    #store classifiers in list
    cascades = [haar_cascade_face]   #, haar_cascade_upperbody,haar_cascade_fullbody]

    i = 0
    buffer = []
    #get a camera frame, analyse it and print the cumulative position of detected faces in the last 5 frames
    while(True):
        
        if run_event.is_set():
            break
    
        #time between frame capture
        time.sleep(0.4)
        i += 1
        #calculate a result every 5 frames
        if i%5 == 0:
            result = [0] * SLICES
            for single_frame_result in buffer:
               result = [sum(x) for x in zip(result, single_frame_result)]
            buffer = []
            
            
            #return (print, post) result
            list_string = f"{result}"
            message = '{"sides": %s}' % list_string 
            if myAWSIoTMQTTClient.publish("camera", message, 0):
                print(" <- camera: %s" % message)
            else:
                print("!!!  Error camera -> AWS IoT")
            #print(result)


        # Capture frame-by-frame
        ret, frame = cap.read()
        #get frame information and append it to buffer
        output = detect(cascades,  cv2.flip( frame, 1 ))
        buffer.append(output)
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
        
