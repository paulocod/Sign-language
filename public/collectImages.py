import cv2
import os
import time
import uuid

IMAGES_PATH = '../RealTimeObjectDetection/Tensorflow/workspace/images/collectedimages'

labels = ['olá', 'obrigado', 'sim', 'não', 'casa']
number_imgs = 15

for label in labels:
    folder = os.path.join(IMAGES_PATH, label)
    os.makedirs(folder, exist_ok=True)

    cap = cv2.VideoCapture(0)
    print('Coletando imagens de {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()