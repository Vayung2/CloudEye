# CloudEye

CloudEye aims to be a system which can be used to automatically unlock a home door while notifying and giving additional control to the homeowner, even if they are far away in a different city. In this project, an ESP32Cam takes an image of a person at the door. The ESP32Cam sends the image in multipart/form-data file format as an HTTP POST Request to the AWS cloud server via TCP/IP packets. A Flask Server, hosted on an AWS EC2 Instance, receives the image and stores it on the server in an S3 Bucket. The image is processed by an OpenCV algorithm in Flask, and the result is returned to the ESP32Cam, triggering a signal for a motor to open the door. An HTML result file is also rendered at the public server address. In the development process, an Apache server serviced by PHP Files were also used (although later removed), while Wireshark was a useful tool to debug HTTP POST Requests by analyzing raw TCP/IP Packets. The project also aimed to be incredibly cost-effective for the homeowner, with the only costs for the homeowner being the ESP32Cam (~$10 or ₹800) and small cloud service costs. 

Here is a sample of the images taken by the ESP32Cam:
<img width="771" alt="image" src="https://github.com/Vayung2/CloudEye/assets/112582191/f9651ce9-807f-47ba-8d18-cbe26a0020c1">

Here is a result coming to the ESP32 Terminal, after an image is taken by the ESP32Cam, sent to a Flask Server hosted on the Cloud, and returned after processing by an AI. 
<img width="687" alt="image" src="https://github.com/Vayung2/CloudEye/assets/112582191/33583611-8ef9-4a5f-9b1e-1895cba0f846">

