import sys


class Colors:
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    ENDC = "\033[0m"


def printc(color, message):
    print(color + message + Colors.ENDC)


# color which we print or import
printc(Colors.CYAN, sys.argv[1])
printc(Colors.GREEN, sys.argv[1])
printc(Colors.YELLOW, sys.argv[1])
printc(Colors.BLUE, sys.argv[1])
printc(Colors.RED, sys.argv[1])
