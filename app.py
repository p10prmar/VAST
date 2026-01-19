import requests
from datetime import datetime

TARGET = "http://testphp.vulnweb.com"

def scan_website():
    print("=" * 50)
    print("SIMPLE WEBSITE SCAN")
    print("=" * 50)
    print(f"Target : {TARGET}")
    print(f"Time   : {datetime.now()}")
    print()

    try:
        response = requests.get(TARGET, timeout=10)

        print("[+] Website is UP")
        print("[+] Status Code :", response.status_code)
        print()

        print("---- HTTP HEADERS ----")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

    except requests.exceptions.RequestException as e:
        print("[-] Website is DOWN or unreachable")
        print("Error:", e)


if __name__ == "__main__":
    scan_website()
