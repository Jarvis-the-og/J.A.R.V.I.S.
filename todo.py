# todo.py
import os
from gtts import gTTS
from playsound import playsound

todo_file = "todo_list.txt"

def speak(text):
    try:
        filename = "todo_voice.mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("Error in speak():", e)

def add_task(task):
    with open(todo_file, "a", encoding="utf-8") as file:
        file.write(task.strip() + "\n")
    speak("Noted down, sir.")

def read_tasks():
    if not os.path.exists(todo_file):
        speak("There is nothing on your list yet.")
        print("[No tasks found]")
        return

    with open(todo_file, "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file.readlines() if line.strip()]

    if not tasks:
        speak("There is nothing on your list, sir.")
        print("[Your to-do list is empty]")
        return

    speak(f"You have {len(tasks)} tasks for today. Here they are:")
    for idx, task in enumerate(tasks, start=1):
        speak(f"Task {idx}: {task}")
        print(f"{idx}. {task}")

import inflect
p = inflect.engine()

def word_to_digit(text):
    """Convert a number word like 'one' to digit '1'"""
    try:
        return str(p.number_to_words(text, wantlist=True)[0])
    except:
        return text

def mark_done(task_identifier):
    if not os.path.exists(todo_file):
        speak("No tasks found to mark as done.")
        return

    with open(todo_file, "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file.readlines() if line.strip()]

    original_tasks = tasks.copy()
    task_identifier_clean = task_identifier.lower().replace("jarvis", "").replace("is done", "").replace("done", "").strip()

    # Convert number words like "one" to digits
    spoken_numbers = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
        "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"
    }
    if task_identifier_clean in spoken_numbers:
        task_identifier_clean = spoken_numbers[task_identifier_clean]

    # If it's a digit index
    if task_identifier_clean.isdigit():
        task_index = int(task_identifier_clean) - 1
        if 0 <= task_index < len(tasks):
            done_task = tasks.pop(task_index)
        else:
            speak("That task number does not exist.")
            return
    else:
        # Try fuzzy match on task string (case-insensitive)
        found = False
        for task in tasks:
            if task_identifier_clean in task.lower():
                done_task = task
                tasks.remove(task)
                found = True
                break
        if not found:
            speak("I couldn't find that task.")
            return

    with open(todo_file, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

    speak(f"Marked as done: {done_task}")
    print(f"Done: {done_task}")