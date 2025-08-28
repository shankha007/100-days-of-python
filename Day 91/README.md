# Convert PDF to Audiobook

A Python project that converts any PDF file into an audiobook.  
It extracts text from the PDF and uses a text-to-speech (TTS) engine to generate audio output.

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

The **Convert PDF to Audiobook** project provides an easy way to listen to books, articles, and documents.  
It uses **PyPDF2** (or `pdfplumber`) to read PDF text and a **TTS engine** (such as `pyttsx3` or `gTTS`) to narrate the content.

---

## Features

- Extract text from PDF files  
- Convert text to audio using a speech engine  
- Supports **English** (extendable to other languages)  
- Option to **save audio as an MP3 file**  
- Works offline with `pyttsx3` (no internet required)  
- Lightweight and user-friendly  

---

## Requirements

- Python 3.7 or later  
- Libraries:
  - `PyPDF2` (PDF text extraction)  
  - `pyttsx3` (offline text-to-speech) or `gTTS` (Google TTS, requires internet)  

Install dependencies:
```bash
pip install PyPDF2 pyttsx3
# Optional: pip install gTTS
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pdf-to-audiobook.git
   ```
2. Navigate to the project folder:
   ```bash
   cd pdf-to-audiobook
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the script:
```bash
python pdf_to_audio.py
```

Steps:
1. Enter the path to your PDF file.  
2. The program extracts text from the PDF.  
3. The text is read aloud using the TTS engine.  
4. Optionally, audio is saved as an MP3 file.  

---

## How It Works

1. The program loads the PDF using `PyPDF2.PdfReader`.  
2. Extracts text page by page.  
3. Feeds text to a TTS engine:  
   - **pyttsx3** → offline, customizable voice & speed  
   - **gTTS** → online, generates MP3 using Google Translate API  
4. Plays the audio or saves it as a file.  

---

## Project Structure

```
pdf-to-audiobook/
├── pdf_to_audio.py     # Main script
├── requirements.txt    # Dependencies
├── sample.pdf          # Example input file
├── output.mp3          # Generated audiobook (optional)
└── README.md           # Documentation
```

---

## Screenshots

*(Optional: Add screenshots of terminal input/output or saved MP3 in folder)*

---

## Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a new branch (`feature-xyz`)  
3. Commit your changes  
4. Push to your fork  
5. Create a Pull Request  

Ideas for improvement:
- Add **GUI** using Tkinter or PyQt  
- Add **language selection**  
- Highlight text while reading (synchronized reading)  
- Batch convert multiple PDFs into audiobooks  

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
