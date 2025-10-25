#!/usr/bin/env python3
import sys
import subprocess
import random

# --- Roast Categories ---

HELP_ROASTS = [
    "Needing help already? Arch btw.",
    "Reading the help menu? Thought you were elite.",
    "Using -h? Just guess the flags like everyone else.",
    "You asked for help? That's not very Arch of you."
]

INSTALL_ROASTS = [
    "Installing {}… wow, really living on the edge.",
    "Really installing {}? Epic choice.",
    "{} is about to bloat your system — congrats!"
]

UPDATE_SYSTEM_ROAST = "Skipped updates again? Bold move, buddy."
UPDATE_APPS_ROASTS = [
    "Updating {}? Keeping things fresh, huh?",
    "Bringing {} up to date? Look at you being responsible.",
    "{} gets a facelift today. Nice."
]

REMOVE_ROASTS = [
    "Farewell, {}. You won’t be missed.",
    "Deleting {}? Brutal.",
    "Uninstalling {} — as you should.",
    "Another one bites the dust: {}."
]

QUERY_ROASTS = [
    "Querying packages again? Still not sure what you installed?",
    "Running -Q like a detective.",
    "Investigating your own mess, huh?",
    "Pacman -Q: because curiosity kills the cat."
]

SEARCH_ROASTS = [
    "Looking for {}? It's probably already installed.",
    "Searching for {}… you sure you need it?",
    "{}? Really? That’s your choice?"
]

FILES_ROASTS = [
    "Checking files with -F? Just admit you broke something.",
    "Hoping -F will save your system? Cute.",
    "Using -F like you know what you're doing."
]

DATABASE_ROASTS = [
    "Messing with the database, huh? Dangerous game.",
    "Pacman -D? The Arch gods are watching.",
    "Tinkering with databases — what could go wrong?"
]

CLEANUP_ROASTS = [
    "Running -Sc to clean up? Minimalism looks good on you.",
    "Trying to free space? Maybe delete your ego next.",
    "Finally cleaning your cache, huh? Took you long enough."
]

SYNC_ROASTS = [
    "Syncing repositories… trying to look busy, I see.",
    "Pacman -Sy: pulling the latest chaos.",
    "You’re syncing? Brace yourself for the upgrades."
]

GENERAL_ROASTS = [
    "Your system is older than your last haircut.",
    "Your RAM says hi.",
    "Warning: package may judge your life choices.",
    "You’ve run pacman more than you’ve run in a week.",
    "Your system is a museum exhibit."
]


def pick_roast(args, pkg=None):
    joined = " ".join(args)

    # --- Specific > General order ---
    if "-h" in args or "--help" in args:
        return random.choice(HELP_ROASTS)

    if any(flag in joined for flag in ["-Syu", "--sync --refresh --sysupgrade"]):
        if any(not a.startswith('-') for a in args):
            pkg = next((a for a in args if not a.startswith('-')), None)
            return random.choice(UPDATE_APPS_ROASTS).format(pkg or "something")
        return UPDATE_SYSTEM_ROAST

    if any(flag in joined for flag in ["-Si", "-Ss", "--info", "--search"]):
        pkg = next((a for a in args if not a.startswith('-')), "something")
        return random.choice(SEARCH_ROASTS).format(pkg)

    if any(flag in joined for flag in ["-Sc", "-Scc", "--clean"]):
        return random.choice(CLEANUP_ROASTS)

    if any(flag in joined for flag in ["-Sy", "--refresh"]) and "-Syu" not in joined:
        return random.choice(SYNC_ROASTS)

    if "-F" in joined or "--files" in joined:
        return random.choice(FILES_ROASTS)

    if "-D" in joined or "--database" in joined:
        return random.choice(DATABASE_ROASTS)

    if "-R" in joined or "--remove" in joined:
        pkg = next((a for a in args if not a.startswith('-')), "something")
        return random.choice(REMOVE_ROASTS).format(pkg)

    if "-Q" in joined or "--query" in joined:
        return random.choice(QUERY_ROASTS)

    if "-S" in joined or "--sync" in joined:
        pkg = next((a for a in args if not a.startswith('-')), "something")
        return random.choice(INSTALL_ROASTS).format(pkg)

    return random.choice(GENERAL_ROASTS)


def main():
    if len(sys.argv) < 2:
        print("Usage: pacroast <pacman flags> [packages...]")
        sys.exit(1)

    args = sys.argv[1:]
    pkgs = [a for a in args if not a.startswith('-')]

    # Print roast(s)
    if pkgs:
        for pkg in pkgs:
            print(pick_roast(args, pkg))
    else:
        print(pick_roast(args))

    # Run pacman
    try:
        subprocess.run(["sudo", "pacman"] + args)
    except KeyboardInterrupt:
        print("Operation cancelled by user.")


if __name__ == "__main__":
    main()
