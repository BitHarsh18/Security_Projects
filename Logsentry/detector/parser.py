import re

log_pattern = re.compile(
    r'(?P<ip>\S+) .* \[(?P<time>.*?)\] "(?P<method>\S+) (?P<url>\S+) .*" (?P<status>\d+) (?P<size>\d+)'
)

def parse_log_line(line):
    match = log_pattern.match(line)
    if match:
        return match.groupdict()        
    return None