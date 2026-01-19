import requests
from datetime import datetime

TARGET = "http://testphp.vulnweb.com"
REPORT_FILE = "report.txt"

def scan_website():
    report_lines = []

    report_lines.append("SIMPLE WEBSITE SCAN REPORT")
    report_lines.append("=" * 50)
    report_lines.append(f"Target : {TARGET}")
    report_lines.append(f"Time   : {datetime.now()}")
    report_lines.append("")

    try:
        response = requests.get(TARGET, timeout=10)

        report_lines.append("[+] Website is UP")
        report_lines.append(f"[+] Status Code : {response.status_code}")
        report_lines.append("")
        report_lines.append("---- HTTP HEADERS ----")

        for header, value in response.headers.items():
            report_lines.append(f"{header}: {value}")

    except requests.exceptions.RequestException as e:
        report_lines.append("[-] Website is DOWN or unreachable")
        report_lines.append(f"Error: {e}")

    # Write report to file
    with open(REPORT_FILE, "w") as report:
        for line in report_lines:
            report.write(line + "\n")

    # Print output on console
    for line in report_lines:
        print(line)

    print("\n[+] Report generated:", REPORT_FILE)


if __name__ == "__main__":
    scan_website()
