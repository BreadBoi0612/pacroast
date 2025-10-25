# PacRoast v1.1!!!!!!

PacRoast is a humorous wrapper for `pacman` on Arch Linux that roasts you for whatever you're doing — installing, updating, removing, syncing, or even asking for help.

## 🧠 How it works
- `-Syu` → *System update roast*
- `-Syu <pkg>` → *App update roast*
- `-S` → *Install roast*
- `-R` → *Remove roast*
- `-Q` → *Query roast*
- `-Si`, `-Ss` → *Search roast*
- `-F` → *File lookup roast*
- `-D` → *Database roast*
- `-Sc`, `-Scc` → *Cleanup roast*
- `-Sy` → *Repo sync roast*
- `-h` → *Help roast*
- Everything else → *General roast*

## ⚙️ Installation
```bash
git clone https://github.com/BreadBoi0612/pacroast.git
cd pacroast
chmod +x pacroast.py
sudo mv pacroast.py /usr/local/bin/pacroast
```
# OR
DM me on discord and I'll send you the files directly (@BreadBoi0612)

## Test Commands
```
pacroast -Syu                # System update roast
pacroast -Syu lolcat         # App update roast
pacroast -S ripgrep          # Install roast
pacroast -Rcs ripgrep        # Remove roast
pacroast -Qe                 # Query roast
pacroast -Si neovim          # Search/info roast
pacroast -F .bashrc          # File lookup roast
pacroast -D something        # Database roast
pacroast -Sc                 # Cleanup roast
pacroast -Sy                 # Repo sync roast
pacroast -h                  # Help roast
pacroast                     # Default/general roast
