import base64
import requests
from datetime import datetime
import libtorrent as lt
import time
import sys

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
    token = {"access_token": "EmpKFWVqLRADAusgudk6rY7a4wj0"}

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

def download_torrent():


    ses = lt.session({'listen_interfaces': '0.0.0.0:6881'})

    magnet_link = "magnet:?xt=urn:btih:158E3514A8EF7A538F4BE3075504612241ED6C62&dn=Terraform+Associate+Certification+%2B300+Exam+Practice+Questions...2ed+2023&tr=http%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2F47.ip-51-68-199.eu%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2780%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2730%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=ud"
    info = lt.torrent_info(lt.parse_magnet_uri(magnet_link))
    h = ses.add_torrent({'ti': info, 'save_path': '.'})
    s = h.status()
    print('starting', s.name)

    while (not s.is_seeding):
        s = h.status()

        print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
            s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
            s.num_peers, s.state), end=' ')

        alerts = ses.pop_alerts()
        for a in alerts:
            if a.category() & lt.alert.category_t.error_notification:
                print(a)

        sys.stdout.flush()

        time.sleep(1)

print(h.status().name, 'complete')
if __name__ == '__main__':
    register_urls()

