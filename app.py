#Import the necessary modules:
from flask import Flask, request, render_template
import cv2
import face_recognition
import  numpy as np

#Initialize the Flask app:
app = Flask(__name__)

#Create a route for file uploading:
@app.route('/process_image', methods=['POST'])
def process_image():
    print("Received POST request:")
    #print("Headers:", request.headers)
    #print("Files:", request.files)
    #print("Raw Request Data:", request.data)

     # Get the uploaded image from the request
    photo = request.files['imageFile']
    photo.save('uploaded_photo.jpg')

    #Reads in the Input Image (here, an unconfirmed picture of test user)
    img = cv2.imread("uploaded_photo.jpg")
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_encoding = face_recognition.face_encodings(rgb_img)[0]

    #Reads in the Image being compared to (here, a confirmed picture of test user)
    img2 = cv2.imread("images/Vayun Gupta.jpg")
    rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

    #Calculates and displays whether the two images are the same or not
    result = face_recognition.compare_faces([img_encoding], img_encoding2)
    print("Result: ", result)
    return render_template('result.html', result=result)

#Create a route to render the HTML form:
@app.route('/', methods=['GET'])
def render_upload_form():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='172.20.10.3', port=5000)