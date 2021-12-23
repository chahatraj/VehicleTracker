import ultrasonic)
import accelerometer
import camera
import time
import gsm

velocity,speed = ultrasonic.ultrasonic()
if(speed>40):
	print ‘Rule Break : Out of speed’

x,y,z=accelerometer. accelerometer()
str=time.time() + ‘.jpg’
no_plate=camera.camera(str)
gsm.gsm(no_plate)
opt=input( ‘Do you want to search a particular vehicle? : (y/n)’)
if opt==’y’ :
	no_plate_check=input(‘Enter vehicle no : ’)
	if no_plate==no_plate_check :
		print ‘Found at time ’ + str – ‘.py’
	else : 
		print ‘Not found’