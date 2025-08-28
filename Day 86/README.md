# Typing Speed Test

A Python-based application that measures a user's typing speed (words per minute and accuracy) through an interactive interface.  
This project is lightweight, beginner-friendly, and can run in the terminal or with a GUI.

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

The **Typing Speed Test** app challenges users to type a random passage as quickly and accurately as possible.  
At the end of the test, the app displays statistics like Words Per Minute (WPM), accuracy percentage, and error count.

---

## Features

- Randomly selects a sentence or paragraph for each test
- Tracks typing speed in **Words Per Minute (WPM)**
- Calculates **accuracy percentage** based on typed vs. expected text
- Highlights mistakes (for GUI or console output)
- Optional timer mode
- Supports both:
  - **Terminal/console version** (basic version with Python I/O)
  - **GUI version** (using `tkinter` or `PyQt`)

---

## Requirements

- Python 3.7 or later  
- Libraries (depending on version):
  - `time` (built-in, for tracking duration)
  - `random` (built-in, for text selection)
  - `tkinter` (for GUI version, included with Python)
  - `pygame` (optional, for advanced GUI or sounds)

Install dependencies (if using GUI/pygame):
```bash
pip install pygame
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/typing-speed-test.git
   ```
2. Navigate to the project folder:
   ```bash
   cd typing-speed-test
   ```
3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the program:
```bash
python typing_test.py
```

Steps (console version):
1. The program displays a random sentence/paragraph.  
2. Start typing as soon as you’re ready.  
3. Press **Enter** when done.  
4. Results are displayed:
   - Time taken
   - Words Per Minute (WPM)
   - Accuracy percentage
   - Errors  

Steps (GUI version):
1. A window opens with the text displayed at the top.  
2. Type in the input box as fast as possible.  
3. Once finished, click **Submit** or press Enter.  
4. Results appear on screen.  

---

## How It Works

1. A random passage is chosen from a predefined list.  
2. The timer starts when the user begins typing.  
3. The app compares the typed text with the reference passage:  
   - Correct words → counted towards accuracy  
   - Errors → highlighted / counted  
4. WPM is calculated using:
   ```
   WPM = (Number of words typed / Time in seconds) * 60
   ```
5. Accuracy is calculated as:
   ```
   Accuracy (%) = (Correct characters / Total characters) * 100
   ```
6. Results are displayed in the terminal or GUI.  

---

## Project Structure

```
typing-speed-test/
├── typing_test.py        # Main application file (console version)
├── gui_typing_test.py    # GUI version (tkinter/pygame)
├── texts.py              # List of random sentences/paragraphs
├── requirements.txt      # Dependencies (if any)
├── assets/               # Optional: fonts, sounds, or images for GUI
└── README.md             # Project documentation
```

---

## Screenshots

*(Optional: Add terminal screenshot or GUI snapshot here)*

---

## Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a new branch (`feature-xyz`)  
3. Commit your changes  
4. Push to your fork  
5. Create a Pull Request  

Ideas for improvement:
- Add leaderboard (track high scores)  
- Difficulty levels (short vs. long passages)  
- Dark mode in GUI  
- Multiplayer mode (race against friends)  

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
