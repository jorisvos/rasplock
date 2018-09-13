from sense_hat import SenseHat

from libs.message import *

import variables.colors as c

sense = SenseHat()
sense.clear()

def lock(useText):
    if useText:
        show_message("Locked!", background_color=c.lightcyan, foreground_color=c.red, speed=0.05)
    sense.set_pixels(c.locked)
