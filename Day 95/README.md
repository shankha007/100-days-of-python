# Space Invaders

A Python implementation of the classic **Space Invaders** arcade game.  
Built using the **Pygame** library, the player controls a spaceship to shoot down waves of incoming aliens while avoiding enemy attacks.

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

The **Space Invaders** project recreates the retro arcade game where the player defends Earth against alien invaders.  
The spaceship moves left and right along the bottom of the screen, shooting bullets upward to destroy enemies before they reach the player.

---

## Features

- Player-controlled spaceship with movement & shooting  
- Multiple enemies that move and descend toward the player  
- Collision detection for bullets and enemies  
- Score tracking system  
- Game over when enemies reach the bottom or player collides with them  
- Retro-style graphics and sounds  

---

## Requirements

- Python 3.7 or later  
- Libraries:
  - `pygame` (game development library)  

Install dependencies:
```bash
pip install pygame
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/space-invaders.git
   ```
2. Navigate to the project folder:
   ```bash
   cd space-invaders
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the game:
```bash
python space_invaders.py
```

### Controls
- **Left Arrow / A** → Move left  
- **Right Arrow / D** → Move right  
- **Spacebar** → Shoot  

---

## How It Works

1. The game window is created using **Pygame**.  
2. The player spaceship is drawn at the bottom of the screen.  
3. Multiple enemy sprites move horizontally and descend gradually.  
4. Player bullets travel upward, destroying enemies on collision.  
5. The game ends if:
   - An enemy collides with the player  
   - Enemies reach the bottom of the screen  

---

## Project Structure

```
space-invaders/
├── space_invaders.py    # Main game script
├── assets/              # Images & sounds
│   ├── player.png
│   ├── enemy.png
│   ├── bullet.png
│   └── background.png
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## Screenshots

*(Optional: Insert game screenshots showing gameplay, spaceship, and enemies)*

---

## Contributing

Contributions are welcome!  
1. Fork the repository  
2. Create a new branch (`feature-xyz`)  
3. Commit your changes  
4. Push to your fork  
5. Create a Pull Request  

Ideas for improvement:
- Add **levels** with increasing difficulty  
- Add **power-ups** (e.g., faster bullets, shields)  
- Add **background music & sound effects**  
- Implement **multiplayer mode**  

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
