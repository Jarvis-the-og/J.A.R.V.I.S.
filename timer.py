import threading
import time
import re
import tempfile
import os
import datetime
from gtts import gTTS
import pygame

# === Global setup ===
pygame.mixer.init()
cancel_event = threading.Event()
current_timer_thread = None
TIMER_FILE = "Timertext.txt"  # <- Logging file for UI

# === TTS Speak Function ===
def speak(text, wait=False):
    def _play_audio():
        try:
            tts = gTTS(text=text, lang='en')
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                temp_path = fp.name
            tts.save(temp_path)
            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                if cancel_event.is_set():
                    pygame.mixer.music.stop()
                    break
                time.sleep(0.1)
            os.remove(temp_path)
        except Exception as e:
            print(f"Error in speak(): {e}")

    if wait:
        _play_audio()
    else:
        t = threading.Thread(target=_play_audio)
        t.start()

# === Convert voice input to total seconds ===
def voice_to_seconds(text):
    text = text.lower()
    minutes = 0
    seconds = 0
    pattern = re.compile(r'(\d+)\s*(minute|minutes|second|seconds)')
    matches = pattern.findall(text)

    for value, unit in matches:
        val = int(value)
        if 'minute' in unit:
            minutes += val
        elif 'second' in unit:
            seconds += val

    if not matches:
        digits = re.findall(r'\d+', text)
        if digits:
            seconds = int(digits[0])
        else:
            return None

    return minutes * 60 + seconds

# === Start Timer ===
def start_timer(seconds):
    global current_timer_thread, cancel_event
    if seconds is None or seconds <= 0:
        speak("Invalid timer duration.")
        return False

    cancel_event.clear()

    def timer_thread(duration):
        speak(f"Timer set for {duration // 60} minutes and {duration % 60} seconds, sir.")

        remaining = duration
        while remaining > 0:
            if cancel_event.is_set():
                speak("Timer was cancelled, sir.", wait=True)
                _clear_timer_file()
                return
            _log_timer(remaining)
            time.sleep(1)
            remaining -= 1

        _clear_timer_file()
        speak("Timer finished, sir.", wait=True)
        now = datetime.datetime.now()
        current_time_str = now.strftime("The time now is %I:%M %p")
        speak(current_time_str, wait=True)

        # Play timer.mp3 if not cancelled
        if not cancel_event.is_set():
            try:
                pygame.mixer.music.load("timer.mp3")  # Ensure this file exists
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    if cancel_event.is_set():
                        pygame.mixer.music.stop()
                        break
                    time.sleep(0.1)
            except Exception as e:
                print(f"Error playing timer.mp3: {e}")

    current_timer_thread = threading.Thread(target=timer_thread, args=(seconds,))
    current_timer_thread.start()
    return True

# === Cancel Timer ===
def cancel_timer():
    global cancel_event, current_timer_thread
    if current_timer_thread and current_timer_thread.is_alive():
        cancel_event.set()
        pygame.mixer.music.stop()
        _clear_timer_file()
        return True
    return False

# === Logging to Timertext.txt ===
def _log_timer(seconds_left):
    mins = seconds_left // 60
    secs = seconds_left % 60
    status = f"Timer running: \n {mins:02d}:{secs:02d} remaining"
    with open(TIMER_FILE, "w") as f:
        f.write(status)

def _clear_timer_file():
    with open(TIMER_FILE, "w") as f:
        f.write("None")

# === Terminal Interaction (for testing) ===
if __name__ == "__main__":
    while True:
        cmd = input("Command (set/cancel/exit): ").strip().lower()
        if cmd == "set":
            test_input = input("Enter timer duration (e.g. '2 minutes 30 seconds'): ")
            secs = voice_to_seconds(test_input)
            if secs:
                start_timer(secs)
            else:
                print("Could not parse the duration.")
        elif cmd == "cancel":
            if cancel_timer():
                print("Timer cancelled.")
            else:
                print("No active timer to cancel.")
        elif cmd == "exit":
            break
        else:
            print("Unknown command.")
