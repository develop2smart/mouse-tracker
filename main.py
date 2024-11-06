import os
import time
import re
from pynput import mouse
from pynput.keyboard import Key, Listener
#f=open('maniac1.txt','a')
inc=1
#f.write('<mouse_new>\n')
from pynput import keyboard
def on_functionf8(key):
    if (key==keyboard.Key.f8):
        print('f8 is pressed')
key_listener = keyboard.Listener(on_release=on_functionf8)
key_listener.start()
def on_click(x, y, button, pressed):
    f=open('maniac1.txt','a')
    if button == mouse.Button.left:
        print ('Left')
        #f.write('left\n')
    if button == mouse.Button.right:
        key_listener.stop()
        print ('right')
        #f.write('right\n')
    if button == mouse.Button.middle:
        print ('middle')
        #f.write('middle\n')
with mouse.Listener(on_click=on_click) as listener:
    try:
        listener.join()
    except Exception as e:
        print('Done'.format(e.args[0]))