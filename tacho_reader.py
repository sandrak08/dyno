import RPi.GPIO as GPIO


class reader:
	def __init__(self, hallpin):
		# specify broadcom chip-specific pin numbering system
		GPIO.setmode(GPIO.BCM)
		
		self.hallpin = hallpin
		
		
if __name__ == "__main__":
	# initialize general purpose input and output pins
	
	# intialize interrupt for digital edge detection
		# provided a callback function that will count the pulses
			# increment pulse
			# calculate elapsed time (sec)
			# refresh current time (sec)
			
	# loop until keyboard interrupt
		# calculate speed (mph) given radius (mm)
			# calculate frequency (rps): 1 / elapsed time
			# calculate circumference (mm): 2 * pi * radius
			# scale frequency unit (rph): rps * (60 s/m) * (60 m/h)
			# scale circumference unit (mile): mm * 1.609 * 10**6
			# return circumference * frequency
	
		# display content
	pass
	
	
