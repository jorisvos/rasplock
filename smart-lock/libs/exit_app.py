import variables.colors as c

from libs.clear import *

def exit(signal, frame):
    clear()
	print(c.bcolors.OKGREEN+"Bye!"+c.bcolors.ENDC)
	sys.exit(0)
