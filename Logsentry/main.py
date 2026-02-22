from detector.parser import parse_log_line
from detector.analyzer import analyze_logs

def load_logs(file_path):
    parsed_logs = []

    with open(file_path, "r") as file:
        for line in file:
            parsed = parse_log_line(line)
            if parsed:
                parsed_logs.append(parsed)

    return parsed_logs

def generate_report(results):
    print("\n====== ThreatLens Security Report ======\n")

    print(f"SQL Injection Attempts Detected: {len(results['sqli'])}")
    print(f"XSS Attempts Detected: {len(results['xss'])}")

    print("\nBrute Force IPs Detected:")
    if results["bruteforce"]:
        for ip, count in results["bruteforce"].items():
            print(f"IP: {ip} | Failed Attempts: {count}")
    else:
        print("No brute force activity detected.")

if __name__ == "__main__":
    logs = load_logs("logs/access.log")
    results = analyze_logs(logs)
    generate_report(results)