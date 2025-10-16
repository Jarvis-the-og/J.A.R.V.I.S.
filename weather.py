import requests

API_KEY = "7PWabnnG5tM6MHrahbbjU5UjURnlEuZC"  # Replace this with your actual API key
BASE_URL = "http://dataservice.accuweather.com"

# -------------------- Location Key Retrieval --------------------
def get_location_key(city_name):
    try:
        url = f"{BASE_URL}/locations/v1/cities/search?apikey={API_KEY}&q={city_name}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data:
            return data[0]['Key']
        else:
            return None
    except Exception as e:
        return None

# -------------------- Current Weather --------------------
def get_current_weather(city_name):
    location_key = get_location_key(city_name)
    if not location_key:
        return f"City '{city_name}' not found."
    try:
        url = f"{BASE_URL}/currentconditions/v1/{location_key}?apikey={API_KEY}&details=true"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data:
            current = data[0]
            weather = current["WeatherText"]
            temp = current["Temperature"]["Metric"]["Value"]
            humidity = current.get("RelativeHumidity", "N/A")
            precipitation = current.get("PrecipitationSummary", {}).get("Precipitation", {}).get("Metric", {}).get("Value", "N/A")
            precipitation_type = current.get("PrecipitationType", "none")
            uv_index = current.get("UVIndexText", "N/A")
            wind_speed = current.get("Wind", {}).get("Speed", {}).get("Metric", {}).get("Value", "N/A")

            return (
                f"The current weather in {city_name} is {weather} with a temperature of {temp}°C. "
                f"Humidity is at {humidity}%. "
                f"Precipitation: {precipitation} mm ({precipitation_type}). "
                f"UV Index: {uv_index}. "
                f"Wind Speed: {wind_speed} km/h."
            )
        else:
            return "Could not retrieve detailed weather data."
    except Exception as e:
        return f"Failed to get weather info: {e}"

# -------------------- Temperature Only --------------------
def get_temperature_only(city_name):
    location_key = get_location_key(city_name)
    if not location_key:
        return f"City '{city_name}' not found."
    try:
        url = f"{BASE_URL}/currentconditions/v1/{location_key}?apikey={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data:
            temp = data[0]["Temperature"]["Metric"]["Value"]
            return f"The current temperature in {city_name} is {temp} degrees Celsius."
        else:
            return "Could not retrieve temperature data."
    except Exception as e:
        return f"Failed to get temperature info: {e}"

# -------------------- Forecast --------------------
def get_forecast(city_name):
    location_key = get_location_key(city_name)
    if not location_key:
        return f"City '{city_name}' not found."
    try:
        url = f"{BASE_URL}/forecasts/v1/daily/1day/{location_key}?apikey={API_KEY}&metric=true&details=true"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data:
            forecast = data["DailyForecasts"][0]
            headline = data["Headline"]["Text"]
            min_temp = forecast["Temperature"]["Minimum"]["Value"]
            max_temp = forecast["Temperature"]["Maximum"]["Value"]
            day_phrase = forecast["Day"]["IconPhrase"]
            night_phrase = forecast["Night"]["IconPhrase"]
            rain_prob = forecast["Day"]["PrecipitationProbability"]
            humidity_day = forecast["Day"].get("RelativeHumidity", "N/A")

            return (
                f"Forecast for {city_name}: {headline}. \n"
                f"Day: {day_phrase}, Night: {night_phrase}. \n"
                f"Temperature will range from {min_temp}°C to {max_temp}°C. \n"
                f"Chance of rain during the day: {rain_prob}%. \n"
                f"Daytime humidity: {humidity_day}%."
            )
        else:
            return "Could not retrieve forecast data."
    except Exception as e:
        return f"Failed to get forecast: {e}"
