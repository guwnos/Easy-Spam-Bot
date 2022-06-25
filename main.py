from pynput.keyboard import Key, Controller
import time

Keyboard = Controller()

time.sleep(3)
for x in range(10): # Change 10 to amount messages to spam
    keyboard.type("Message to spam") # Change "Message to spam" to your message
    keyboard.press(key.enter)
