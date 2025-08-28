# Automate the Google Dinosaur Game

A Python project that automates the **Google Chrome Dinosaur Game** (the offline game shown when no internet connection is available).  
The bot detects obstacles on the screen and makes the dinosaur jump or duck automatically to maximize the score.

---

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## Description

The **Automate the Google Dinosaur Game** project uses **image processing** and **keyboard automation** to control the Chrome Dino.  
The bot continuously monitors the screen, detects upcoming obstacles, and sends key presses to jump/duck at the right time.

---

## Features

- Plays the Google Dinosaur Game automatically  
- Detects obstacles using **screenshot + image processing**  
- Controls keyboard with simulated key presses  
- Adjustable speed and difficulty handling  
- Works in any Chromium-based browser (tested on Chrome)  

---

## Requirements

- Python 3.7 or later  
- Libraries:
  - `pyautogui` (for key presses & screenshots)  
  - `opencv-python` (for image recognition)  
  - `numpy` (for array handling)  
  - `time` (built-in)  

Install dependencies:
```bash
pip install pyautogui opencv-python numpy
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/automate-dino-game.git
   ```
2. Navigate to the project folder:
   ```bash
   cd automate-dino-game
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Open Google Chrome.  
2. Go offline and start the **Dino Game** (`chrome://dino`).  
3. Run the bot script:
   ```bash
   python dino_bot.py
   ```
4. The bot will detect obstacles and control the Dino automatically.  

> ⚠️ **Tip:** Make sure the browser window is not minimized and the game is visible on screen.

---

## How It Works

1. **Screen Capture** → Continuously take screenshots of a specific region near the Dino.  
2. **Image Processing** → Use `OpenCV` + `numpy` to detect changes (obstacles like cacti or birds).  
3. **Decision Making** → If obstacle is detected at a threshold distance, decide whether to jump or duck.  
4. **Automation** → Use `pyautogui` to press `space` (jump) or `down` (duck).  

---

## Project Structure

```
automate-dino-game/
├── dino_bot.py          # Main automation script
├── requirements.txt     # Dependencies
├── assets/              # (Optional) Reference images
└── README.md            # Documentation
```

---

## Screenshots

*(Optional: Add screenshots of the game being automated with the bot running)*

---

## Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a new branch (`feature-xyz`)  
3. Commit your changes  
4. Push to your fork  
5. Create a Pull Request  

Ideas for improvement:
- Train a **machine learning model** (instead of static detection)  
- Add support for **higher speeds** and dynamic difficulty  
- Integrate with **TensorFlow/PyTorch** for reinforcement learning  
- Add a GUI to start/stop the bot  

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
