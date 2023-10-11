#!/usr/bin/env python3
import interface
import signal
from sys import exit

def ctrlc(sig, frame):
    exit(0)
if __name__ == "__main__":
    signal.signal(signal.SIGINT, ctrlc)
    interface.run()
