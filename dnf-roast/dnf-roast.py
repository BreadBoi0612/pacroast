#!/usr/bin/env python3
import sys
import subprocess
import random
import configparser
from pathlib import Path

# -----------------------------
# Fedora Roast Wrapper: dnf-roast
# -----------------------------
# Loads roasts from roasts.txt and maps pacman-like flags to DNF commands.
# Includes Fedora and Atomic Workstation humor.
# -----------------------------

# Load roasts from file
CONFIG_PATH = Path(__file__).parent / "roasts.txt"
config = configparser.ConfigParser()
config.optionxform = str  # keep case
config.read(CONFIG_PATH)

def pick_roast(category, pkg=None):
    """Pick a random roast from a given category, optionally formatting with package name."""
    if category not in config:
        category = "general"
    roasts = [v for k, v in config[category].items()]
    roast = random.choice(roasts)
    if pkg:
        roast = roast.format(pkg)
    return roast

def map_args_to_dnf(args):
    """Map pacman-like arguments to actual DNF commands and return the command + roast category."""
    joined = " ".join(args)
    dnf_args = []

    # --- Update whole system ---
    if "-Syu" in joined or "--sync --refresh --sysupgrade" in joined:
        dnf_args = ["sudo", "dnf", "upgrade", "--refresh"]
        return dnf_args, "update"

    # --- Install packages ---
    if "-S" in joined or "--sync" in joined:
        pkgs = [a for a in args if not a.startswith('-')]
        if not pkgs:
            pkgs = ["something"]
        dnf_args = ["sudo", "dnf", "install"] + pkgs
        return dnf_args, "install"

    # --- Remove packages ---
    if "-R" in joined or "--remove" in joined:
        pkgs = [a for a in args if not a.startswith('-')]
        if not pkgs:
            pkgs = ["something"]
        dnf_args = ["sudo", "dnf", "remove"] + pkgs
        return dnf_args, "remove"

    # --- Query installed packages ---
    if "-Q" in joined or "--query" in joined:
        pkgs = [a for a in args if not a.startswith('-')]
        dnf_args = ["dnf", "list", "installed"] + pkgs
        return dnf_args, "query"

    # --- Search packages ---
    if "-Ss" in joined or "--search" in joined:
        pkgs = [a for a in args if not a.startswith('-')]
        if not pkgs:
            pkgs = ["something"]
        dnf_args = ["dnf", "search"] + pkgs
        return dnf_args, "search"

    # --- Clean cache ---
    if "-Sc" in joined or "-Scc" in joined or "--clean" in joined:
        dnf_args = ["sudo", "dnf", "clean", "all"]
        return dnf_args, "clean"

    # --- Fallback general ---
    dnf_args = ["sudo", "dnf"] + args
    return dnf_args, "general"

def main():
    if len(sys.argv) < 2:
        print("Usage: dnf-roast <dnf flags> [packages...]")
        sys.exit(1)

    args = sys.argv[1:]
    pkgs = [a for a in args if not a.startswith('-')]

    # Map to DNF command & roast category
    dnf_args, category = map_args_to_dnf(args)

    # Print roast(s)
    if pkgs:
        for pkg in pkgs:
            print(pick_roast(category, pkg))
    else:
        print(pick_roast(category))

    # Run DNF
    try:
        subprocess.run(dnf_args)
    except KeyboardInterrupt:
        print("Operation cancelled by user.")

if __name__ == "__main__":
    main()
