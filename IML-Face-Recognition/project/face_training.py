import os
import pickle
import cv2
import numpy as np
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")
detector = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
#LBPH (Local Binary Pattern Histogram) is a Face-Recognition algorithm it is used to recognize the face of a person.
# It is known for its performance and how it is able to recognize the face of a person from both front face and side face
recogniser = cv2.face.LBPHFaceRecognizer_create()
# recognizer = cv2.face.createEigenFaceRecognizer()
# recognizer = cv2.face.createFisherFaceRecognizer()
current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(IMAGE_DIR):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()
            # Store the name in dictionary if user doesn't exist.
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id = label_ids[label]
            pil_image = Image.open(path).convert("L")  # Coverts Image into Grayscale
            size = (550, 550)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(final_image, "uint8")   # Convert Image into Numpy Array
            # 'detectMultiscale()' function detects the faces in frame.
            faces = detector.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
            for (x, y, w, h) in faces:
                boxed = image_array[y:y + h, x:x + w]     # Detected Face
                x_train.append(boxed)
                y_labels.append(id)

#writing in binary
with open("data/face_labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)
print(label_ids)
#print(x_train, np.array(y_labels))

recogniser.train(x_train, np.array(y_labels))
# Save the model as trainer.yml
recogniser.write('data/face_trainer.yml')
