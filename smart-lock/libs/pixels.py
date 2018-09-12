from sense_hat import SenseHat
import variables.colors as c

sense = SenseHat()
sense.clear()

def setLocked():
    sense.set_pixels(c.locked)
def setUnlocked():
    sense.set_pixels(c.unlocked)
