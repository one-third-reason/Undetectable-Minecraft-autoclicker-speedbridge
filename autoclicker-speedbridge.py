import time
import threading
import random
from pynput.mouse import Button
from pynput.mouse import Controller as mc
from pynput.keyboard import Key, GlobalHotKeys
from pynput.keyboard import Controller as kc

leftClickKey = "q"  # Key to activate autoclicker (left key)
rightClickKey = "x" # Key to activate autoclicker (right key)
bridgeKey = "z"     # Key to activate speedbridge bot

class Click(threading.Thread):
	def __init__(self):
		super(Click, self).__init__()
		self.mode = None

	def run(self):
		while True:
			while self.mode:
				mouse.click(self.mode)
				time.sleep(random.uniform(0.001,0.09)) # interval between clicks are 0.01 until 0.15 seconds
			time.sleep(0.001)

class Bridge(threading.Thread):
	def __init__(self):
		super(Bridge, self).__init__()
		self.running = False

	def run(self):
		while True:
			while self.running:
				keyboard.press(Key.shift)
				keyboard.press('s')
				time.sleep(0.2)
				keyboard.release('s')
				mouse.click(Button.right)
				time.sleep(0.01)
				keyboard.release(Key.shift)
				keyboard.press('s')
				time.sleep(0.18)
				keyboard.release('s')
			time.sleep(0.001)

mouse = mc()
keyboard = kc()
clickC = Click()
bridgeC = Bridge()
clickC.start()
bridgeC.start()

def activateLeftClick():
	clickC.mode = Button.left if clickC.mode != Button.left else None

def activateRightClick():
	clickC.mode = Button.right if clickC.mode != Button.right else None

def activateBridge():
	bridgeC.running = not bridgeC.running

with GlobalHotKeys({
	leftClickKey : activateLeftClick,
	rightClickKey : activateRightClick,
	bridgeKey : activateBridge
	}) as i:
	i.join()
