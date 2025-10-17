# 🎭 Farsi Mafia Game

A simple, console-based **Mafia Game in Persian (Farsi)** — written in Python.  
Players take turns revealing their secret roles, clearing the screen between each reveal to maintain suspense. This project brings the classic party game "Mafia" to life for Persian speakers in a fun and minimalist way.

---

## 🧠 About the Game

This project is a **terminal-based Persian Mafia (Werewolf-style)** game. It supports customizable player and mafia counts and assigns roles like:

- 🕵️‍♂️ **Karagah (Detective)**
- 💉 **Doctor**
- 🔫 **Sniper**
- 🦺 **ZerehPosh (Armored)**
- 😈 **GodFather**
- 😎 **Mafia Sade (Regular Mafia)**
- 🧍‍♂️ **Shahrvand Sade (Civilian)**

Each player privately views their role before the screen is cleared for the next player, keeping everything secret — just like the real-life Mafia experience.

---

## ✨ Features

- Full **Persian/Farsi text-based interface**
- Secret **role distribution system**
- Auto-clearing terminal between players for privacy
- Role customization and random shuffling
- Simple, dependency-light Python codebase
- Perfect for small friend groups (6+ players)

---

## ⚙️ Requirements

- Python 3.7 or newer  
- `termcolor` package for colored terminal output  

You can install the required package with:

    pip install termcolor

---

## 🚀 How to Run

1. Clone this repository:

       git clone https://github.com/ParsaTB/Farsi-Mafia-Game.git
       cd Farsi-Mafia-Game

2. Run the game:

       python mafia.py

3. Follow the prompts (in Farsi):
   - Enter the number of players
   - Enter the number of mafia members
   - Each player presses ENTER to see their role
   - Press ENTER again to clear the screen for the next player

---

## 🕹️ Example Gameplay

    Tedad Bazikonan Ra Vared Konid: 6
    Tedad Mafia Ha Ra Vared Konid: 2
    
    Baray Didan Naqsh ENTER Bezanid.
    Doctor
    Baray Khali Shodan Safhe ENTER Bezani.
    
    (terminal clears)
    
    Baray Didan Naqsh ENTER Bezanid.
    GodFather
    ...

This continues until all players have viewed their secret roles.

---

## 🧩 How It Works (Code Overview)

- `shuffle_roles()` creates a list of all roles based on the number of players and mafia.
- Roles are randomized using Python's `random.shuffle()`.
- Each player presses ENTER to reveal their role in private.
- The terminal is cleared using `os.system('cls' if os.name == 'nt' else 'clear')` to hide the previous role.
- The `termcolor` library adds color to prompts and messages for a more engaging look.

---

## 🤝 Contributing

If you'd like to improve or expand this project:

1. Fork this repo
2. Create a feature branch (`git checkout -b new-feature`)
3. Commit your changes
4. Submit a pull request!

---

## 📜 License

This project is open-source under the MIT License.  
Feel free to use, modify, and share it with credit.

---

## 📬 Contact

👤 **Author:** ParsaTB  
📧 **Email:** parsatborg@gmail.com  

⭐ If you like this project, consider giving it a star on GitHub!
