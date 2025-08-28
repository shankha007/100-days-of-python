# Todo List

A simple **Todo List application** built with Python.  
This project helps users create, manage, and track tasks efficiently.  
It can be implemented as a **console app**, **desktop app (Tkinter/PyQt)**, or **web app (Flask/Django)**.

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

The **Todo List App** allows users to add, update, delete, and mark tasks as complete.  
It’s a great project for practicing CRUD operations, file/database management, and user interfaces.

---

## Features

- Add new tasks  
- View all tasks  
- Mark tasks as complete/incomplete  
- Edit task details  
- Delete tasks  
- Save tasks to file or database  
- Different versions possible:
  - **Console version** (basic, file storage)  
  - **Desktop GUI version** (Tkinter/PyQt)  
  - **Web version** (Flask/Django + SQLite)  

---

## Requirements

- Python 3.7 or later  
- Depending on version:  
  - **Console:** no external libraries (just `os`, `json`)  
  - **Desktop GUI:** `tkinter` (default) or `PyQt5`  
  - **Web:** `flask`, `flask-sqlalchemy`, `jinja2`  

Install dependencies (for web version):
```bash
pip install flask flask-sqlalchemy
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/todo-list.git
   ```
2. Navigate to the project folder:
   ```bash
   cd todo-list
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Console Version
```bash
python todo.py
```
- Follow the menu prompts to add, view, update, or delete tasks.  

### GUI Version (Tkinter/PyQt)
```bash
python gui_todo.py
```
- A window opens where you can manage tasks with buttons and input fields.  

### Web Version (Flask)
```bash
python app.py
```
- Visit `http://127.0.0.1:5000/` in your browser.  

---

## How It Works

1. **Data Storage**  
   - Console/GUI → JSON or text file  
   - Web → SQLite database (via SQLAlchemy)  

2. **CRUD Operations**  
   - Create → Add new task  
   - Read → View tasks list  
   - Update → Edit/mark task complete  
   - Delete → Remove task  

3. **Flow**  
   - User interacts with app → task is saved → list updates → changes persist across sessions.  

---

## Project Structure

```
todo-list/
├── todo.py              # Console version
├── gui_todo.py          # GUI version (Tkinter/PyQt)
├── app.py               # Flask web app
├── models.py            # Database models (if web)
├── templates/           # HTML files for web version
│   ├── base.html
│   ├── index.html
│   └── add_task.html
├── static/              # CSS/JS for web version
├── tasks.json           # Data file (console/GUI version)
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## Screenshots

*(Optional: Add screenshots of console, GUI, or web UI here)*

---

## Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a new branch (`feature-xyz`)  
3. Commit your changes  
4. Push to your fork  
5. Create a Pull Request  

Ideas for improvement:
- Add due dates & reminders  
- Task categories (Work, Personal, Urgent)  
- Search and filter functionality  
- User authentication for multi-user web app  
- Sync tasks with cloud or mobile  

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
