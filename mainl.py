import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

IN1 = 23 #real pin 16
IN2 = 24 #real pin 18
ENA = 12 #real pin 32

IN3 = 17 #real pin 11
IN4 = 27 #real pin 13
ENB = 13 #real pin 33

GPIO.setup([IN1,IN2,ENA,IN3,IN4,ENB],GPIO.OUT)

pwmA = GPIO.PWM(ENA,1000)
pwmB = GPIO.PWM(ENB,1000)

pwmA.start(0)
pwmB.start(0)

def forward(speed=70):
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)
    
    pwmA.ChangeDutyCycle(speed)
    pwmB.ChangeDutyCycle(speed)
    
def backward(speed = 70):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    
    pwmA.ChangeDutyCycle(speed)
    pwmB.ChangeDutyCycle(speed)
    
def turn_right_smooth(speed=70, smoothness=30):
    """
    speed: Speed of the outer wheel (0-100)
    smoothness: Speed of the inner wheel (0-100). 
    Higher smoothness = wider, gentler turn.
    """
    GPIO.output(IN1, GPIO.HIGH) # Left Forward
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH) # Right Forward
    GPIO.output(IN4, GPIO.LOW)
    
    pwmA.ChangeDutyCycle(speed)      # Left goes fast
    pwmB.ChangeDutyCycle(smoothness) # Right goes slow

def turn_left_smooth(speed=70, smoothness=30):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    
    pwmA.ChangeDutyCycle(smoothness) # Left goes slow
    pwmB.ChangeDutyCycle(speed)      # Right goes fast
    
def sharp_turn_right(speed = 80):
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)
    
    pwmA.ChangeDutyCycle(speed) #left motor speed
    pwmB.ChangeDutyCycle(speed) #right motor speed
    

    
def sharp_turn_left(speed=80):
    # Left motor backward
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    # Right motor forward
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    
    pwmA.ChangeDutyCycle(speed)
    pwmB.ChangeDutyCycle(speed)
    


    
def stop():
    GPIO.output([IN1,IN2,IN3,IN4], GPIO.LOW)
    pwmA.ChangeDutyCycle(0)
    pwmB.ChangeDutyCycle(0)

    

try:

    #move forward
    print("Forward")
    forward(70)
    sleep(1)
    stop()

    #move backward
    print("Backward")
    turn_right_smooth(70)
    sleep(1)
    stop()



finally:
    stop()         # make sure motors are off
    pwmA.stop()
    pwmB.stop()
    GPIO.cleanup()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
