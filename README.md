# 🔤 Morse Code Converter

A simple and interactive terminal-based application written in **Python** that allows users to **encode text into Morse code** and **decode Morse code back to text**. This project is perfect for beginners who want to practice string manipulation, dictionaries, and user input in Python.

---

## 📌 Table of Contents

- [🔤 Morse Code Converter](#-morse-code-converter)
  - [📌 Table of Contents](#-table-of-contents)
  - [🚀 Features](#-features)
  - [⚙️ How It Works](#️-how-it-works)
  - [🧰 Technologies](#-technologies)
  - [🛠️ Getting Started](#️-getting-started)
    - [1. Clone the repository](#1-clone-the-repository)
    - [2. Run the program](#2-run-the-program)
  - [▶️ Usage](#️-usage)
  - [🧪 Examples](#-examples)
    - [🔐 Encode](#-encode)
    - [🔓 Decode](#-decode)
  - [📚 What I Learned](#-what-i-learned)
  - [📄 License](#-license)
  - [👤 Author](#-author)
  - [💬 Feedback](#-feedback)

---

## 🚀 Features

- Convert **text to Morse code**
- Convert **Morse code to text**
- Support for **letters**, **numbers**, and **punctuation**
- **Accent removal** from input text
- Detects if input is valid Morse code
- Simple and user-friendly **command-line interface**
- Built entirely in **pure Python**

---

## ⚙️ How It Works

- Input text is normalized using `unicodedata` to remove accents.
- Morse code is generated using a dictionary that maps characters to Morse symbols.
- Letters are separated by 3 spaces, and words by 7 spaces.
- Decoding matches Morse code symbols back to characters using reverse mapping.

---

## 🧰 Technologies

- **Python 3**
- Standard library:
  - `unicodedata`
  - `input()`
  - `print()`

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/CelmarPA/Morse_code
cd Morse_Code_Python
```

### 2. Run the program

```bash
python3 main.py
```

---

## ▶️ Usage

> 💡 **When you run the program, you will see a prompt like this:**

```
======= Welcome to Morse Code Converter ========
Enter 1 to convert text into morse code,
2 to convert morse code into text,
q or quit to exit:
```

Choose an option and follow the instructions to encode or decode your message.

---

## 🧪 Examples

### 🔐 Encode

**Input:**
```
HELLO WORLD
```

**Output:**
```
....   .   .-..   .-..   ---       .--   ---   .-.   .-..   -..
```

---

### 🔓 Decode

**Input:**
```
.... . .-.. .-.. ---       .-- --- .-. .-.. -..
```

**Output:**
```
HELLO WORLD
```

---

## 📚 What I Learned

This project helped me practice:

- Working with **dictionaries** in Python
- **Normalizing and sanitizing** input strings
- Using **control structures** (loops, conditionals)
- Designing **user-friendly CLI** applications
- Mapping between **symbolic and readable** data

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use and modify it as you like.

---

## 👤 Author

**Celmar Pereira**

- [GitHub](https://github.com/CelmarPA)
- [LinkedIn](https://linkedin.com/in/celmar-pereira-de-andrade-039830181)
- [Portfolio](https://yourportfolio.com)

---

## 💬 Feedback

If you find a bug or have suggestions for improvement, feel free to **open an issue** or **submit a pull request**. Contributions are welcome!
