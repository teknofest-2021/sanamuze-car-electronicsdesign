import RPi.GPIO as GPIO
import time
import TowerServo

Pin1 = 7
Pin2 = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(Pin1,GPIO.OUT)
GPIO.setup(Pin2,GPIO.OUT)



def deggre(derece) :
    x = (derece*6.35)/360
    rotate()
    time.sleep(x)
   
def R_deggre(derece):
    x = (derece*6.35)/360
    R_rotate()
    time.sleep(x)
def rotate():
    GPIO.output(Pin1,GPIO.HIGH)
    GPIO.output(Pin2,GPIO.LOW)
def R_rotate():
    GPIO.output(Pin1,GPIO.LOW)
    GPIO.output(Pin2,GPIO.HIGH)
def stop():
    GPIO.output(Pin1,GPIO.LOW)
    GPIO.output(Pin2,GPIO.LOW)
def Full_Rotate(directory):
    time.sleep(5)
    print("1/10")
    R_deggre(1)
    stop()
    time.sleep(1)
    TowerServo.ServoRotate(directory,"a")
    print("2/10")
    R_deggre(40)
    stop()
    time.sleep(1)
    TowerServo.ServoRotate(directory,"b")
    print("3/10")
    R_deggre(40)
    
    stop()
    time.sleep(1)
    TowerServo.ServoRotate(directory,"c")
    print("4/10")
    R_deggre(40)
    
    stop()
    time.sleep(1)
    TowerServo.ServoRotate(directory,"d")
    print("5/10")
    R_deggre(40)
    
    stop()
    time.sleep(1)
    TowerServo.ServoRotate(directory,"e")
    print("6/10")
    R_deggre(40)
    
    stop()
    time.sleep(1)
    TowerServo.ServoRotate(directory,"f")
    print("7/10")
    R_deggre(40)
    
    stop()
    time.sleep(1)
    TowerServo.ServoRotate(directory,"g")
    print("8/10")
    R_deggre(40)
    
    stop()
    time.sleep(1)
    TowerServo.ServoRotate(directory,"h")
    print("9/10")
    R_deggre(40)
    
    stop()
    time.sleep(1)
    TowerServo.ServoRotate(directory,"ı")
    print("10/10")
    R_deggre(40)

    stop()
    time.sleep(1)
    print("Bağlangıç Dönüşü . -FİNİSH'")
    deggre(360)
    
    stop()
    time.sleep(1)


#deggre(40)
Full_Rotate("16")
#deggre(30)
#stop()
#time.sleep(1)

GPIO.cleanup()

