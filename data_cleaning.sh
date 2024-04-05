#!/bin/bash

# Define paths
LOG_DIR="/path/to/local/output"
CLEANED_DIR="/path/to/cleaned/logs"

# Example cleaning and filtering (adjust as needed)
for logfile in "$LOG_DIR"/*.txt; do
    # Filter logs for errors and delays
    grep -E "ERROR|DELAY" "$logfile" > "$CLEANED_DIR/filtered_$(basename "$logfile")"
done

echo "Data cleaning and filtering completed."
