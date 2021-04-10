import pyzbar.pyzbar as pyzbar
import cv2
import numpy 
def scan():
    i=0;
    cap = cv2.VideoCapture(0)# to capture the qr form the video
    while i <1:
        _,frame = cap.read() # open camera in frame
        decoded = pyzbar.decode(frame)
        for obj in decoded:
            print(obj.data)
            str1 = obj.data
            i+=1
        cv2.imshow("QRCode",frame)
        cv2.waitKey(5)
        cv2.destroyAllWindows
    return str1
value = scan()
# program ended below is the additional program 
print(type(value)) #to see the type 
data = value.decode('UTF-8') # To convert Byte to string 
print(type(data))
s=data.split(' ') # To convert  string to list 
print(s)
for j in s:
    print(j)
