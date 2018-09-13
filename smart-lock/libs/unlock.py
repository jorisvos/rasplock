from sense_hat import SenseHat

from libs.message import *

import variables.colors as c

sense = SenseHat()
sense.clear()

def unlock(device_name):
    show_message("Unlocked! "+device_name, background_color=c.lightcyan, foreground_color=c.green, speed=0.05)
    sense.set_pixels(c.unlocked)
