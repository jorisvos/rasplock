import bluetooth
import os, sys, signal, subprocess

import variables.colors as c
import variables.device as d

from sense_hat import SenseHat
from time import sleep
from libs.pixels import *
from libs.message import *

unlocked = False
tempDebug = False

sense = SenseHat()
sense.clear()

# Classes ------------------
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Functions ----------------
def clear():
	sense.clear()

def exit(signal, frame):
	mode_index = 0
	clear()
	print(bcolors.OKGREEN+"Bye!"+bcolors.ENDC)
	sys.exit(0)

# Main program -------------
if __name__ == '__main__':
    if tempDebug:
        print("Colors:")
        print(bcolors.HEADER + "Header" + bcolors.ENDC)
        print(bcolors.OKBLUE + "OKBlue" + bcolors.ENDC)
        print(bcolors.OKGREEN + "OKGreen" + bcolors.ENDC)
        print(bcolors.WARNING + "Warning" + bcolors.ENDC)
        print(bcolors.ERROR + "Error" + bcolors.ENDC)
        print(bcolors.BOLD + "Bold" + bcolors.ENDC)
        print(bcolors.UNDERLINE + "Underline" + bcolors.ENDC)

    signal.signal(signal.SIGINT, exit)
    while True:
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        print("found %d devices" % len(nearby_devices))

        for addr, name in nearby_devices:
            print("  %s - %s" % (addr, name))

        if len(nearby_devices) < 1:
            if unlocked:
                unlocked = False
                showMessage("Locked!", background_color=c.lightcyan, foreground_color=c.red, speed=0.10)
                setLocked()
            else:
                setLocked()
        else:
            foundDevice = False
            for addr, name in nearby_devices:
                if addr == d.deviceMacA and name == d.deviceName:
                    foundDevice = True
                    break
            if foundDevice:
                if unlocked:
                    setUnlocked()
                else:
                    unlocked = True
                    showMessage("Unlocked! "+name, background_color=c.lightcyan, foreground_color=c.green, speed=0.10)
                    setUnlocked()
            else:
                if unlocked:
                    unlocked = False
                    showMessage("Locked!", background_color=c.lightcyan, foreground_color=c.red, speed=0.10)
                    setLocked()
                else:
                    setLocked()
        sleep(0.05)



nearby_devices = bluetooth.discover_devices(duration=4, lookup_names=True, flush_cache=True, lookup_class=False)
