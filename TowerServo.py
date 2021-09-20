import time
import RPi.GPIO as GPIO
import cv2

servo = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo,GPIO.OUT)

p = GPIO.PWM(servo,50)

p.start(0)

def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo, True)
    p.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo, False)
    p.ChangeDutyCycle(0)

#def ServoRotate():

def image(direc,value):
    #480p : 854x640
    #720p : 1280x720
    #1080p : 1920x1080
    kamera=cv2.VideoCapture(0) 
    kamera.set(3,1280)
    kamera.set(4,720)
    ret,kare=kamera.read()
    cv2.imwrite("images/"+direc+"/im"+value+".jpg",kare)

def ServoRotate(director,value):
    print("Servo - 145 Derece")
    SetAngle(170)
    time.sleep(1)
    image(director,"-"+value+"-1-")
    
    time.sleep(1)
    print("Servo - 120 Derece")
    SetAngle(135)
    time.sleep(1)
    image(director,"-"+value+"-2-")
    
    time.sleep(1)
    print("Servo - 95 Derece")
    SetAngle(100)
    time.sleep(1)
    image(director,"-"+value+"-3-")
    
    time.sleep(1)
    print("Servo - 70 Derece")
    SetAngle(65)
    time.sleep(1)
    image(director,"-"+value+"-4-")
    
    time.sleep(1)
    print("Servo - 45 Derece")
    SetAngle(30)
    time.sleep(1)
    image(director,"-"+value+"-5-")
    
    time.sleep(1)
    print("Servo - 20 Derece")
    SetAngle(10)
    time.sleep(1)
    image(director,"-"+value+"-6-")
    
    time.sleep(1)

#SetAngle(100)
# 170
# 135
# 100
# 65
# 30
# 10
#ServoRotate(1)

#GPIO.cleanup()
#150 peek

#90 deep
