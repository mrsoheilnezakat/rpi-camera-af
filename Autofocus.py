import time
import cv2
from picamera2 import Picamera2
import RPi.GPIO as GPIO
import threading
import queue
import numpy
from collections import deque
from datetime import datetime

class FrameVarianceMonitor:
	def __init__(self, window_size):
		self.window_size = window_size
		self.variances = deque(maxlen=window_size)
		self.current_max = float('-inf')
	def add_variance(self, variance):
		if variance>11:
			self.variances.append(variance)
		if len(self.variances) == self.window_size:
			self.current_max = max(self.variances)
		else:
			if variance > self.current_max:
				self.current_max = variance
	def get_max_variance(self):
		return self.current_max
	def is_maximum_found(self):
		if len(self.variances) == self.window_size and self.current_max in self.variances:
			self.clear_variances()
			return True
		return False
	def clear_variances(self):
		self.variances.clear()
		self.current_max = float('-inf')

window_size = 30
monitor = FrameVarianceMonitor(window_size)

servo_pin = 11 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)
picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={"size": (480,360)})
size_tuple = video_config['main']['size']
size_str = str(size_tuple)
picam2.configure(video_config)
picam2.start()

def is_blurred(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	lap_var = cv2.Laplacian(gray, cv2.CV_64F).var()
	return int(lap_var)

rotate=True

def compare (a,b,tol=1e-15):
	if abs(a-b)<tol:
		return "equal"
	return "greater" if a>b else "less"

def rightmove():
	pwm.ChangeDutyCycle(12)
	time.sleep(0.02)
	pwm.ChangeDutyCycle(0)
	time.sleep(0.3)

def leftmove():
	pwm.ChangeDutyCycle(1)
	time.sleep(0.02)
	pwm.ChangeDutyCycle(0)
	time.sleep(0.3)

def frameshow(picam2):
	frame = picam2.capture_array()
	if frame is None:
		#print("Failed to capture image")
		return True
	frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
	cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
	cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	cv2.imshow('Frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		return False
	return True

def show():
	while True:
			if not frameshow(picam2):
				break

def takepic(x,y):
	now = datetime.now()
	filename = now.strftime("%Y%m%d_%H%M%S")
	metadata = picam2.capture_file(f"{filename}_variance_is_{x}_resolution_is_{y}.jpg")

def moarso():
	initial_var=is_blurred(picam2.capture_array())
	leftmove()
	second_var=is_blurred(picam2.capture_array())
	comp_res=compare(second_var,initial_var)
	# either use "rotate=False" or below if condition for better readability
	if comp_res=="greater" or comp_res=="equal":
		rotate=False #false means rotation direction is left
	else:
		rotate=True #true means rotation direction is right
	#print("initial_var",initial_var,"second_var",second_var)
	try:
		start_time = time.time()
		count=0
		while True:
			# monitor.add_variance(is_blurred(picam2.capture_array()))
			# if monitor.is_maximum_found():
				# current_max = monitor.get_max_variance()
				# #print(f"Maximum variance in the last {window_size} frames: {current_max}")
				# picvar=is_blurred(picam2.capture_array())
				# takepic(picvar)
				# realtimevar=picvar
				# while (picvar*0.9<=realtimevar<=picvar*1.1):
					# realtimevar=is_blurred(picam2.capture_array())
			if rotate==True:
				rightmove()
				initial_var=second_var
				second_var=is_blurred(picam2.capture_array())
				print("if rotate==True: , second_var: ",second_var,"     initial_var: ",initial_var)
				comp_res=compare(second_var,initial_var)
				if comp_res=="greater" or comp_res=="equal":
					rotate=True
				else:
					rotate=False
					count+=1
			if rotate==False:
				leftmove()
				initial_var=second_var
				second_var=is_blurred(picam2.capture_array())
				print("if rotate==False: , second_var: ",second_var,"    initial_var:",initial_var)
				comp_res=compare(second_var,initial_var)
				if comp_res=="greater" or comp_res=="equal":
					rotate=False
				else:
					rotate=True
					count+=1
			if count>5:
				picvar=is_blurred(picam2.capture_array())
				takepic(picvar,size_str)
				realtimevar=picvar
				count=0
				end_time = time.time()
				runtime = end_time - start_time
				print(f"The runtime of the code is {runtime} seconds.")
				print("change now")
				while (picvar*0.9<=realtimevar<=picvar*1.1):
					realtimevar=is_blurred(picam2.capture_array())
				time.sleep(5)
				start_time = time.time()
			#print(f"count is {count}")

	except KeyboardInterrupt:
		print("Interrupted by user.")
	
	finally:
		pwm.stop()
		GPIO.cleanup()
		picam2.stop()
		picam2.close()
		cv2.destroyAllWindows()

focuse_thread = threading.Thread(target=moarso)
frameshow_thread = threading.Thread(target=show)
focuse_thread.start()
frameshow_thread.start()