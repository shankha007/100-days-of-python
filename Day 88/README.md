# Cafe and WiFi Website

A Python-based web application where users can browse and share information about cafes, including details like location, coffee quality, and WiFi availability.  
This project is built with **Flask** and uses a database to store cafe details.

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

The **Cafe and WiFi Website** allows users to view cafes and their amenities (WiFi speed, power sockets, coffee rating, etc.).  
It demonstrates building a Flask web app with a database, HTML forms, and RESTful routes.

---

## Features

- Home page listing cafes
- Add new cafes (via web form)
- View cafe details (address, WiFi, power sockets, coffee rating)
- Update or delete cafes (if enabled)
- Responsive design (with Bootstrap/HTML templates)
- SQLite database integration
- REST API (optional)

---

## Requirements

- Python 3.7 or later  
- Recommended libraries:
  - `Flask` (web framework)
  - `Flask-WTF` (form handling)
  - `Flask-SQLAlchemy` (ORM for database)
  - `WTForms` (form validation)
  - `Jinja2` (templating, built into Flask)

Install dependencies:
```bash
pip install flask flask-wtf flask-sqlalchemy
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cafe-and-wifi-website.git
   ```
2. Navigate to the project folder:
   ```bash
   cd cafe-and-wifi-website
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the app locally:
```bash
python app.py
```

Then open your browser and visit:
```
http://127.0.0.1:5000/
```

---

## How It Works

1. The app initializes with Flask and connects to an SQLite database.  
2. The `Cafe` model stores details such as:  
   - Name  
   - Location  
   - Coffee rating  
   - WiFi strength  
   - Power socket availability  
3. Routes handle:
   - `/` → Homepage with list of cafes  
   - `/add` → Add new cafe (via form)  
   - `/cafes` → API endpoint returning cafes as JSON (optional)  
4. Templates (`Jinja2`) render pages dynamically.  
5. Users can submit new cafes, and data is saved in the database.  

---

## Project Structure

```
cafe-and-wifi-website/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── forms.py               # WTForms classes
├── templates/             # HTML templates (Jinja2)
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   └── cafes.html
├── static/                # CSS, JS, images
├── instance/              # SQLite database
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## Screenshots

*(Optional: Insert screenshots of the homepage, add cafe form, and cafe list page)*

---

## Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a new branch (`feature-xyz`)  
3. Commit your changes  
4. Push to your fork  
5. Create a Pull Request  

Ideas for improvement:
- Add user authentication (login/signup)  
- Allow image uploads for cafes  
- Add search & filter functionality  
- Deploy on Heroku, Render, or Railway  

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
