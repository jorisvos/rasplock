import os, sys, signal, subprocess

from sense_hat import SenseHat
from time import sleep

from libs.clear import *

from modules.joystick import *
from modules.check import *

import variables.vars as v

sense = SenseHat()
sense.clear()

# Function -----------------
def exit(signal, frame):
    clear()
    print(c.bcolors.OKGREEN+"Bye!"+c.bcolors.ENDC)
    sys.exit(0)

# Main program -------------
if __name__ == '__main__':
    sense.stick.direction_middle = joystick_move_middle
    signal.signal(signal.SIGINT, exit)

    print("initialized")

    while True:
        if v.enabled:
            check()
        sleep(0.05)

# nearby_devices = bluetooth.discover_devices(duration=4, lookup_names=True, flush_cache=True, lookup_class=False)
