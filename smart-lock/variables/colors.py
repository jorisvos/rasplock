white = (255,255,255)
blue = (0, 0, 255)
red = r = (255, 0, 0)
green = g = (0, 255, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
brown = (165, 42, 42)
grey = (190, 190, 190)
lightcyan = c = (0, 50, 50)

locked = [
    c, c, c, c, c, c, c, c,
    c, c, c, r, r, c, c, c,
    c, c, r, c, c, r, c, c,
    c, c, r, c, c, r, c, c,
    c, r, r, r, r, r, r, c,
    c, r, r, r, r, r, r, c,
    c, r, r, r, r, r, r, c,
    c, c, c, c, c, c, c, c
]

unlocked = [
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c,
    c, c, g, c, c, c, c, c,
    c, g, c, g, g, g, g, c,
    c, g, c, g, g, g, g, c,
    c, c, g, c, c, g, g, c,
    c, c, c, c, c, c, c, c,
    c, c, c, c, c, c, c, c
]

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
