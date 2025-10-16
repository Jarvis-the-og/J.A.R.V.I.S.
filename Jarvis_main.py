import pyttsx3
import random
import requests
import time
import os
import pyautogui
import core
from bs4 import BeautifulSoup
import speech_recognition
from conversations import get_response
from Namaskaram import greetMe
import todo  # Make sure todo.py is in the same folder
from weather import get_temperature_only
from dictApp import openAppWeb, closeAppWeb
from alarm import setAlarm, voice_to_time
from timer import start_timer, voice_to_seconds
import subprocess

# Jarvis prototype v2 - speech-to-text and text-to-speech with external conversation mapping

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

def run_jarvis():
# Initial startup message
    speak("We are online and ready")


    while True:
        query = takeCommand()
        if "wake up jarvis" in query or "jarvis you up" in query or "wake up daddy's home" in query:
            greetMe()
            speak("Please mention the authentication code")

            query = takeCommand()
            if "jarvis 3212" in query:
                speak("access granted sir")
                print("access granted sir")
                speak("How may I assist you today?")


                while True:
                    query = takeCommand()
                    if "go to sleep pal" in query or "we are done for now" in query:
                        speak("Going into sleep. Will calibrate systems")
                        speak("You may call me anytime")
                        break

                    # ------------- open close stuff -------------

                    elif "google" in query and "launch" not in query and "open" not in query:
                        from searchNow import searchGoogle
                        searchGoogle(query)

                    elif "youtube" in query and "open" not in query:
                        from searchNow import searchYoutube
                        searchYoutube(query)

                    elif any(kw in query for kw in ["instagram", "reddit", "chatgpt"]):
                        response = get_response(query)
                        print(f"Jarvis: {response}")  # Optional: print response to console
                        speak(response)

                    elif "open" in query or "launch" in query:
                        openAppWeb(query)

                    elif "close" in query:
                        closeAppWeb(query)

                    # ------------- yt controls -------------

                    elif "pause" in query or "play" in query:
                        from searchNow import focus_youtube_window
                        if focus_youtube_window():
                            pyautogui.press('k')
                        else:
                            speak("YouTube window is not open.")


                    # ------------- Alarm -------------

                    elif "set an alarm" in query:
                        speak("Tell me the alarm time in 24-hour format, like fourteen thirty or seventeen thirteen.")
                        spoken_time = takeCommand()

                        if spoken_time != "none":
                            alarm_time = voice_to_time(spoken_time)
                            print(f"Parsed time: {alarm_time}")  # Debug info

                            if alarm_time:
                                # Launch alarm.py in a separate process with the time argument
                                subprocess.Popen(["python", "alarm.py", alarm_time])
                                speak(f"Alarm set for {alarm_time}, sir.")
                            else:
                                speak("I couldn't understand the time. Please try again with format like seventeen thirty.")
                        else:
                            speak("I didn't hear the time. Please try setting the alarm again.")

                    # ------------- Timer -------------

                    elif "set a timer" in query or "timer" in query:
                        speak("Please tell me the timer duration, sir.")
                        duration_text = takeCommand()
                        if duration_text != "none":
                            total_seconds = voice_to_seconds(duration_text)
                            success = start_timer(total_seconds)
                            if not success:
                                speak("Please try again with a valid timer duration.")
                        else:
                            speak("I did not get the timer duration. Please try again.")

                    # ------------- Reminder -------------

                    elif "remind me to" in query or "reminder" in query:
                        try:
                            query = query.lower()
                            message = None
                            time_part = None

                            if "remind me to" in query and "at" in query:
                                parts = query.split("remind me to", 1)[1].strip()
                                if " at " in parts:
                                    message, time_part = parts.rsplit(" at ", 1)

                            elif "reminder to" in query and "at" in query:
                                parts = query.split("reminder to", 1)[1].strip()
                                if " at " in parts:
                                    message, time_part = parts.rsplit(" at ", 1)

                            if message and time_part:
                                reminder_time = voice_to_time(time_part)
                                if reminder_time:
                                    subprocess.Popen(["python", "reminder.py", reminder_time, message])
                                    print(f"Reminder set for {reminder_time}, with message: {message}")
                                else:
                                    speak("I couldn't understand the time. Please try again with a proper format like 5 PM or 17 00.")
                            else:
                                speak("Please say the reminder like: remind me to take medicine at 5 PM.")

                        except Exception as e:
                            speak("Something went wrong while setting the reminder.")
                            print("Error in reminder elif:", e)




                    elif "wikipedia" in query:
                        from searchNow import searchWikipedia
                        searchWikipedia(query)

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

                    # ------------- Weather related -------------

                    elif "weather" in query:
                        city = ""
                        if "in" in query:
                            city = query.split("in", 1)[-1].strip()
                            if not city:
                                speak("Please mention a proper city name to get weather.")
                                continue
                        else:
                            speak("Please mention a proper city name to get weather.")
                            continue
                        from weather import get_current_weather
                        weather_info = get_current_weather(city)
                        print(weather_info)
                        speak(weather_info)

                    elif "temperature" in query:
                        city = ""
                        if "in" in query:
                            city = query.split("in", 1)[-1].strip()
                            if not city:
                                speak("Please mention a proper city name to get temperature.")
                                continue
                        else:
                            speak("Please mention a proper city name to get temperature.")
                            continue
                        from weather import get_temperature_only
                        temperature_info = get_temperature_only(city)
                        print(temperature_info)
                        speak(temperature_info)

                    elif "forecast" in query or "weather forecast" in query or "weather prediction" in query:
                        city = ""
                        if "in" in query:
                            city = query.split("in", 1)[-1].strip()
                            if not city:
                                speak("Please mention a proper city name to get forecast.")
                                continue
                        else:
                            speak("Please mention a proper city name to get forecast.")
                            continue
                        from weather import get_forecast
                        forecast_info = get_forecast(city)
                        print(forecast_info)
                        speak(forecast_info)

                    # ------------- To-Do list -------------

                    elif "to do" in query or "take a note" in query:
                        try:
                            speak("What should I note down, sir?")
                            task = takeCommand()
                            if task and task != "none":
                                todo.add_task(task)
                                print(f"Task added: {task}")
                            else:
                                speak("I didn't catch that. Please try again.")
                        except Exception as e:
                            speak("There was an error while adding the task.")
                            print("Error:", e)

                    elif "agenda" in query or "checklist" in query:
                        try:
                            todo.read_tasks()
                        except Exception as e:
                            speak("Unable to fetch your checklist at the moment.")
                            print("Error:", e)

                    elif "mark" in query and "done" in query:
                        try:
                            speak("Tell me the task number or the task name to mark as done.")
                            task_identifier = takeCommand()
                            if task_identifier and task_identifier != "none":
                                todo.mark_done(task_identifier)
                            else:
                                speak("I didn't catch the task. Please try again.")
                        except Exception as e:
                            speak("Something went wrong while marking the task.")
                            print("Error:", e)


                    # ------------- Phone Number lookupp -------------

                    elif any(kw in query for kw in ["lookup phone", "phone lookup", "get phone info", "get phone details"]):
                        speak("Please say the full phone number, including the country code. For example, say plus nine one followed by the number.")
                        
                        import speech_recognition as sr
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print("Listening for phone number...")
                            r.pause_threshold = 1
                            audio = r.listen(source, timeout=7, phrase_time_limit=10)

                        try:
                            phone_number = r.recognize_google(audio, language='en-in')
                            phone_number = phone_number.lower().replace("plus", "+").replace(" ", "").replace("dash", "")
                            from phoneLookUp import lookup_phone_number
                            result = lookup_phone_number(phone_number)
                            print(result)
                            speak("Here is the information I found.")
                            speak(result)
                            
                        except sr.UnknownValueError:
                            speak("Sorry, I couldn't understand the number. Please try again.")
                        except sr.RequestError:
                            speak("Sorry, there was an error with the speech recognition service.")

                    # ------------- Battery Info -------------
                    elif any(phrase in query for phrase in ["battery status", "check battery", "battery percentage"]):
                        from core import get_battery_status
                        result = get_battery_status()
                        print(result)
                        speak(result)

                    # ------------- Volume Info -------------
                    elif any(phrase in query for phrase in ["volume status", "current volume", "what's the volume"]):
                        from core import get_volume_level
                        result = get_volume_level()
                        print(result)
                        speak(result)

                    elif any(phrase in query for phrase in ["mute audio", "mute", "mute sound", "turn volume off"]):
                        from core import mute_volume
                        result = mute_volume()
                        print(result)
                        speak(result)

                    elif any(phrase in query for phrase in ["max volume", "set volume to max", "increase volume to full"]):
                        from core import max_volume
                        result = max_volume()
                        print(result)
                        speak(result)

                    elif "set volume to" in query:
                        from core import set_volume_level
                        import re
                        match = re.search(r"set volume to (\d+)", query)
                        if match:
                            level = int(match.group(1))
                            if 0 <= level <= 100:
                                result = set_volume_level(level)
                                print(result)
                                speak(result)
                            else:
                                speak("Please specify a volume between 0 and 100.")
                        else:
                            speak("Please specify the volume percentage to set.")

                    # ------------- Wi-Fi Info -------------
                    elif any(phrase in query for phrase in ["wifi status", "is wifi connected", "check connectivity","are we online"]):
                        from core import is_wifi_connected
                        result = is_wifi_connected()
                        print(result)
                        speak(result)

                    # ------------- Bluetooth Info -------------
                    elif any(phrase in query for phrase in ["bluetooth status", "is bluetooth connected", "check bluetooth"]):
                        from core import is_bluetooth_connected
                        result = is_bluetooth_connected()
                        print(result)
                        speak(result)

                    # ------------- IP Address Info -------------
                    elif any(phrase in query for phrase in ["ip address", "network info", "check ip"]):
                        from core import get_ip_info
                        result = get_ip_info()
                        print(result)
                        speak(result)

                    # ------------- Internet Speed Test -------------
                    elif any(phrase in query for phrase in ["speed test", "check internet speed", "test network speed"]):
                        from core import run_speed_test
                        result = run_speed_test()
                        print(result)
                        speak(result)

                    # ------------- Running Processes -------------
                    elif any(phrase in query for phrase in ["list running apps", "running processes", "active tasks", "show running apps"]):
                        from core import get_running_processes
                        result = get_running_processes()
                        if result:
                            for process in result:
                                speak(process)
                        else:
                            speak("No active processes found or access denied.")

                    # ------------- Kill Process -------------
                    elif "kill process" in query or "stop process" in query:
                        speak("Please tell me the exact name of the process to terminate.")
                        proc_name = takeCommand()
                        if proc_name != "none":
                            from core import kill_process
                            result = kill_process(proc_name)
                            print(result)
                            speak(result)

                    elif "finally sleep" in query:
                        speak("system shut down initiated")
                        speak("Jarvis powering off...")
                        print("Jarvis powering off...")
                        exit()
                    elif query != "none":
                        # Get response from conversations.py and speak it
                        response = get_response(query)
                        print(f"Jarvis: {response}")  # Optional: print response to console
                        speak(response)
                            
            else:
                speak("Invalid auth. illai podaa. wake up call terminated")

if __name__ == "__main__":
    run_jarvis()
                