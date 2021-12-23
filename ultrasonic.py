import RPi.GPIO as GPIO
import time

def ultrasonic():
GPIO.setmode(GPIO.BCM)
trig=11
echo=13
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
samp=20
offset=0.0
SOS=34300
total_distance=0
average_distance=0
distance0=0
distance1=0
speed=0
total_speed=0
total_velocity=0
velocity=0
pulse_width=0
pulse_begin=0
pulse_end0=0
pulse_end1=0
distance_error=False
for x in range(0,samp):
		GPIO.output(trig,False)
		time.sleep(0.310)

GPIO.output(trig,True)
time.sleep(0.000015)
GPIO.output(trig, False)
pulse_end0=pulse_end1
while GPIO.input(echo)==0:
			pulse_begin=time.time()

while GPIO>input(echo)==1:
			pulse_end1=time.time()

pulse_width=pulse_end1-pulse_begin
print(‘Read’+str(x+1)+’/’+str(samp),str(round(pulse_width,9)))
distance1=pulse_width*SOS*0.5
total_distance += distance1
if distance1<2 or distance1>400 :
		distance_error=True

velocity=(distance1-distance0)/(pulse_end1-pulse_end0)
speed=abs(velocity)
ditance0=distance1
total_speed += speed
total_velocity += velocity

if distance_error :
		print ‘Range error: Range 2 – 400 cm’
else 
		print (‘cms/s: VEL:’ , int(total_velocity/samp), ‘Average Speed:’, int (total_speed/samp))

GPIO.cleanup()
print “Done”
return int(total_velocity/samp), int (total_speed/samp)
