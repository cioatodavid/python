from termcolor import cprint
from pyfiglet import figlet_format
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) 


cprint(figlet_format('DAVID', font='slant'),
       'cyan')
