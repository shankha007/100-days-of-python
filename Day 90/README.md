# Disappearing Text Writing App

A Python desktop app that helps you stay focused while writing.  
The challenge: **if you stop typing for a few seconds, your text disappears!**  
This project is built using `tkinter` for the GUI.

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

The **Disappearing Text Writing App** is a fun productivity tool designed to encourage consistent typing.  
Writers must keep typing without long pauses—otherwise, their work vanishes.  
This concept is inspired by writing challenges that reward continuous focus.

---

## Features

- Simple, clean interface (`tkinter`)  
- Large text area for writing  
- Countdown timer resets as you type  
- If the timer reaches zero, all text is deleted  
- Adjustable countdown duration (default: 5 seconds)  
- Option to save your work before it disappears (if you stop in time!)  

---

## Requirements

- Python 3.7 or later  
- Libraries:
  - `tkinter` (comes with Python)  

Optional (for extensions):  
- `playsound` → Add sound alerts when time is running out  

Install extra library if needed:
```bash
pip install playsound
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/disappearing-text-app.git
   ```
2. Navigate to the project folder:
   ```bash
   cd disappearing-text-app
   ```
3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the app:
```bash
python app.py
```

Steps:
1. A window opens with a text box.  
2. Start typing — the countdown resets each time you press a key.  
3. If you stop typing for too long (default: 5 seconds) → **all text disappears**.  
4. Optional: Save your writing before taking a break.  

---

## How It Works

1. The app uses `tkinter` for the GUI (main window + text widget).  
2. A timer is set (e.g., 5 seconds).  
3. On every keystroke:
   - The timer resets.  
   - The countdown continues in the background.  
4. If the countdown reaches zero:
   - The text area is cleared.  
   - The user must start again.  

This teaches discipline: **don’t stop writing!**

---

## Project Structure

```
disappearing-text-app/
├── app.py             # Main application file
├── requirements.txt   # Dependencies (optional)
├── assets/            # (Optional) Fonts, sounds, icons
└── README.md          # Documentation
```

---

## Screenshots

*(Optional: Add screenshot of the text editor with timer running)*

---

## Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a new branch (`feature-xyz`)  
3. Commit your changes  
4. Push to your fork  
5. Create a Pull Request  

Ideas for improvement:
- Customizable timer length  
- Save automatically every few seconds  
- Dark mode for writing at night  
- Sound/visual alerts before text disappears  
- Cloud sync for documents  

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
