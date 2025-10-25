#!/usr/bin/env python3
import sys
import subprocess
import random

ROASTS = [
    "Skipped updates again? Bold move, buddy.",
    "Your system is older than your last haircut.",
    "Installing {}… wow, really living on the edge.",
    "Really installing {}? Epic choice.",
    "Your RAM says hi.",
    "Warning: package may judge your life choices.",
    "You’ve run pacman more than you’ve run in a week.",
    "Your system is a museum exhibit."
]

def pick_roast(pkg=None):
    roast = random.choice(ROASTS)
    if '{}' in roast and pkg:
        return roast.format(pkg)
    return roast

def main():
    if len(sys.argv) < 2:
        print("Usage: pacroast <pacman flags> [packages...]")
        sys.exit(1)

    args = sys.argv[1:]
    pkgs = [arg for arg in args if not arg.startswith('-')]

    for pkg in pkgs:
        print(pick_roast(pkg))

    try:
        subprocess.run(['sudo', 'pacman'] + args)
    except KeyboardInterrupt:
        print("Operation cancelled by user.")

if __name__ == '__main__':
    main()
