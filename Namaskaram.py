import datetime
import random

def greetMe(speak):
    hour = datetime.datetime.now().hour

    morning_quotes = [
        "Good Morning, sir.",
        "Top of the morning to you, sir.",
        "Another glorious morning, sir. Shall we get to work?",
        "Good Morning. A brilliant day for a brilliant mind."
    ]

    afternoon_quotes = [
        "Good Afternoon, sir.",
        "Pleasant afternoon. Ready to commence operations.",
        "Hope your day has been productive, sir."
    ]

    evening_quotes = [
        "Good Evening, sir.",
        "Evening, sir. You’ve had quite the day.",
        "Systems online. Ready to assist."
    ]

    jarvis_quotes = [
        "Sir, I am the interface between you and the machine.",
        "I’ve accessed all systems. We are operational.",
        "I await your command. Fully charged and at your service."
    ]

    if hour < 12:
        speak(random.choice(morning_quotes))
    elif hour < 16:
        speak(random.choice(afternoon_quotes))
    else:
        speak(random.choice(evening_quotes))

    speak(random.choice(jarvis_quotes))
