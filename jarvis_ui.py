import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading
import sys
import os
import datetime
from PIL import Image, ImageTk

from Jarvis_main import run_jarvis
import psutil

class RedirectStdout:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.config(state='normal')
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)
        self.text_widget.config(state='disabled')

    def flush(self):
        pass


def launch_jarvis():
    threading.Thread(target=run_jarvis, daemon=True).start()

# Clock Updater
def update_clock(time_label, date_label):
    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p")
    date_str = now.strftime("%A, %d %B %Y")

    time_label.config(text=time_str)
    date_label.config(text=date_str)

    time_label.after(1000, update_clock, time_label, date_label)

# System Text File Monitoring
def update_panel_from_files(alarm_label, timer_label, reminder_label):
    try:
        with open("alarm.txt", "r") as f:
            alarm_label.config(text="Alarm: " + f.read().strip())
    except:
        alarm_label.config(text="Alarm: None")

    try:
        with open("Timertext.txt", "r") as f:
            timer_label.config(text="Timer: " + f.read().strip())
    except:
        timer_label.config(text="Timer: Not Running")

    try:
        with open("reminder.txt", "r") as f:
            reminder_label.config(text="Reminder: " + f.read().strip())
    except:
        reminder_label.config(text="Reminder: --")

    alarm_label.after(1000, update_panel_from_files, alarm_label, timer_label, reminder_label)

# Battery + RAM Monitor
def update_system_info(battery_label, ram_label):
    # RAM usage
    ram = psutil.virtual_memory().percent

    # Battery info
    battery = psutil.sensors_battery()
    if battery:
        battery_text = f"{battery.percent:.1f}%"
        if battery.power_plugged:
            battery_text += " (Charging)"
    else:
        battery_text = "N/A"

    battery_label.config(text=f"Battery: {battery_text}")
    ram_label.config(text=f"RAM Usage: {ram:.1f}%")

    battery_label.after(1000, update_system_info, battery_label, ram_label)

def update_todo_info(count_label, next_label):
    todo_file = "todo_list.txt"
    if os.path.exists(todo_file):
        with open(todo_file, "r", encoding="utf-8") as f:
            tasks = [line.strip() for line in f.readlines() if line.strip()]
        if tasks:
            count_label.config(text=f"Tasks: {len(tasks)}")
            next_label.config(text=f"Next Task: {tasks[0]}")
        else:
            count_label.config(text="Tasks: 0")
            next_label.config(text="Next Task: --")
    else:
        count_label.config(text="Tasks: --")
        next_label.config(text="Next Task: --")

    # Repeat every second
    count_label.after(1000, update_todo_info, count_label, next_label)


# MAIN GUI
def main():
    root = tk.Tk()
    root.title("JARVIS Assistant UI")
    root.state('zoomed')
    root.minsize(850, 500)
    root.resizable(True, True)

    # Header
    header_frame = tk.Frame(root, bg="#1f1f1f", height=100)
    header_frame.pack(fill=tk.X)
    header_frame.pack_propagate(False)

    logo_img = Image.open("logo.jpg")
    try:
        resample = Image.Resampling.LANCZOS
    except AttributeError:
        resample = Image.LANCZOS
    logo_img = logo_img.resize((80, 80), resample)
    logo_photo = ImageTk.PhotoImage(logo_img)

    logo_label = tk.Label(header_frame, image=logo_photo, bg="#1f1f1f")
    logo_label.image = logo_photo
    logo_label.pack(side=tk.LEFT, padx=20, pady=10)

    header_label = tk.Label(
        header_frame,
        text="JARVIS AI INTERFACE",
        bg="#1f1f1f",
        fg="cyan",
        font=("Segoe UI", 26, "bold")
    )
    header_label.pack(side=tk.LEFT, padx=20, pady=10)

    clock_frame = tk.Frame(header_frame, bg="#1f1f1f")
    clock_frame.pack(side=tk.RIGHT, padx=20, pady=10)

    time_label = tk.Label(clock_frame, text="", font=("Segoe UI", 22, "bold"), fg="white", bg="#1f1f1f")
    time_label.pack(anchor="e")

    date_label = tk.Label(clock_frame, text="", font=("Segoe UI", 11), fg="gray", bg="#1f1f1f")
    date_label.pack(anchor="e")

    update_clock(time_label, date_label)

    # Right System Panel
    info_frame = tk.Frame(root, bg="#2a2a2a", width=250)
    info_frame.pack(side=tk.RIGHT, fill=tk.Y)
    info_frame.pack_propagate(False)

    tk.Label(info_frame, text="System Panel", bg="#2a2a2a", fg="cyan", font=("Segoe UI", 14, "bold")).pack(pady=10)

    alarm_label = tk.Label(info_frame, text="Alarm: None", bg="#2a2a2a", fg="white", font=("Segoe UI", 10), anchor='w', justify='left')
    alarm_label.pack(fill=tk.X, padx=10)

    timer_label = tk.Label(info_frame, text="Timer: Not Running", bg="#2a2a2a", fg="white", font=("Segoe UI", 10), anchor='w', justify='left')
    timer_label.pack(fill=tk.X, padx=10, pady=10)

    reminder_label = tk.Label(info_frame, text="Reminder: --", bg="#2a2a2a", fg="white", font=("Segoe UI", 10), wraplength=220, justify="left")
    reminder_label.pack(fill=tk.X, padx=10)

    tk.Label(info_frame, text=" ", bg="#2a2a2a").pack(pady=5)

    # --- To-Do Labels ---
    todo_count_label = tk.Label(info_frame, text="Tasks: --", bg="#2a2a2a", fg="white", font=("Segoe UI", 10))
    todo_count_label.pack(fill=tk.X, padx=10)

    todo_next_label = tk.Label(info_frame, text="Next Task: --", bg="#2a2a2a", fg="white", font=("Segoe UI", 10), wraplength=220, justify="left")
    todo_next_label.pack(fill=tk.X, padx=10, pady=(0, 10))

    # System Usage
    tk.Label(info_frame, text="System Usage", bg="#2a2a2a", fg="cyan", font=("Segoe UI", 14, "bold")).pack(pady=(20, 5))

    battery_label = tk.Label(info_frame, text="Battery: --", bg="#2a2a2a", fg="white", font=("Segoe UI", 10))
    battery_label.pack(fill=tk.X, padx=10)

    ram_label = tk.Label(info_frame, text="RAM Usage: --", bg="#2a2a2a", fg="white", font=("Segoe UI", 10))
    ram_label.pack(fill=tk.X, padx=10)

    update_panel_from_files(alarm_label, timer_label, reminder_label)
    update_system_info(battery_label, ram_label)
    update_todo_info(todo_count_label, todo_next_label)


    # Console Output (Left)
    text_console = ScrolledText(root, wrap=tk.WORD, font=("Consolas", 11), bg="black", fg="lime")
    text_console.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    text_console.config(state='disabled')

    sys.stdout = RedirectStdout(text_console)
    launch_jarvis()

    root.mainloop()

if __name__ == "__main__":
    main()
