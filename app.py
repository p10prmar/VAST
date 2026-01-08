#!/usr/bin/env python3
import os
import sys
import time
from datetime import datetime

# -------------------------------
# Utility Functions
# -------------------------------

def banner():
    print("=" * 70)
    print("        VAST - Vulnerability Assessment Scanner Tool")
    print("        Author : Security Learner")
    print("        Use    : Educational Purpose Only")
    print("=" * 70)


def check_tool(tool_name):
    """Check if tool is installed"""
    return os.system(f"which {tool_name} > /dev/null 2>&1") == 0


def save_report(tool, target, output):
    filename = f"reports/{tool}_{target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(output)
    print(f"\n[+] Report saved as: {filename}")


def run_command(command):
    try:
        stream = os.popen(command)
        return stream.read()
    except Exception as e:
        return str(e)


# -------------------------------
# Scan Functions
# -------------------------------

def nmap_scan():
    if not check_tool("nmap"):
        print("[!] Nmap is not installed")
        return

    target = input("Enter target IP/Domain: ")
    print("\n[+] Running Nmap Scan...\n")
    command = f"nmap -sV -O {target}"
    output = run_command(command)
    print(output)
    save_report("nmap", target.replace("/", "_"), output)


def nikto_scan():
    if not check_tool("nikto"):
        print("[!] Nikto is not installed")
        return

    target = input("Enter target URL (http://example.com): ")
    print("\n[+] Running Nikto Scan...\n")
    command = f"nikto -h {target}"
    output = run_command(command)
    print(output)
    save_report("nikto", target.replace("/", "_"), output)


def whois_lookup():
    if not check_tool("whois"):
        print("[!] Whois is not installed")
        return

    target = input("Enter domain: ")
    print("\n[+] Running WHOIS Lookup...\n")
    command = f"whois {target}"
    output = run_command(command)
    print(output)

from datetime import datetime

report = f"""
Vulnerability Scan Report
=========================
Date: {datetime.now()}

Target: example.com
Status: Scan completed
Issues Found: None
"""

with open("report.txt", "w") as f:
    f.write(report)

print("Report generated successfully")


