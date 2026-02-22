import re

# SQL Injection patterns
SQLI_PATTERN = re.compile(r"(union|select|or 1=1|--)", re.IGNORECASE)

# XSS patterns
XSS_PATTERN = re.compile(r"(<script>|javascript:)", re.IGNORECASE)

def detect_sqli(url):
    return bool(SQLI_PATTERN.search(url))

def detect_xss(url):
    return bool(XSS_PATTERN.search(url))

def detect_bruteforce(logs):
    failed_attempts = {}

    for log in logs:
        if log["status"] == "401":
            ip = log["ip"]
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    # If more than 5 failed logins → suspicious
    return {ip: count for ip, count in failed_attempts.items() if count > 5}