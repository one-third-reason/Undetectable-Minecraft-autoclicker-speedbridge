import time
import threading
import random
from pynput.mouse import Button
from pynput.mouse import Controller as mc
from pynput.keyboard import Key, GlobalHotKeys
from pynput.keyboard import Controller as kc

clickKey = "q"  # Key to activate autoclicker
bridgeKey = "z" # Key to activate speedbridge bot

class Click(threading.Thread):
	def __init__(self):
		super(Click, self).__init__()
		self.running = False

	def run(self):
		while True:
			while self.running:
				mouse.click(Button.left)
				time.sleep(random.uniform(0.01,0.15)) # interval between clicks are 0.01 until 0.15 seconds
			time.sleep(0.1)

class Bridge(threading.Thread):
	def __init__(self):
		super(Bridge, self).__init__()
		self.running = False

	def run(self):
		while True:
			while self.running:
				keyboard.press(Key.shift)
				keyboard.press('s')
				time.sleep(0.3)
				keyboard.release('s')
				mouse.click(Button.right)
				time.sleep(random.uniform(0.01, 0.1)) # interval between placing block and uncrouching are 0.01 until 0.1 seconds, which is pretty useless
				keyboard.release(Key.shift)
				keyboard.press('s')
				time.sleep(0.18)
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
	clickKey : activateClick,
	bridgeKey : activateBridge,
	}) as i:
	i.join()
