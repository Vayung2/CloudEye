import cv2
import face_recognition

#Reads in the Input Image (here, an unconfirmed picture of Messi)
img = cv2.imread("Messi1.webp")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

#Reads in the Image being compared to (here, a confirmed picture of Messi)
img2 = cv2.imread("images/Messi.webp")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

#Calculates and displays whether the two images are the same or not
result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Result: ", result)

#Shows both the images which were being compared side by side
cv2.imshow("Img", img)
cv2.imshow("Img 2", img2)
cv2.waitKey(0)
