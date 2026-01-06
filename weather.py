import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not OPENWEATHER_API_KEY:
    raise ValueError("OPENWEATHER_API_KEY not found in environment variables")
BASE_URL = "https://api.openweathermap.org/data/2.5"

# -------------------- Current Weather --------------------
def get_current_weather(city_name):
    try:
        url = f"{BASE_URL}/weather"
        params = {
            "q": city_name,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # ---------- Core numbers ----------
        temp = round(data["main"]["temp"])
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]      # hPa
        wind_speed = data["wind"]["speed"]       # m/s
        description = data["weather"][0]["description"].capitalize()

        response_parts = [
            f"It’s {temp} degrees in {city_name} with {humidity} percent humidity."
        ]

        insights = []

        # ---------- Hot / Cold interpretation ----------
        if temp >= 35:
            insights.append("It’s quite hot outside, so staying hydrated would be important.")
        elif temp <= 15:
            insights.append("It’s fairly cold outside, so dressing warmly would help.")

        # ---------- Rain / Snow ----------
        if data.get("rain", {}).get("1h"):
            insights.append("Light rain is expected, so carrying an umbrella might be useful.")
        elif data.get("snow", {}).get("1h"):
            insights.append("Snowfall conditions are present, so travel carefully.")

        # ---------- UV Index (only if meaningful) ----------
        # OpenWeather provides UV via One Call API, but some setups still include it
        uv_index = data.get("uvi")
        if uv_index is not None and uv_index >= 6:
            insights.append("UV levels are on the higher side, so some sun protection would be wise.")

        # ---------- Pressure ----------
        if pressure < 1000:
            insights.append("Atmospheric pressure is quite low, which means the weather may change later.")

        # ---------- Wind ----------
        if wind_speed > 10:
            insights.append("Winds are stronger than usual, so outdoor conditions might feel rough.")

        # ---------- If nothing unusual ----------
        if not insights:
            insights.append("Overall, conditions look stable and comfortable.")

        response_parts.extend(insights)
        return " ".join(response_parts)

    except Exception:
        return "I couldn’t fetch the weather details right now. Please try again later."

# -------------------- Temperature Only --------------------
def get_temperature_only(city_name):
    try:
        url = f"{BASE_URL}/weather"
        params = {
            "q": city_name,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        return f"The current temperature in {city_name} is {temp} degrees Celsius."

    except Exception as e:
        return f"Failed to get temperature info: {e}"

# -------------------- Forecast (Next 24 Hours Summary) --------------------
def get_forecast(city_name):
    try:
        url = f"{BASE_URL}/forecast"
        params = {
            "q": city_name,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Next 24 hours (8 × 3-hour intervals)
        forecasts = data["list"][:8]

        temps = [item["main"]["temp"] for item in forecasts]
        min_temp = round(min(temps))
        max_temp = round(max(temps))

        # Rain probability (max POP)
        rain_prob = max(item.get("pop", 0) for item in forecasts) * 100

        # Pressure & wind averages
        avg_pressure = sum(item["main"]["pressure"] for item in forecasts) / len(forecasts)
        max_wind = max(item["wind"]["speed"] for item in forecasts)

        main_desc = forecasts[0]["weather"][0]["description"].capitalize()

        # -------- Phase 1: Numbers first --------
        response_parts = [
            f"Tomorrow’s temperature in {city_name} will range between {min_temp} and {max_temp} degrees."
        ]

        # -------- Phase 2: Interpretation --------
        insights = []

        if rain_prob >= 40:
            insights.append("There’s a fair chance of rain, so planning ahead would be wise.")

        if avg_pressure < 1000:
            insights.append("Pressure is expected to stay low, which means the weather could feel unstable.")

        if max_wind > 10:
            insights.append("Winds may pick up during the day, so outdoor conditions might feel rough.")

        if not insights:
            insights.append("Overall, the day looks stable and suitable for regular activities.")

        response_parts.extend(insights)

        return " ".join(response_parts)

    except Exception:
        return "I couldn't fetch the forecast right now. Please try again later."

def get_aqi(city_name):
    try:
        # Step 1: Get latitude & longitude from city name
        geo_url = "http://api.openweathermap.org/geo/1.0/direct"
        geo_params = {
            "q": city_name,
            "limit": 1,
            "appid": OPENWEATHER_API_KEY
        }

        geo_res = requests.get(geo_url, params=geo_params)
        geo_res.raise_for_status()
        geo_data = geo_res.json()

        if not geo_data:
            return f"I couldn't find air quality data for {city_name}."

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]

        # Step 2: Fetch AQI data
        aqi_url = f"{BASE_URL}/air_pollution"
        aqi_params = {
            "lat": lat,
            "lon": lon,
            "appid": OPENWEATHER_API_KEY
        }

        aqi_res = requests.get(aqi_url, params=aqi_params)
        aqi_res.raise_for_status()
        aqi_data = aqi_res.json()

        aqi = aqi_data["list"][0]["main"]["aqi"]

        # Step 3: Human-readable AQI interpretation
        if aqi == 1:
            return (
                f"The air quality index in {city_name} is around 45. "
                f"The air is clean and comfortable to breathe."
            )

        elif aqi == 2:
            return (
                f"The air quality index in {city_name} is around 75. "
                f"Air quality is acceptable, but sensitive people should be slightly cautious."
            )

        elif aqi == 3:
            return (
                f"The air quality index in {city_name} is around 120. "
                f"Air quality is moderate, so limiting long outdoor exposure would help."
            )

        elif aqi == 4:
            return (
                f"The air quality index in {city_name} is around 170. "
                f"The air is quite polluted right now, so avoiding outdoor activities would be a good idea."
            )

        elif aqi == 5:
            return (
                f"The air quality index in {city_name} has crossed 250. "
                f"Air quality is very poor, and staying indoors as much as possible would be safer."
            )

        else:
            return "Air quality data is currently unavailable."

    except Exception:
        return "I couldn't fetch the air quality information right now. Please try again later."

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