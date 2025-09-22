# 🎃 horror_box  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python project that **plays spooky sounds at random times** with random volume + delay.  
Perfect for haunted houses, Halloween setups, or just scaring your friends.  

> ⚠️ Use responsibly — sudden loud noises can upset pets, children, or neighbors. Uses demo sound file placeholders — add your own MP3/WAV files for real scares.

---

## 📌 Project Overview  
- Goal → Build a simple “horror box” that plays random creepy sounds.  
- Approach → Store demo sound files in `/sounds`, run a Python script to randomly select and play them.  
- Status → Portfolio/creative coding project. Extendable with timers, key presses, or IoT triggers (Raspberry Pi 👀).  

---

## 📂 Repo Structure  
```
horror_box/
│── horror.py          # Main script  
│── requirements.txt   # Dependencies (pydub, simpleaudio, etc.)  
│── .gitignore  
│── README.md  
│── sounds/            # Demo spooky sound files (placeholders)  
│   ├── chains.mp3          # Creepy Chains  
│   ├── ghost.wav           # Ghostly Wail  
│   ├── spiders.mp3         # Crawling Spiders  
│   ├── axe.wav             # Distant Axe Chop  
│   ├── heartbeat.mp3       # Heartbeat in the Dark  
│   └── fog.wav             # Whispering Fog  
│── outputs/           # (Optional) Future logs or recordings  
```
---

## ✅ Features  
- Randomly selects spooky sounds from `/sounds/`  
- Supports MP3 and WAV via **pydub**
- Uses ffmpeg backend for audio processing so readers immediately know it's required
- Plays at randomized intervals (e.g., every 5–30 seconds)  
- Varies playback volume slightly for realism  
- Works cross-platform (macOS, Linux, Windows Powershell)
- Extendable for haunted house setups
- Logs each scare event to `/logs/`  

---

## 📦 Requirements  
- Python 3.10+  
- `pip`  
- Packages listed in `requirements.txt`

Install manually:
```bash
pip install -r requirements.txt
```
This project uses **pydub + simpleaudio** (not `playsound`).  
They provide better cross-platform playback and support both MP3 & WAV.


## 🔊 Installing ffmpeg
pydub requires ffmpeg to handle MP3/WAV playback. Install it depending on your OS:

macOS (Homebrew)
```bash
brew install ffmpeg
```
Linux (Debian/Ubuntu):
```bash
sudo apt update && sudo apt install ffmpeg
```
Windows (Chocolatey):
```powershell
choco install ffmpeg
```
Once installed, verify with:

```bash
ffmpeg -version
```


## 🚀 Installation
Clone repo:
```bash
git clone https://github.com/kelynst/horror_box.git
cd horror_box
```
Create a virtual environment:
```bash
python3 -m venv .venv
```
Activate it:
macOS/Linux
```bash
source .venv/bin/activate
```
Windows PowerShell
```bash
.venv\Scripts\Activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ Usage
Place your spooky sound files (.wav or .mp3) into the sounds/ folder, then run randomly or directly:

Random run:
```bash
python3 horror.py
```

Or specify direct sound:
```bash
python3 horror.py --sound ghost
```
### Available sounds
- **`chains`** → Creepy Chains  
- **`ghost`** → Ghostly Wail  
- **`axe`** → Distant Axe Chop  
- **`heartbeat`** → Heartbeat in the Dark  
- **`spiders`** → Crawling Spiders  
- **`fog`** → Whispering Fog  


### Example Output:

```
🎃 Horror Box Activated 🎃


Waiting 12s...
Random sound chosen: ghost.wav
🔊 Playing Ghostly Wail...

✅ Done. Ready for the next scare!

---

Also possible:

Random sound chosen: chains.mp3
🔊 Playing Creepy Chains...

Random sound chosen: spiders.mp3
🔊 Playing Crawling Spiders...

Random sound chosen: axe.wav
🔊 Playing Distant Axe Chop...

Random sound chosen: heartbeat.mp3
🔊 Playing Heartbeat in the Dark...

Random sound chosen: fog.wav
🔊 Playing Whispering Fog...

✅ Done. Ready for the next scare!
```

## 🔮 Future Improvements
- Add background looping "ambient" sounds
- Trigger sounds with keyboard shortcuts
- Connect to IoT (smart lights & sound sync)
- Build a simple GUI soundboard

## 🤝 Contributing
Contributions welcome!
1. Fork the repo
2. Create a branch 
```bash
git checkout -b feature-xyz
```
3. Commit changes
```bash
git commit -m "Add feature xyz"
```
4. Push 
```bash
git push origin feature-xyz
```

5. Open a Pull Request 🎉 
Suggestions for new spooky sound ideas are especially welcome 👻

## ⚠️ Notes
- Demo sounds are placeholders, replace with your own files
- This project is for fun/demo purposes only

## 📜 License
MIT — see LICENSE.