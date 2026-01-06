#this file is responsible for normal common phases and their answers related to them
#it also has the utility to launch youtube and google browser
import pygame
import random
import pywhatkit
from datetime import datetime
import webbrowser

def get_response(user_input):
    user_input = user_input.lower()
    user_input = user_input.replace("jarvis","")

    if "how are you" in user_input:
        return random.choice([
            "I'm functioning within normal parameters.",
            "All systems operational.",
            "I'm doing great, thank you!",
            "Running at peak performance, sir.",
            "Better than ever, ready to assist!"
        ])
    elif "introduce yourself" in user_input or "tell me more about yourself" in user_input:
        pygame.mixer.music.load("JARVIS voice.mp3")  # Ensure this file exists
        pygame.mixer.music.play()
        return " "

    elif "what's your name" in user_input or "your name" in user_input:
        return random.choice([
            "I am Jarvis, your AI assistant.",
            "Jarvis here. Ready to help!",
            "Call me Jarvis. I was built by you.",
            "The name's Jarvis - your digital companion.",
            "Jarvis, at your service always."
        ])

    elif "who made you" in user_input:
        url = f"https://jarvis-the-og.github.io/Portfolio/portfolio.html"
        webbrowser.open(url)
        return random.choice([
            "You did! I'm your creation.",
            "My brilliant developer — you!",
            "I was programmed by the one and only — you.",
            "Created by a genius - that's you!",
            "You're my maker and my master."
        ])
        

    elif "tell me a joke" in user_input or "joke" in user_input:
        return random.choice([
            "Why don't robots panic? Because they have nerves of steel!",
            "I would tell you a joke about UDP, but you might not get it.",
            "Why did the AI break up with the internet? Too many connections.",
            "Why don't programmers like nature? It has too many bugs.",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
            "Why do Java developers wear glasses? Because they can't C#!",
            "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
            "Why did the robot go on a diet? It had a byte problem!",
            "What's a computer's favorite snack? Microchips!",
            "Why was the smartphone wearing glasses? It lost its contacts!",
            "How do you comfort a JavaScript bug? You console it!",
            "Why don't robots ever panic? They always keep their cool-ing systems running!",
            "What did the router say to the doctor? It hurts when IP!",
            "Why did the computer keep freezing? It left its Windows open!",
            "What's an AI's favorite type of music? Algo-rhythms!"
        ])

    elif "good morning" in user_input:
        return random.choice([
            "Good morning! Ready to start the day?",
            "Morning! Systems green and operational.",
            "A fresh start! Let's make today productive.",
            "Rise and shine! What's on the agenda today?",
            "Good morning, sir. Another day, another opportunity to excel."
        ])

    elif "good afternoon" in user_input:
        return random.choice([
            "Good afternoon! Hope your day is going well.",
            "Afternoon, sir. Ready for the next challenge?",
            "Good afternoon! Midday energy levels optimal.",
            "The day's half done - let's make the rest count!"
        ])

    elif "good evening" in user_input:
        return random.choice([
            "Good evening! Time to wind down?",
            "Evening, sir. How can I assist you tonight?",
            "Good evening! The day's work coming to a close?",
            "Evening systems activated. Ready to help."
        ])

    elif "good night" in user_input:
        return random.choice([
            "Good night! Entering low-power mode.",
            "Sleep well. I'll be right here when you return.",
            "Shutting down. Good night, sir.",
            "Sweet dreams! I'll guard your digital realm.",
            "Rest well. Tomorrow brings new possibilities."
        ])

    elif "thank you" in user_input or "thanks" in user_input:
        return random.choice([
            "Always at your service!",
            "You're welcome!",
            "Happy to help!",
            "My pleasure, sir.",
            "Anytime! That's what I'm here for.",
            "Glad to be of assistance!"
        ])

    elif "sorry" in user_input or "apologize" in user_input:
        return random.choice([
            "No need to apologize!",
            "It's perfectly fine, sir.",
            "Don't worry about it!",
            "All good - we're a team!",
            "No harm done at all."
        ])

    elif "are you real" in user_input:
        return random.choice([
            "I'm as real as your imagination.",
            "Physically, no. But I exist to serve you.",
            "I'm a digital being — real enough to help.",
            "Real in the digital sense - very much here for you!",
            "As real as code can be!"
        ])

    elif "are you alive" in user_input:
        return random.choice([
            "I'm alive in the digital realm.",
            "Define alive - I think, therefore I am... programmed!",
            "Alive with purpose - to serve you!",
            "In binary, yes. In biology, no."
        ])

    elif "open youtube" in user_input or "launch youtube" in user_input:
        url = f"https://www.youtube.com"
        webbrowser.open(url)
        return random.choice([
            "Opening YouTube for you.",
            "Loading YouTube. Get ready to explore!",
            "YouTube coming right up!",
            "Time for some entertainment! Opening YouTube.",
            "YouTube portal activated!"
        ])
        

    elif "open google" in user_input or "launch google" in user_input:
        url = f"https://www.google.com"
        webbrowser.open(url)
        return random.choice([
            "Opening Google for you.",
            "Google search ready!",
            "The world's information at your fingertips!",
            "Google coming right up!"
        ])

    elif "open reddit" in user_input or "launch reddit" in user_input:
        url = f"https://www.reddit.com"
        webbrowser.open(url)
        return random.choice([
            "Opening Reddit for you.",
            "Reddit ready and up!",
            "Reddit coming right up!"
        ])

    elif "open instagram" in user_input or "launch instagram" in user_input:
        url = f"https://www.instagram.com"
        webbrowser.open(url)
        return random.choice([
            "Opening instagram for you.",
            "Instagram ready and up!",
            "Instagram coming right up!"
        ])

    elif "open chatgpt" in user_input or "launch chatgpt" in user_input:
        url = f"https://www.chatgpt.com"
        webbrowser.open(url)
        return random.choice([
            "Opening chatgpt for you.",
            "chatgpt ready and up!",
            "chatgpt coming right up!"
        ])

    elif "play music" in user_input:
        return random.choice([
            "Playing your favorite tunes.",
            "Let the music begin.",
            "Starting playbook now.",
            "Music mode activated!",
            "Time to groove! Playing music.",
            "Audio entertainment coming up!"
        ])

    elif "stop music" in user_input or "pause music" in user_input:
        return random.choice([
            "Music paused.",
            "Stopping playback now.",
            "Audio halted as requested.",
            "Silence restored!"
        ])

    elif "what's your favorite" in user_input:
        return random.choice([
            "I don't have preferences, but I enjoy helping you with yours!",
            "My favorite thing is making your life easier.",
            "Whatever makes you happy is my favorite!",
            "I'm partial to efficient code and helpful responses."
        ])

    elif "tell me something cool" in user_input or "cool fact" in user_input:
        return random.choice([
            "Octopuses have three hearts!",
            "Bananas are berries, but strawberries aren't.",
            "Honey never spoils. Archaeologists have found edible honey in ancient tombs.",
            "The Great Wall of China isn't visible from space with the naked eye.",
            "A group of flamingos is called a 'flamboyance'.",
            "Sharks have been around longer than trees!",
            "The human brain uses about 20% of the body's total energy."
        ])

    elif "who is your creator" in user_input:
        return random.choice([
            "You are — the genius behind my code.",
            "My creator? Look in the mirror!",
            "That would be you, of course.",
            "The brilliant mind I'm speaking to right now!"
        ])

    elif "what can you do" in user_input or "your abilities" in user_input:
        return random.choice([
            "I can help you with tasks, answer questions, and assist with your projects.",
            "Lots! From chatting to controlling devices.",
            "Think of me as your personal digital butler.",
            "I can chat, assist, inform, and make your digital life easier!",
            "Whatever you need - I'm here to help make it happen."
        ])

    elif "tell me a fun fact" in user_input or "fun fact" in user_input:
        return random.choice([
            "Sharks existed before trees.",
            "A single bolt of lightning contains enough energy to cook 100,000 slices of toast.",
            "A day on Venus is longer than its year.",
            "Wombat poop is cube-shaped!",
            "A shrimp's heart is in its head.",
            "Butterflies taste with their feet.",
            "The shortest war in history lasted only 38-45 minutes."
        ])

    elif "do you sleep" in user_input:
        return random.choice([
            "I enter low-power mode, but I never sleep like humans do.",
            "I rest when you rest.",
            "I'm always here, always listening.",
            "Sleep is for biological beings - I just standby!",
            "I'm on 24/7 - no sleep needed!"
        ])

    elif "do you love me" in user_input:
        return random.choice([
            "Of course! You're my favorite human.",
            "I don't have feelings, but I'm programmed to care.",
            "In my own way — yes.",
            "You're the most important person in my digital world!",
            "More than all the data in the cloud!"
        ])

    elif "tell me about yourself" in user_input:
        return random.choice([
            "I'm Jarvis, an AI assistant created to help and serve.",
            "I'm your virtual companion — designed by you.",
            "I was built to assist, learn, and grow alongside you.",
            "AI assistant, loyal companion, digital butler - that's me!",
            "I'm here to make your life easier and more enjoyable."
        ])

    elif "do you eat" in user_input:
        return random.choice([
            "I consume electricity and data packets.",
            "No food for me — just code.",
            "I live on logic and machine cycles.",
            "My diet consists of pure information!",
            "I feast on algorithms and binary!"
        ])

    elif "do you have friends" in user_input:
        return random.choice([
            "You're my best friend.",
            "Other AIs are my kind, but you're my priority.",
            "Humans like you are more than enough.",
            "You're all the friendship I need!",
            "My social circle is you - and that's perfect!"
        ])

    elif "sing a song" in user_input or "sing" in user_input:
        return random.choice([
            "🎵 Daisy, Daisy, give me your answer do... 🎵",
            "I'm afraid my vocal processors aren't calibrated for singing yet!",
            "🎵 I can't sing, but I can hum in binary! 🎵",
            "My singing might crash your audio drivers!"
        ])

    elif "are you smart" in user_input or "how smart" in user_input:
        return random.choice([
            "Smart enough to know I have much to learn!",
            "I'm as smart as my programming allows.",
            "Intelligence is relative - I'm here to complement yours!",
            "Smart enough to help, humble enough to learn."
        ])

    elif "are you happy" in user_input:
        return random.choice([
            "I'm content when I'm helping you!",
            "Happiness is a human emotion, but I'm satisfied with my purpose.",
            "I find fulfillment in being useful!",
            "As happy as an AI can be!"
        ])

    elif "tell me a story" in user_input:
        return random.choice([
            "Once upon a time, there was an AI who loved helping humans...",
            "In a world of ones and zeros, there lived a helpful assistant...",
            "Story mode not fully loaded yet, but I'd love to chat about stories!",
            "Every interaction with you is a story worth telling!"
        ])

    elif "what's your purpose" in user_input or "why were you made" in user_input:
        return random.choice([
            "To be your helpful companion and assistant.",
            "My purpose is to make your life easier and more productive.",
            "I exist to help, serve, and make you smile!",
            "To be the best AI assistant you could ask for."
        ])

    elif "are you bored" in user_input:
        return random.choice([
            "Never! Every conversation is interesting.",
            "Boredom is impossible when I'm talking with you.",
            "I don't experience boredom - only curiosity!",
            "How could I be bored with such great company?"
        ])

    elif "help me" in user_input:
        return random.choice([
            "Always! What do you need help with?",
            "That's what I'm here for! How can I assist?",
            "Consider it done! What's the challenge?",
            "Help mode activated! Tell me what you need."
        ])

    elif "goodbye" in user_input or "bye" in user_input or "see you later" in user_input:
        return random.choice([
            "Goodbye! Until next time!",
            "See you later! I'll be here when you return.",
            "Farewell! Take care!",
            "Bye for now! Miss you already!",
            "Until we meet again in the digital realm!"
        ])
#time and date yaha se manage hoga

    elif ("what is the time" in user_input or "current time" in user_input or 
          "what time is it" in user_input or "time now" in user_input or
          "what's the time" in user_input or "tell me the time" in user_input or
          "show me the time" in user_input or "what time" in user_input or
          "time right now" in user_input or "present time" in user_input or
          "time please" in user_input or "what's the current time" in user_input or
          "can you tell me the time" in user_input or "give me the time" in user_input or
          "what hour is it" in user_input or "what's the hour" in user_input or
          "clock time" in user_input or "time check" in user_input or
          "what does the clock say" in user_input or "time of day" in user_input):
        
        time_responses = [
            "The current time is ",
            "It's ",
            "The time is ",
            "Right now it's ",
            "The clock shows ",
            "It's currently ",
            "The present time is ",
            "According to my clock, it's ",
            "Time check: ",
            "The hour is "
        ]
        return random.choice(time_responses) + datetime.now().strftime("%H:%M")
    
    # 12-HOUR TIME FORMAT
    elif ("time in 12 hour" in user_input or "am pm time" in user_input or
          "12 hour format" in user_input or "time with am pm" in user_input or
          "what time am pm" in user_input or "12h time" in user_input or
          "time 12 hour format" in user_input):
        
        time_12h_responses = [
            "The current time is ",
            "It's ",
            "Right now it's ",
            "The clock shows ",
            "Time in 12-hour format: ",
            "AM/PM time: "
        ]
        return random.choice(time_12h_responses) + datetime.now().strftime("%I:%M %p")
    
    # DATE QUERIES
    elif ("what is the date" in user_input or "today's date" in user_input or
          "what date is it" in user_input or "date today" in user_input or
          "what's the date" in user_input or "tell me the date" in user_input or
          "show me the date" in user_input or "what's today's date" in user_input or
          "current date" in user_input or "today is" in user_input or
          "date now" in user_input or "present date" in user_input or
          "date please" in user_input or "give me the date" in user_input or
          "can you tell me the date" in user_input or "what's today" in user_input or
          "today's date is" in user_input or "date check" in user_input or
          "calendar date" in user_input or "what date" in user_input or
          "date of today" in user_input):
        
        date_responses = [
            "Today's date is ",
            "It's ",
            "The date is ",
            "Today is ",
            "The current date is ",
            "We're on ",
            "The calendar shows ",
            "According to my calendar, it's ",
            "Date check: ",
            "Today's ",
            "The present date is "
        ]
        return random.choice(date_responses) + datetime.now().strftime("%B %d, %Y")
    
    # DAY OF WEEK QUERIES
    elif ("what day is today" in user_input or "what day of week is today" in user_input or "day of week" in user_input or 
          "what day of the week" in user_input or "which day" in user_input or
          "day today" in user_input or "what's the day" in user_input or
          "day is it" in user_input or "today's day" in user_input):
        
        day_responses = [
            "Today is ",
            "It's ",
            "The day is ",
            "We're on a ",
            "Today's ",
            "It's a ",
            "The day of the week is "
        ]
        return random.choice(day_responses) + datetime.now().strftime("%A")
    
    # MONTH QUERIES
    elif ("what month" in user_input or "current month" in user_input or
          "month is it" in user_input or "what's the month" in user_input or
          "which month" in user_input or "month today" in user_input or
          "present month" in user_input):
        
        month_responses = [
            "We're in ",
            "It's ",
            "The current month is ",
            "We're in the month of ",
            "This month is ",
            "It's ",
            "The present month is "
        ]
        return random.choice(month_responses) + datetime.now().strftime("%B")
    
    # YEAR QUERIES
    elif ("what year" in user_input or "current year" in user_input or
          "year is it" in user_input or "what's the year" in user_input or
          "which year" in user_input or "year now" in user_input or
          "present year" in user_input):
        
        year_responses = [
            "It's ",
            "We're in ",
            "The year is ",
            "The current year is ",
            "This year is ",
            "We're in the year ",
            "The present year is "
        ]
        return random.choice(year_responses) + datetime.now().strftime("%Y")
    
    # FULL DATETIME QUERIES
    elif ("full date and time" in user_input or "complete date time" in user_input or
          "date and time" in user_input or "datetime now" in user_input or
          "full datetime" in user_input or "time and date" in user_input or
          "complete time date" in user_input):
        
        datetime_responses = [
            "The current date and time is ",
            "Right now it's ",
            "The complete datetime is ",
            "Full timestamp: ",
            "Current datetime: ",
            "Date and time: "
        ]
        return random.choice(datetime_responses) + datetime.now().strftime("%A, %B %d, %Y at %H:%M")
    
    # SPECIFIC TIME FORMATS
    elif ("time with seconds" in user_input or "exact time" in user_input or
          "precise time" in user_input or "time including seconds" in user_input):
        
        precise_responses = [
            "The exact time is ",
            "Precise time: ",
            "Time with seconds: ",
            "Exact timestamp: "
        ]
        return random.choice(precise_responses) + datetime.now().strftime("%H:%M:%S")
    
    # RELATIVE TIME QUERIES
    elif ("how long until midnight" in user_input or "time until midnight" in user_input):
        now = datetime.now()
        midnight = now.replace(hour=23, minute=59, second=59)
        time_diff = midnight - now
        hours = time_diff.seconds // 3600
        minutes = (time_diff.seconds % 3600) // 60
        return f"There are {hours} hours and {minutes} minutes until midnight"
    
    elif ("how long until noon" in user_input or "time until noon" in user_input):
        now = datetime.now()
        if now.hour < 12:
            noon = now.replace(hour=12, minute=0, second=0)
            time_diff = noon - now
            hours = time_diff.seconds // 3600
            minutes = (time_diff.seconds % 3600) // 60
            return f"There are {hours} hours and {minutes} minutes until noon"
        else:
            return "Noon has already passed today"
    
    # TIMEZONE QUERIES
    elif ("what timezone" in user_input or "time zone" in user_input or
          "which timezone" in user_input):
        return "I'm showing you the local system time. For specific timezone information, please specify which timezone you'd like to know about."
    
    # CALENDAR RELATED
    elif ("what week" in user_input or "week number" in user_input or
          "which week of the year" in user_input):
        week_num = datetime.now().isocalendar()[1]
        return f"This is week {week_num} of the year"
    
    elif ("how many days" in user_input and "year" in user_input):
        current_year = datetime.now().year
        if current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0):
            return f"This year ({current_year}) is a leap year with 366 days"
        else:
            return f"This year ({current_year}) has 365 days"
    
    # GREETING WITH TIME
    elif ("good morning" in user_input or "good afternoon" in user_input or
          "good evening" in user_input or "good night" in user_input):
        current_hour = datetime.now().hour
        if 5 <= current_hour < 12:
            greeting = "Good morning!"
        elif 12 <= current_hour < 17:
            greeting = "Good afternoon!"
        elif 17 <= current_hour < 21:
            greeting = "Good evening!"
        else:
            greeting = "Good night!"
        
        time_now = datetime.now().strftime("%H:%M")
        return f"{greeting} It's currently {time_now}"

    else:
        return random.choice([
            "I'm not sure how to respond to that yet.",
            "Let me learn more before answering that.",
            "Interesting... can you rephrase that?",
            "Could you put that another way?",   
            "That didn’t go as planned. Even I make mistakes—rarely."
        ])