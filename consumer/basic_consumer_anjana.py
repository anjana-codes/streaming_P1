"""
basic_consumer_anjana.py

Read a log file as it is being written and perform simple analytics. 
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os
import time

# Import functions from local modules
from utils.utils_logger import logger, get_log_file_path

#####################################
# Define a function to process a single message
#####################################


def process_message(log_file) -> None:
    """
    Read a log file and process each message.

    Args:
        log_file (str): The path to the log file to read.
    """
    with open(log_file, "r") as file:
        # Move to the end of the file
        file.seek(0, os.SEEK_END)
        print("Consumer is ready and waiting for a new log message...")

        # Use while True loop so the consumer keeps running forever
        while True:

            # Read the next line of the file
            line = file.readline()

            # If the line is empty, wait for a new log entry
            if not line:
                delay_seconds = 1
                time.sleep(delay_seconds)
                continue

            # We got a new log entry!
            message = line.strip()
            print(f"Consumed log message: {message}")

            # Example analytics: Monitor for special events
            if "festival" in message.lower():
                print(f"ALERT: Festival detected! \n{message}")
                logger.warning(f"ALERT: Festival detected! \n{message}")

            if "concert" in message.lower():
                print(f"INFO: A concert was mentioned. \n{message}")
                logger.info(f"INFO: A concert was mentioned. \n{message}")


#####################################
# Define main function for this script.
#####################################


def main() -> None:
    """Main entry point."""

    logger.info("START consumer...")

    # Get the log file path from utils/utils_logger
    log_file_path = get_log_file_path()
    logger.info(f"Reading file located at {log_file_path}.")

    try:
        process_message(log_file_path)
    except KeyboardInterrupt:
        print("User stopped the process.")

    logger.info("END consumer.....")


#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()
