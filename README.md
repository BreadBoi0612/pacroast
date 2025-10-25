# PacRoast v1.0!!!!!!

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
git clone https://github.com/YOUR_USERNAME/pacroast.git
cd pacroast
chmod +x pacroast.py
sudo mv pacroast.py /usr/local/bin/pacroast
