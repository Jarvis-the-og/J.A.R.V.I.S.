import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import random
import webbrowser
import requests
import pygetwindow as gw
import time
import pyautogui
from bs4 import BeautifulSoup


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 250
        audio = r.listen(source, 0, 6)

    try:
        print("Understanding and Processing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
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
        print(random.choice(unclear_responses))
        return "none"
    return query.lower()

def searchGoogle(query):

    if "google" in query:
        import wikipedia as googleScrap
        fillers = ["open", "launch", "jarvis", "please", "could you", "can you", "start", "google search","google", "search"]
        for word in fillers:
            query = query.replace(word, "")
        query = query.strip()

        speak("These are the results which I found on the web")
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            responses = [
                "I am still learning. Currently this is beyond my domain.",
                "Apologies, but I haven't mastered that yet.",
                "I'm not trained for this task at the moment.",
                "That's outside my current knowledge base, but I'll get there soon."
            ]
            speak(random.choice(responses))

def focus_youtube_window():
    for window in gw.getWindowsWithTitle("YouTube"):
        if window.isMinimized:
            window.restore()
        window.activate()
        time.sleep(1)  # Wait to ensure focus
        return True
    return False

def searchYoutube(query):
    speak("Searching YouTube...")
    
    # Remove trigger phrases
    query = query.replace("jarvis", "")
    query = query.replace("youtube search", "")
    query = query.replace("youtube", "")
    query = query.replace("play","")
    query = query.strip()

    if not query:
        speak("Please tell me what to search on YouTube.")
        return

    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

    try:
        pywhatkit.playonyt(query)
        speak("Here is your video.")
    except:
        speak("Something went wrong while opening YouTube.")


def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching results....")
        query = query.replace("jarvis","")
        query = query.replace("wikipedia search","")
        query = query.replace("wikipedia","")
        query = query.strip()  # Remove extra spaces
        
        if not query:  # If query is empty after cleaning
            speak("Please specify what you want to search on Wikipedia")
            return
        
        try:
            results = wikipedia.summary(query, sentences=2).strip()
            
            # Remove or replace problematic characters for safe output
            safe_results = results.encode('ascii', errors='replace').decode()
            speak("According to Wikipedia")
            print(safe_results)
            speak(safe_results)

            
        except wikipedia.exceptions.DisambiguationError as e:
            # Handle disambiguation - use the first suggestion
            try:
                results = wikipedia.summary(e.options[0], sentences=2)
                speak(f"I found multiple results. Here's information about {e.options[0]}")
                print(results)
                speak(results)
            except Exception:
                speak("The search term is too ambiguous. Please be more specific")
                
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find any Wikipedia page for that topic")
            
        except Exception as e:
            print(f"Wikipedia search error: {e}")
            fallback_responses = [
                "There was an error searching Wikipedia. Please try again.",
                "Something went wrong while fetching the Wikipedia data.",
                "Hmm... I hit a snag while accessing Wikipedia.",
                "Sorry, I couldn't complete the Wikipedia search right now."
            ]
            speak(random.choice(fallback_responses))

# def get_weather(city):
#     try:
#         if not city or city.lower() == "in":
#             speak("Please provide a valid city name to get the weather report.")
#             return

#         url = f"https://wttr.in/{city}?format=j1"
#         response = requests.get(url)
#         data = response.json()

#         current = data['current_condition'][0]
#         weather = current['weatherDesc'][0]['value']
#         temp = current['temp_C']
#         feels_like = current['FeelsLikeC']
#         humidity = current['humidity']
#         chance_of_rain = data['weather'][0]['hourly'][1]['chanceofrain']
#         max_temp = data['weather'][0]['maxtempC']
#         min_temp = data['weather'][0]['mintempC']

#         message = (
#             f"Currently in {city}, it's {weather}. "
#             f"The temperature is {temp} degrees Celsius, feels like {feels_like}. "
#             f"Humidity is at {humidity} percent. "
#             f"The maximum today is {max_temp}, and the minimum is {min_temp} degrees. "
#             f"Chance of rain is {chance_of_rain} percent."
#         )

#         print(message)
#         speak(message)

#     except Exception as e:
#         print("Weather fetch error:", e)
#         speak("I couldn't fetch the full weather details at the moment.")


# def get_temperature(city):
#     try:
#         if not city or city.lower() == "in":
#             speak("Please provide a valid city name to get the temperature.")
#             return

#         url = f"https://wttr.in/{city}?format=j1"
#         response = requests.get(url)
#         data = response.json()

#         temp = data['current_condition'][0]['temp_C']
#         print(f"The temperature in {city} is {temp}°C.")
#         speak(f"The temperature in {city} is {temp} degrees Celsius.")

#     except Exception as e:
#         print("Temperature fetch error:", e)
#         speak("I couldn't fetch the temperature at the moment.")

# elif "weather" in query:
                #     city = ""
                #     if "in" in query:
                #         city = query.split("in", 1)[-1].strip()
                #         if not city:
                #             speak("Please mention a proper city name to get weather.")
                #             continue
                #     else:
                #         speak("Please mention a proper city name to get weather.")
                #         continue
                #     get_weather(city)