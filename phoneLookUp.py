import requests
import os
from dotenv import load_dotenv

load_dotenv()

def lookup_phone_number(phone_number):
    PHONELOOKUP_API_KEY = os.getenv("PHONELOOKUP_API_KEY")
    if not PHONELOOKUP_API_KEY:
        raise ValueError("PHONELOOKUP_API_KEY not found in environment variables")
    url = f"http://apilayer.net/api/validate?access_key={PHONELOOKUP_API_KEY}&number={phone_number}&format=1"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("valid"):
            info = (
                f"Phone Number: {data.get('international_format')}\n"
                f"Country: {data.get('country_name')} ({data.get('country_code')})\n"
                f"Location: {data.get('location')}\n"
                f"Carrier: {data.get('carrier')}\n"
                f"Line Type: {data.get('line_type')}"
            )
        else:
            info = "Invalid phone number or no information found."

        return info

    except Exception as e:
        return f"Error occurred while looking up the phone number: {str(e)}"
