import requests

def lookup_phone_number(phone_number):
    api_key = '64393141a88bf30c4a5d2b2d5b540460'  # replace with your actual API key
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&format=1"

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
