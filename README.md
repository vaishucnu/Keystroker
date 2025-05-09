# Keylogger (For Educational Use Only)

> ⚠️ **DISCLAIMER:**  
> This software is provided **strictly for educational, or controlled penetration testing environments** where **all participants have given explicit consent**. Unauthorized use of this software to spy on users, steal credentials, or monitor keystrokes without permission is **illegal and unethical**, and may result in severe legal consequences.

---

## 🧠 Overview

This is a simple Python-based keylogger script that:

- Records all keyboard input using `pynput`
- Logs keystrokes into memory
- Sends the keystroke log via email using Gmail SMTP
- Repeats the sending process at timed intervals

---

## ⚙️ Features

- Captures normal and special keystrokes (e.g., backspace, space)
- Sends logs via email every 10 seconds (adjustable)
- Uses threading for asynchronous log delivery
- Runs in the background once started

---

## 📦 Requirements

- Python 3.x
- Packages:
  - `pynput`
  - `smtplib` (standard library)
  - `threading` (standard library)

Install dependencies (if needed):

```bash
pip install pynput
```

## 🚀 Usage
IMPORTANT: Do not run this script on any system you do not own or have permission to test.

1. Open keylogger.py
2. Replace the following:
  - "username" → your Gmail address
  - "password" → your Gmail App Password (not regular password)
3. Run the script:
  ```bash
python keylogger.py
  ```
