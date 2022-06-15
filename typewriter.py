import sys
import time


def typewriter(message):
    '''Typewriter will help me to print my story letter by letter'''
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.05)
        else:
            time.sleep(0.5)


# typewriter("Typewriter will help me to print my story letter by letter")
