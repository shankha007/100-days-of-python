# Image Colour Palette Generator

A Python application that generates a **colour palette** from any given image.  
It extracts the most dominant colours and displays them visually, making it useful for designers, developers, and artists.

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

The **Image Colour Palette Generator** analyzes an image and identifies its most prominent colours.  
It uses clustering techniques (like **K-Means**) to extract colour values and generates a palette for inspiration or design use.

---

## Features

- Extract **dominant colours** from any image  
- Display colour swatches with HEX & RGB values  
- Save generated palette as an image or text file  
- Adjustable number of colours in palette  
- Works with PNG, JPG, and other formats  
- Lightweight and beginner-friendly  

---

## Requirements

- Python 3.7 or later  
- Libraries:
  - `opencv-python` (for image loading & processing)  
  - `numpy` (array handling)  
  - `matplotlib` (for displaying palette)  
  - `scikit-learn` (K-Means clustering)  

Install dependencies:
```bash
pip install opencv-python numpy matplotlib scikit-learn
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/image-colour-palette-generator.git
   ```
2. Navigate to the project folder:
   ```bash
   cd image-colour-palette-generator
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the script:
```bash
python palette_generator.py
```

Steps:
1. Enter the path to your image file.  
2. The program extracts colours and displays the palette.  
3. Palette HEX/RGB codes are printed on screen.  
4. (Optional) Palette can be saved as an image or text file.  

---

## How It Works

1. Load the image with `OpenCV`.  
2. Reshape image into a 2D array of pixels.  
3. Apply **K-Means clustering** to group colours.  
4. Extract dominant cluster centres as **palette colours**.  
5. Display the colours using `matplotlib` with their HEX/RGB values.  

---

## Project Structure

```
image-colour-palette-generator/
├── palette_generator.py   # Main script
├── requirements.txt       # Dependencies
├── images/                # Sample input images
├── output/                # Generated palettes
└── README.md              # Documentation
```

---

## Screenshots

*(Optional: Add before/after screenshots showing an image and its generated palette)*

---

## Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a new branch (`feature-xyz`)  
3. Commit your changes  
4. Push to your fork  
5. Create a Pull Request  

Ideas for improvement:
- Add GUI (Tkinter or PyQt) for drag-and-drop images  
- Save palettes in JSON/ASE format (for Photoshop/Illustrator)  
- Generate complementary/analogous colour schemes  
- Web app version (Flask/Streamlit)  

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
