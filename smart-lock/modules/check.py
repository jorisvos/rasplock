from modules.find_device import *
from modules.check_device import *

from libs.lock import *
from libs.unlock import *

import variables.vars as v
import variables.device as d

def check():
    nearby_devices = find_device()

    if len(nearby_devices) < 1:
        if v.unlocked:
            v.unlocked = False
            lock(True)
    else:
        found_device = check_device(nearby_devices)
        if found_device and v.unlocked == False:
            v.unlocked = True
            unlock(d.deviceName)
        elif found_device and v.unlocked:
            v.unlocked = True
        else:
            if v.unlocked:
                lock(True)
                v.unlocked = False
