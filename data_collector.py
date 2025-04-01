import os
import cv2
import time
import uuid

IMAGE_PATH = "CollectedImages"

labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number_of_images =  35

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path)

    #open camera 
    cap = cv2.VideoCapture(0)
    print(f"Collecting images for {label}")
    time.sleep(3)

    for imgnum in range(number_of_images):
        ret,frame = cap.read()
        imagename=os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    
    cap.release()