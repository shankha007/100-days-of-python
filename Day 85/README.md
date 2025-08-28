# Image Watermarking Desktop App

A Python-based desktop application that allows users to add custom watermarks (text or image) to their images.  
This project is designed with a simple GUI for ease of use and can handle batch watermarking.

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

The **Image Watermarking Desktop App** makes it easy to protect your images by embedding a visible watermark.  
Users can upload their images, enter text or select a watermark image, customize placement, and save the watermarked output.

---

## Features

- Graphical User Interface (GUI) using `tkinter` or `PyQt`
- Add **text watermark** with customizable:
  - Font style, size, and color
  - Position (top-left, top-right, center, bottom-left, bottom-right)
  - Transparency level
- Add **image watermark** with resizing and transparency options
- Support for **batch watermarking**
- Save images in multiple formats (PNG, JPG, etc.)
- Lightweight and beginner-friendly

---

## Requirements

- Python 3.7 or later  
- Recommended libraries:
  - `Pillow` (PIL Fork, for image processing)
  - `tkinter` (default with Python, for GUI) or `PyQt5`
  - `os` and `sys` (built-in)
  - `numpy` (optional, if needed for advanced image manipulation)

Install dependencies via pip:
```bash
pip install pillow
pip install pyqt5   # if using PyQt
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/image-watermarking-app.git
   ```
2. Navigate to the project folder:
   ```bash
   cd image-watermarking-app
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the application:
```bash
python app.py
```

Steps:
1. Launch the app window.  
2. Select an image (or folder for batch mode).  
3. Choose watermark type:
   - **Text Watermark** → Enter text, choose font, size, position, and transparency.  
   - **Image Watermark** → Upload watermark image, adjust size, position, and transparency.  
4. Click **Apply Watermark**.  
5. Save the new watermarked image(s).  

---

## How It Works

1. The app loads the target image(s) using `Pillow`.  
2. For text watermark:
   - Renders text with chosen font & transparency.  
   - Pastes onto image at selected position.  
3. For image watermark:
   - Opens watermark image, resizes & adjusts transparency.  
   - Pastes onto original image.  
4. Saves the modified image(s) in the desired format.  

---

## Project Structure

```
image-watermarking-app/
├── app.py                 # Main application file (GUI + logic)
├── watermark.py           # Core watermarking logic
├── requirements.txt       # Project dependencies
├── assets/                # Example watermark images, fonts
├── output/                # Generated watermarked images
├── tests/                 # (Optional) Unit tests
└── README.md              # Project documentation
```

---

## Screenshots

*(Optional: Add sample screenshots of the GUI and watermarked images here)*

---

## Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a new branch (`feature-xyz`)  
3. Commit your changes  
4. Push to your fork  
5. Create a Pull Request  

Ideas for improvement:
- Drag-and-drop image support  
- Predefined watermark templates  
- Export settings for batch use  
- Cross-platform executable (using `PyInstaller`)  

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
