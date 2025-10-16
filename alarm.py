import datetime
import os
import time
from gtts import gTTS
from playsound import playsound
import sys

alarm_input_time = sys.argv[1] if len(sys.argv) > 1 else None
ALARM_FILE = "alarm.txt"

def speak(text):
    try:
        filename = "alarm_speech.mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("Error in speak():", e)

def voice_to_time(text):
    text = text.lower().replace("oh", "0").replace("zero", "0")
    text = text.replace(".", "").replace("  ", " ").replace(":", "").replace("p m", "pm").replace("a m", "am").replace(" ", "")
    
    word_to_num = {
        "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8",
        "nine": "9", "ten": "10", "eleven": "11", "twelve": "12",
        "thirteen": "13", "fourteen": "14", "fifteen": "15",
        "sixteen": "16", "seventeen": "17", "eighteen": "18",
        "nineteen": "19", "twenty": "20", "thirty": "30",
        "forty": "40", "fifty": "50"
    }

    for word, num in word_to_num.items():
        text = text.replace(word, num)

    # Check for AM/PM suffix
    if "am" in text or "pm" in text:
        try:
            time_part = text.replace("am", "").replace("pm", "")
            hour = time_part[:-2] if len(time_part) > 3 else time_part[0]
            minute = time_part[-2:]
            ampm = "AM" if "am" in text else "PM"
            in_time = datetime.datetime.strptime(f"{hour}:{minute} {ampm}", "%I:%M %p")
            return in_time.strftime("%H:%M")
        except:
            return None

    # Fallback for pure HHMM 24-hour input
    if len(text) == 4:
        hh, mm = text[:2], text[2:]
    elif len(text) == 3:
        hh, mm = "0" + text[0], text[1:]
    else:
        return None

    if hh.isdigit() and mm.isdigit() and 0 <= int(hh) <= 23 and 0 <= int(mm) <= 59:
        return f"{hh}:{mm}"
    return None

def setAlarm(time_str):
    """Set alarm in HH:MM 24-hour format"""
    alarm_time = alarm_input_time.strip()

    # Write to alarm.txt
    with open(ALARM_FILE, "w") as f:
        f.write(alarm_time)

    speak(f"Alarm set for {alarm_time}, sir.")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            speak("It's time, sir! The time is now " + alarm_time)
            os.startfile("uddgaye.mp3")  # Replace with your actual alarm file path

            # Reset alarm.txt
            with open(ALARM_FILE, "w") as f:
                f.write("None")
            break

        time.sleep(10)

if __name__ == "__main__":
    if alarm_input_time:
        setAlarm(alarm_input_time)
    else:
        print("No alarm time passed.")
