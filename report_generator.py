import pandas as pd

def generate_high_level_report(log_files):
    # Example: Aggregate data over recent weeks/months
    # Sample DataFrame (replace with actual data processing logic)
    data = {
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'Failures': [5, 3, 7],
        'Delays': [2, 1, 4]
    }
    df = pd.DataFrame(data)
    print("High-Level Report:")
    print(df)

def generate_detailed_report(log_file):
    # Example: Analyze data from the most recent log file
    # Sample DataFrame (replace with actual data processing logic)
    data = {
        'Timestamp': ['2022-01-03 10:00:00', '2022-01-03 11:00:00'],
        'Error Type': ['ERROR', 'DELAY'],
        'Description': ['Database connection error', 'Processing delay due to high load']
    }
    df = pd.DataFrame(data)
    print("Detailed Report (Most Recent Run):")
    print(df)

# Example usage:
log_files = ["path/to/cleaned/logs/filtered_logs_20220101_120000.txt", "path/to/cleaned/logs/filtered_logs_20220102_100000.txt"]
most_recent_log_file = "path/to/cleaned/logs/filtered_logs_20220103_090000.txt"

generate_high_level_report(log_files)
generate_detailed_report(most_recent_log_file)
