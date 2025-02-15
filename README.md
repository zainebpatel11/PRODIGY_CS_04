# PRODIGY_CS_04
# Ethical Keylogger

This Ethical Keylogger is a Python-based application designed for educational purposes to demonstrate how keylogging works. The program provides real-time logging of keyboard inputs, displays typing statistics, and saves encrypted logs.

## 🚨 Disclaimer
This tool is intended for educational and ethical purposes only. Unauthorized use of keyloggers is illegal.

## 🛠️ Features
- Real-time keylogging with date and time
- User-friendly graphical interface using Tkinter
- Encrypted log files with Fernet symmetric encryption
- Displays typing statistics like typing speed and most-used keys
- Options to start, stop, save, clear logs, and view stats

## 🖥️ Installation

1. Clone the repository:
   git clone
   
   ```bash
   cd ethical-keylogger
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

**`requirements.txt`**
```
tkinter
pynput
cryptography
```

3. Run the application:
   ```bash
   python keylogger.py
   ```

## 🧩 Usage

- **Start Logging**: Begin keylogging with timestamped logs displayed in the text area.
- **Stop Logging**: Stop keylogging.
- **Save Logs**: Save encrypted logs to a file.
- **Show Stats**: Display typing speed and most frequently used keys.
- **Clear Logs**: Clear the current logs.
- **Exit**: Close the application.

## 📂 Log File Encryption
The application uses `cryptography.Fernet` for encrypting log files.
- A key file (`key.key`) is generated in the working directory on the first run.
- Encrypted logs are stored as binary files and can only be decrypted with the generated key.

## 📊 Sample Output
```
2024-02-15 10:23:01 - H
2024-02-15 10:23:02 - e
2024-02-15 10:23:03 - l
2024-02-15 10:23:04 - l
2024-02-15 10:23:05 - o
```

## ⚠️ Legal Warning
Misuse of this tool is strictly prohibited. The developer does not assume responsibility for any malicious use.

Happy Ethical Learning! 🛡️

