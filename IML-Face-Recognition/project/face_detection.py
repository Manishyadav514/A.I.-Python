import numpy as np
import cv2
import pickle

detector = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt2.xml')
recogniser = cv2.face.LBPHFaceRecognizer_create()
recogniser.read("./data/face_trainer.yml")

labels = {"username": 1}

with open("data/face_labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v: k for k, v in og_labels.items()}
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        boxed_gray = gray[y:y + h, x:x + w]
        boxed_color = frame[y:y + h, x:x + w]
        id, conf = recogniser.predict(boxed_gray)
        #higher the confidence, lower the accuracy. For instance, confidence of 100 is better than 200
        #a confidence of 0 is a perfect match
        #confidence increase as we get close to the camera
        if conf <= 100:
            name = labels[id]
            conf = "{} ".format(round(conf))   #probability of the match in percentage
            name = str(conf) + str(name)
            # puts text around the detected face
            cv2.putText(frame, name, (x - 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        else:
            cv2.putText(frame, "Unknown", (x + 5, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
