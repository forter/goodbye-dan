# pip install pyfiglet termcolor

__author__ = "synhershko"

import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('Goodbye Dan!!', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
