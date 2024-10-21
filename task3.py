import sys
import re
from collections import Counter


def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return [parse_log_line(line) for line in lines]
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)

def parse_log_line(line: str) -> dict:
    log_dict = {}
    match = re.match(r"(\S+) (\S+) (\S+) (.+)", line)
    if match:
        log_dict["date"] = match.group(1)
        log_dict["time"] = match.group(2)
        log_dict["level"] = match.group(3)
        log_dict["message"] = match.group(4)
    return log_dict


def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].lower() == level.lower()]


def count_logs_by_level(logs: list) -> dict:
    levels = [log['level'] for log in logs]
    return dict(Counter(levels))


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("---------------- | ---------")
    for level, count in counts.items():
        print(f"{level:<15} | {count}")

# Функція для відображення деталей логів за рівнем
def display_log_details(logs: list, level: str):
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

# Основна функція
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