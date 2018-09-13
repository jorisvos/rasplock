import variables.colors as c

def color_debug():
    print("Colors:")
    print(c.bcolors.HEADER + "Header" + c.bcolors.ENDC)
    print(c.bcolors.OKBLUE + "OKBlue" + c.bcolors.ENDC)
    print(c.bcolors.OKGREEN + "OKGreen" + c.bcolors.ENDC)
    print(c.bcolors.WARNING + "Warning" + c.bcolors.ENDC)
    print(c.bcolors.ERROR + "Error" + c.bcolors.ENDC)
    print(c.bcolors.BOLD + "Bold" + c.bcolors.ENDC)
    print(c.bcolors.UNDERLINE + "Underline" + c.bcolors.ENDC)
