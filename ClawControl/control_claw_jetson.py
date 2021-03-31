import Jetson.GPIO as GPIO
import time

enA = 12        # Physical pin 32
in1 = 23        # Physical pin 16
in2 = 24        # Physical pin 18

low_speed = 25
med_speed = 50
hi_speed = 75

clamp = False       # True = clamping mode, False = opening mode
speed = 25
running = False

start_time = 0
stop_time  = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(enA, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)

pwm_sig = GPIO.PWM(enA, 1000)
pwm_sig.start(speed)

def run_motor():
    global running
    global start_time

    if not running:
        start_time = round(time.time() * 1000)
        running = True
    if clamp:
        print("ON, CLAMP")
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
    else:
        print("ON, RELEASE")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)

def stop_motor():
    global running
    global start_time
    global stop_time
    stop_time = round(time.time() * 1000)
    if running:
        run_time = stop_time - start_time
        print(f"OFF, RAN FOR {run_time} ms")
        running = False
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)

def configure_mode():
    global running
    if running:
        run_motor()

print("A: turn motor ON")
print("D: turn motor OFF")
print("M: toggle direction")
print("1: set speed LOW")
print("2: set speed MED")
print("3: set speed HI")
print("X: EXIT program")

while(1):
    key = input()
    if key == 'a':
        run_motor()        
    
    elif key == 'd':
        stop_motor()
    
    elif key == 'm':
        if clamp:
            print("SET MODE RELEASE")
            clamp = False
        else:
            print("SET MODE CLAMP")
            clamp = True
        configure_mode()
    
    elif key == '1':
        print("SET SPEED LOW")
        pwm_sig.ChangeDutyCycle(low_speed)
    
    elif key == '2':
        print("SET SPEED MED")
        pwm_sig.ChangeDutyCycle(med_speed)
    
    elif key == '3':
        print("SET SPEED HI")
        pwm_sig.ChangeDutyCycle(hi_speed)
    
    elif key == 'x':
        stop_motor()
        GPIO.cleanup()
        break
    
    else:
        print("INVALID ENTRY")
    
