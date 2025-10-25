# PacRoast 😎

PacRoast is a humorous wrapper for `pacman` on Arch Linux that prints random roast messages while running your package commands.

## Features
- Works with **all pacman commands and flags**
- Prints random roast messages
- Lightweight, no dependencies

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/pacroast.git
cd pacroast
chmod +x pacroast.py
sudo mv pacroast.py /usr/local/bin/pacroast
```
Then run:
```bash
pacroast -Syu
pacroast -S ripgrep (for testing)
pacroast -Rcs old-package
```

## Customization
Edit `roasts.txt` to add or change your roast messages.
