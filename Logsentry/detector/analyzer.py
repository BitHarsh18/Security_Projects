from detector.rules import detect_sqli, detect_xss, detect_bruteforce

def analyze_logs(parsed_logs):
    sqli_attacks = []
    xss_attacks = []

    for log in parsed_logs:
        if detect_sqli(log["url"]):
            sqli_attacks.append(log)

        if detect_xss(log["url"]):
            xss_attacks.append(log)

    bruteforce_ips = detect_bruteforce(parsed_logs)

    return {
        "sqli": sqli_attacks,
        "xss": xss_attacks,
        "bruteforce": bruteforce_ips
    }