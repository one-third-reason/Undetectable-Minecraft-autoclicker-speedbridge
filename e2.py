import time
import threading
import random
from pynput.mouse import Button
from pynput.mouse import Controller as mc
from pynput.keyboard import Key, GlobalHotKeys
from pynput.keyboard import Controller as kc

class Click(threading.Thread):
	def __init__(self):
		super(Click, self).__init__()
		self.running = False

	def run(self):
		while True:
			while self.running:
				mouse.click(Button.left)
				time.sleep(random.uniform(0.01,0.15))
			time.sleep(0.1)

class Bridge(threading.Thread):
	def __init__(self):
		super(Bridge, self).__init__()
		self.running = False

	def run(self):
		while True:
			while self.running:
				keyboard.press(Key.ctrl)
				keyboard.press('s')
				time.sleep(0.25)
				keyboard.release('s')
				mouse.click(Button.right)
				time.sleep(random.uniform(0.01, 0.1))
				keyboard.release(Key.ctrl)
				keyboard.press('s')
				time.sleep(0.2)
				keyboard.release('s')
			time.sleep(0.1)

mouse = mc()
keyboard = kc()
clickFunc = Click()
bridgeFunc = Bridge()
clickFunc.start()
bridgeFunc.start()

def activateClick():
	print("clicked")
	if clickFunc.running:
		clickFunc.running = False
	else:
		clickFunc.running = True

def activateBridge():
	print("bridged")
	if bridgeFunc.running:
		bridgeFunc.running = False
	else:
		time.sleep(0.2)
		bridgeFunc.running = True

with GlobalHotKeys({
	'q' : activateClick,
	'v' : activateBridge,
	}) as i:
	i.join()