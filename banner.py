from pyfiglet import Figlet
from colorama import Fore


def banner():
    """This is my function to print my banner using pyfiglet library"""
    custom_fig = Figlet(font="slant")
    logo = custom_fig.renderText("ESCAPE THE CAVE")
    print(Fore.BLUE + logo + Fore.RESET)
