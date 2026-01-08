import subprocess
from datetime import datetime

TARGET = "http://testphp.vulnweb.com/"
REPORT_FILE = "report.txt"

def run_scan():
    """
    Executes Nikto scan on the target
    """
    command = ["nikto", "-h", TARGET]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)

def generate_report(output, error):
    with open(REPORT_FILE, "w") as report:
        report.write("VULNERABILITY SCAN REPORT\n")
        report.write("=" * 40 + "\n")
        report.write(f"Target     : {TARGET}\n")
        report.write(f"Scan Tool  : Nikto\n")
        report.write(f"Date       : {datetime.now()}\n\n")

        report.write("SCAN OUTPUT\n")
        report.write("-" * 40 + "\n")
        report.write(output if output else "No output\n")

        report.write("\nERRORS\n")
        report.write("-" * 40 + "\n")
        report.write(error if error else "No errors\n")

    print("[+] Report generated: report.txt")

def main():
    print("[+] Starting scan on target:", TARGET)
    output, error = run_scan()
    generate_report(output, error)

if __name__ == "__main__":
    main()
