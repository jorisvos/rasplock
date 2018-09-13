import variables.vars as v

from libs.lock import *
from libs.clear import *

def joystick_move_middle(event):
    if event.action == "pressed":
        if v.enabled:
            v.enabled = False
            clear()
        else:
            v.enabled = True
            lock(False)


        print("enabled="+str(v.enabled))
