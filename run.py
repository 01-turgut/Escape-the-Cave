# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
from colorama import Fore, Back
from typewriter import typewriter
from banner import banner


banner()

start = input
time.sleep(3)
typewriter(Back.RED + Fore.WHITE + "...You were walking around and saw a cave...\n")

