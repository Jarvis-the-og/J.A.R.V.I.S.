import os
import webbrowser
import pyautogui
import pyttsx3
from time import sleep

# Initialize TTS engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# App dictionary with common synonyms
dictapp = {
    "commandprompt": "cmd",
    "cmd": "cmd",
    "paint": "paint",
    "word": "winword",
    "microsoft word": "winword",
    "excel": "excel",
    "microsoft excel": "excel",
    "chrome": "chrome",
    "googlechrome": "chrome",
    "vscode": "code",
    "visualstudiocode": "code",
    "powerpoint": "powerpnt",
    "microsoftpowerpoint": "powerpnt",
    "whatsapp": "whatsapp",
    "cmd": "cmd",
    "command prompt": "cmd",
    "powershell": "powershell",
    "windows powershell": "powershell",
    "terminal": "cmd",
    "taskmanager": "taskmgr",
    "task manager": "taskmgr",
    "controlpanel": "control",
    "control panel": "control",
    "registry": "regedit",
    "registryeditor": "regedit",
    "systeminfo": "msinfo32",
    "system information": "msinfo32",
    "calculator": "calc",
    "calc": "calc",
    "notepad": "notepad",
    "charactermap": "charmap",
    "character map": "charmap",
    "systemconfiguration": "msconfig",
    "msconfig": "msconfig",
    "snippingtool": "snippingtool",
    "snipping tool": "snippingtool",
    "snip and sketch": "snippingtool",  # legacy name
    "wordpad": "wordpad",
    "windows media player": "wmplayer",
    "media player": "wmplayer",
    "file explorer": "explorer",
    "explorer": "explorer",
    "device manager": "devmgmt.msc",
    "event viewer": "eventvwr",
    "services": "services.msc",
    "disk management": "diskmgmt.msc",
    "task scheduler": "taskschd.msc",
    "resource monitor": "resmon",
    "performance monitor": "perfmon",
    "edge": "msedge",
    "microsoft edge": "msedge"
}

def openAppWeb(query):
    speak("Launching sir...")
    query = query.lower()

    # Remove filler phrases
    fillers = ["open", "launch", "jarvis", "please", "could you", "can you", "start", "run"]
    for word in fillers:
        query = query.replace(word, "")
    query = query.strip()

    # Handle website opening
    if any(ext in query for ext in [".com", ".co.in", ".ai", ".org", ".in"]):
        webbrowser.open(f"https://www.{query}")
        return

    # Handle application launching
    for app in dictapp:
        if app in query:
            os.system(f"start {dictapp[app]}")
            return

    speak("Sorry, I couldn't find the application.")

def closeAppWeb(query):
    speak("Initiating closure sir. Please wait...")
    query = query.lower()

    # Handle tab closures
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        return
    elif "two tab" in query or "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All requested tabs have been closed")
        return

    # Handle application termination
    for app in dictapp:
        if app in query:
            os.system(f"taskkill /f /im {dictapp[app]}.exe")
            return

    speak("Sorry, I couldn't identify what to close.")
