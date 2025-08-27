import sys
import time

class SlowPrinter:
    def __init__(self, delay=0.03):
        self.delay = delay

    def print(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(self.delay)
        print()