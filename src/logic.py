import base64
import requests
from datetime import datetime

def get_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    consumer_key = ""
    consumer_secret = ""

    headers = {
        "Authorization": f"Basic {base64.b64encode(f'{consumer_key}:{consumer_secret}'.encode()).decode()}"
    }
    
    params = {}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        print(response.headers)
        print(response.content.decode())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

def generate_qr_code():
    url = "https://sandbox.safaricom.co.ke/mpesa/qrcode/v1/generate"
    body = {    
        "MerchantName": "TEST SUPERMARKET",
        "RefNo": "Invoice Test",
        "Amount": 1,
        "TrxCode": "BG",
        "CPI": "373132",
        "Size": "300"
    }
    token = {"access_token": ""}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token['access_token']}"
    }

    try:
        response = requests.post(url=url, json=body, headers=headers)
        response.raise_for_status()
        print(response.headers)
        print(response.content.decode())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

# Check the status of a Lipa Na M-Pesa Online Payment.

def check_lipa_na_mpesa_status():
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"
    
    # Replace with your actual access token
    token = {"access_token": "your_actual_access_token"}

    # Generate a current timestamp in the required format
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    body = {
        "BusinessShortCode": "174379",
        "Password": "MTc0Mzc5YmZiMjc5TliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTYwMjE2MTY1NjI3",
        "Timestamp": timestamp,
        "CheckoutRequestID": "ws_CO_260520211133524545",
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token['access_token']}"
    }

    try:
        response = requests.post(url=url, json=body, headers=headers)
        response.raise_for_status()
        print(response.headers)
        print(response.content.decode())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

def register_urls():
    url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    body = {    
        "ShortCode": "601426",
        "ResponseType":"Cancelled/Completed",
        "ConfirmationURL":"http://localhost:8000/confirmation",
        "ValidationURL":"http://localhost:8000/validation"
    }

    token = {"access_token": "UtPFXs1N8LbpHyGwk6YTUFgAqmo9"}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token['access_token']}"
    }

    try:
        response = requests.post(url=url, json=body, headers=headers)
        response.raise_for_status()
        print(response.headers)
        print(response.content.decode())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise
if __name__ == '__main__':
    register_urls()

