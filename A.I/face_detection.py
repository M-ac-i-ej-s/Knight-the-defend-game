import cv2
from cv2 import cvtColor

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#PHOTO

img = cv2.imread('james.jpg')

grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Clever Programmer Face Detector', img)

cv2.waitKey()

# VIDEO

# video = cv2.VideoCapture('piwnica.MOV')

# while True:

#     successful_frame_read, frame = video.read()

#     grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#     for (x,y,w,h) in face_coordinates:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#     cv2.imshow('Clever Programmer Face Detector', frame)

#     key = cv2.waitKey(1)

#     if key==81 or key==113:
#         break