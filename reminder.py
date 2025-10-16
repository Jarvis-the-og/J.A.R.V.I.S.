import datetime
import os
import time
from gtts import gTTS
from playsound import playsound
import sys
import random

reminder_time = sys.argv[1] if len(sys.argv) > 1 else None
reminder_message = sys.argv[2] if len(sys.argv) > 2 else "You have a reminder."
REMINDER_FILE = "reminder.txt"

def speak(text):
    try:
        filename = "reminder_audio.mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("Error in speak():", e)

def announce_reminder(message, reminder_time):
    responses = [
        f"It's {reminder_time}, sir. I would like to alert you to {message}.",
        f"Apologies for the interruption, but it's {reminder_time} and you need to {message}.",
        f"As per your request, sir, I would like to remind you to {message}.",
        f"Gentle nudge at {reminder_time}. You asked me to remind you to {message}.",
        f"Sir, this is a timely alert to {message}. The time is {reminder_time}",
        f"Your scheduled reminder just kicked in. Please {message}. It's {reminder_time} already.",
        f"Pardon the disturbance, but it’s time for you to {message} since it is {reminder_time}.",
    ]
    speak(random.choice(responses))

def setReminder(time_str, message):
    # Write to reminder.txt
    with open(REMINDER_FILE, "w") as f:
        f.write(f"{time_str} - {message}")

    speak(f"Reminder set for {time_str} to {message}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == time_str:
            announce_reminder(message, current_time)

            # Clear the file after alert
            with open(REMINDER_FILE, "w") as f:
                f.write("None")
            break
        time.sleep(10)

if __name__ == "__main__":
    if reminder_time:
        setReminder(reminder_time, reminder_message)
    else:
        print("Reminder time or message not provided.")
