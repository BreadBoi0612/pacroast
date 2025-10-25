# PacRoast 0.8

PacRoast is a humorous wrapper for `pacman` on Arch Linux that prints sarcastic roast messages depending on what you’re doing.

## 🧠 How it works
- `-Syu`: Update roast (“Skipped updates again? Bold move, buddy.”)
- `-S` + other flags: Install roasts (“Installing {}… wow, really living on the edge.”)
- `-R`: Removal roasts (“Farewell, {}. You won’t be missed.”)
- Everything else: Random general roasts

## ⚙️ Installation
```bash
git clone https://github.com/YOUR_USERNAME/pacroast.git
cd pacroast
chmod +x pacroast.py
sudo mv pacroast.py /usr/local/bin/pacroast
