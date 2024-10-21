import sys
import re
from collections import Counter


def load_logs(file_path: str) -> list:
    """
    Loads logs from a file.

    Args:
        file_path (str): Path to the log file.

    Returns:
        list: A list of dictionaries representing each log.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return [parse_log_line(line) for line in lines]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

def parse_log_line(line: str) -> dict:
    '''
    Parses a log line and returns it as a dictionary.
    '''

    log_dict = {}
    match = re.match(r"(\S+) (\S+) (\S+) (.+)", line)
    if match:
        log_dict["date"] = match.group(1)
        log_dict["time"] = match.group(2)
        log_dict["level"] = match.group(3)
        log_dict["message"] = match.group(4)
    return log_dict


def filter_logs_by_level(logs: list, level: str) -> list:
    '''
    Filters logs by level.
    '''
    return [log for log in logs if log['level'].lower() == level.lower()]


def count_logs_by_level(logs: list) -> dict:
    ''''
    Counts the number of logs by level.
    '''
    levels = [log['level'] for log in logs]
    return dict(Counter(levels))


def display_log_counts(counts: dict):
    '''
    Displays the count of logs by level.
    '''

    print("Рівень логування | Кількість")
    print("---------------- | ---------")
    for level, count in counts.items():
        print(f"{level:<15} | {count}")


def display_log_details(logs: list, level: str):
    '''
    Displays the details of logs for a specified level.
    '''
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

# the main
if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)  
        display_log_counts(counts)

    elif len(sys.argv) > 2:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)
        display_log_details(filtered_logs, level)
    else:
        print("Entered: python main.py <path_to_logfile> [log_level]")
        sys.exit(1)