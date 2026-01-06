import random
import webbrowser
import requests
import time
import subprocess
import sys
import warnings
from bs4 import GuessedAtParserWarning
warnings.filterwarnings("ignore", category=GuessedAtParserWarning)
import speech_recognition
import pywhatkit
import wikipedia
import pygetwindow as gw
import pyautogui
from bs4 import BeautifulSoup


# ---------- TTS BRIDGE ----------
def speak(text):
    subprocess.run(
        [sys.executable, "tts.py", text],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


# ---------- VOICE INPUT ----------
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 250
        audio = r.listen(source, 0, 6)

    try:
        print("Understanding and Processing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
        return query.lower()

    except Exception:
        unclear_responses = [
        "Pardon me, sir, I didn’t quite catch that.",
        "Could you please repeat that, sir?",
        "I’m afraid I missed that, sir. Care to try again?",
        "My apologies, sir. Your last command wasn’t clear.",
        "I'm listening, sir — would you mind saying that again?",
        "Signal lost on that one, sir. Could you say it once more?",
        "Audio unclear, sir. Requesting repeat input.",
        "Processing failed — awaiting clearer instructions, sir.",
        "Your voice didn’t register properly. Try again, sir?",
        "That input didn’t compute, sir. Please restate your command.",
        "My circuits must’ve blinked. Mind repeating that, sir?",
        "That went right past my audio sensors, sir.",
        "Even perfection has blind spots — could you say that again?",
        "Oops, auditory static! Say that one more time, sir?",
        "I detected a voice but not the meaning. Retry, sir?"
        ]
        speak(random.choice(unclear_responses))
        return "none"


# ---------- GOOGLE SEARCH ----------
def searchGoogle(query):
    if "google" not in query:
        return

    fillers = [
        "open", "launch", "jarvis", "please", "could you",
        "can you", "start", "google search", "google", "search"
    ]

    for word in fillers:
        query = query.replace(word, "")

    query = query.strip()
    if not query:
        speak("Please specify what you want to search on Google.")
        return

    speak("These are the results which I found on the web")

    try:
        pywhatkit.search(query)
        summary = wikipedia.summary(query, sentences=1)
        speak(summary)

    except Exception:
        responses = [
            "I am still learning. Currently this is beyond my domain.",
            "Apologies, but I haven't mastered that yet.",
            "I'm not trained for this task at the moment.",
            "That's outside my current knowledge base, but I'll get there soon."
        ]
        speak(random.choice(responses))


# ---------- YOUTUBE ----------
def focus_youtube_window():
    for window in gw.getWindowsWithTitle("YouTube"):
        if window.isMinimized:
            window.restore()
        window.activate()
        time.sleep(1)
        return True
    return False


def searchYoutube(query):
    speak("Searching YouTube")

    for word in ["jarvis", "youtube search", "youtube", "play"]:
        query = query.replace(word, "")

    query = query.strip()
    if not query:
        speak("Please tell me what to search on YouTube.")
        return

    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    try:
        pywhatkit.playonyt(query)
        speak("Here is your video.")
    except Exception:
        speak("Something went wrong while opening YouTube.")


# ---------- WIKIPEDIA ----------
def searchWikipedia(query):
    if "wikipedia" not in query:
        return

    speak("Searching Wikipedia")

    for word in ["jarvis", "wikipedia search", "wikipedia"]:
        query = query.replace(word, "")

    query = query.strip()
    if not query:
        speak("Please specify what you want to search on Wikipedia.")
        return

    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        print(results)

    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"I found multiple results. Here's information about {e.options[0]}")
        speak(wikipedia.summary(e.options[0], sentences=2))

    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any Wikipedia page for that topic.")

    except Exception:
        speak("Something went wrong while accessing Wikipedia.")
