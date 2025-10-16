import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
import datetime
import random

def greetMe():
    hour = int(datetime.datetime.now().hour)

    morning_quotes = [
        "Good Morning, sir.",
        "Top of the morning to you, sir.",
        "Another glorious morning, sir. Shall we get to work?",
        "Good Morning. ‘A brilliant day for a brilliant mind.’"
    ]

    afternoon_quotes = [
        "Good Afternoon, sir.",
        "Pleasant afternoon. Ready to commence operations.",
        "Hope your day has been productive, sir.",
        "Afternoon check-in, sir. Shall we proceed?"
    ]

    evening_quotes = [
        "Good Evening, sir.",
        "Evening, sir. You’ve had quite the day.",
        "Systems online. Ready to assist, even at this hour.",
        "As Tony Stark once said, 'Sometimes you gotta run before you can walk.' Good evening, sir."
    ]

    jarvis_quotes = [
        "Sir, I am the interface. Between you and the machine.",
        "A pleasure to see you again, sir. Initiating all protocols.",
        "I’ve accessed all systems. We are operational.",
        "I’m just a rather very intelligent system, sir.",
        "I’m afraid I can’t do that… just kidding. Ready when you are, sir.",
        "I await your command. Fully charged and at your service."
    ]

    # Greeting based on time
    if 0 <= hour < 12:
        speak(random.choice(morning_quotes))
    elif 12 <= hour < 16:
        speak(random.choice(afternoon_quotes))
    else:
        speak(random.choice(evening_quotes))

    # Follow-up Jarvis-style messages
    speak(random.choice(jarvis_quotes))
