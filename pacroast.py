#!/usr/bin/env python3
import sys
import subprocess
import random

# Roast pools by category
GENERAL_ROASTS = [
    "Your system is older than your last haircut.",
    "Your RAM says hi.",
    "Warning: package may judge your life choices.",
    "You’ve run pacman more than you’ve run in a week.",
    "Your system is a museum exhibit."
]

INSTALL_ROASTS = [
    "Installing {}… wow, really living on the edge.",
    "Really installing {}? Epic choice."
]

UPDATE_ROAST = "Skipped updates again? Bold move, buddy."

REMOVE_ROASTS = [
    "Farewell, {}. You won’t be missed.",
    "Deleting {}? Brutal.",
    "Uninstalling {} — as you should."
]

def pick_roast(args, pkg=None):
    joined = " ".join(args)

    if "-Syu" in joined:
        return UPDATE_ROAST
    elif "-S" in joined and not "-Syu" in joined:
        return random.choice(INSTALL_ROASTS).format(pkg or "")
    elif "-R" in joined:
        return random.choice(REMOVE_ROASTS).format(pkg or "")
    else:
        roast = random.choice(GENERAL_ROASTS)
        return roast.format(pkg or "")

def main():
    if len(sys.argv) < 2:
        print("Usage: pacroast <pacman flags> [packages...]")
        sys.exit(1)

    args = sys.argv[1:]
    pkgs = [arg for arg in args if not arg.startswith('-')]

    # Context-aware roast printing
    if "-Syu" in args:
        print(pick_roast(args))
    elif pkgs:
        for pkg in pkgs:
            print(pick_roast(args, pkg))
    else:
        print(pick_roast(args))

    # Run the actual pacman command
    try:
        subprocess.run(["sudo", "pacman"] + args)
    except KeyboardInterrupt:
        print("Operation cancelled by user.")

if __name__ == "__main__":
    main()
