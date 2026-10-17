# Password Manager (Tkinter)

A desktop password manager GUI built with **Python** and **Tkinter** — a learning project exploring GUI development, JSON persistence, and the clipboard API.

---

## ✨ Features

* **Password generator** — creates a 16-character password (uppercase, lowercase, digits) and copies it to your clipboard automatically
* **Save credentials** — stores website / email / password entries in `data.json`
* **Search** — look up a saved password by website name
* Simple, friendly Tkinter UI with logo canvas

---

## 🛠️ Requirements

* Python 3.x
* [pyperclip](https://pypi.org/project/pyperclip/)

```
pip install pyperclip
```

---

## ▶️ Usage

```
python main.py
```

1. Enter a website and email, then press **Generate Password** (or type your own)
2. Press **Add** to save the entry
3. To retrieve an entry: type the website name and press **Search**

---

## 📂 Project Structure

```
Password-Manger-Tkinter/
├── main.py      # App: UI, generator, save/search logic
├── data.json    # Saved credentials (sample entries included)
├── logo.png     # App logo
└── README.md
```

---

## ⚠️ Note

This is an **educational project**: credentials are stored in a local JSON file **in plain text**. Don't use it for real passwords — a good next step would be adding encryption (e.g. the `cryptography` package).

Sample entries (`Amazon`, `Ebay`) are included in `data.json` — replace or delete them.
