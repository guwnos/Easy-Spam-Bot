from pynput.keyboard import Key, Controller
import time

Keyboard = Controller()

time.sleep(3)
for x in range(10): # Change 10 to amount messages to spam
    for i in "Dupa": # Change Dupa for your message # Or if you want delete this line of code and change Keyboard.press(i) to Keyboard.type("message")
        Keyboard.press(i)
        Keyboard.press(Key.enter)
