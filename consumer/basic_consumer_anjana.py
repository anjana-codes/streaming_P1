"""
basic_consumer_case.py

Read a log file as it is being written and process multiple unique messages at a time.
"""

#####################################
# Import Modules
#####################################

import os
import time

from utils.utils_logger import logger, get_log_file_path

#####################################
# Define a function to process messages
#####################################

def process_messages(log_file, batch_size=4) -> None:
    """
    Read a log file and process up to 4 new messages at a time.

    Args:
        log_file (str): Path to the log file.
        batch_size (int): Number of messages to process per loop.
    """
    seen_messages = set()

    with open(log_file, "r") as file:
        file.seek(0, os.SEEK_END)
        print("Consumer is ready and waiting for new log messages...")

        while True:
            new_messages = []

            # Collect up to batch_size messages
            for _ in range(batch_size):
                line = file.readline()
                if line:
                    message = line.strip()
                    if message not in seen_messages:
                        seen_messages.add(message)
                        new_messages.append(message)

            # If no new messages, pause briefly
            if not new_messages:
                time.sleep(1)
                continue

            # Process all collected messages
            for message in new_messages:
                print(f"Consumed log message: {message}")

                # Event-specific alerts
                if "festival" in message.lower():
                    print(f"ALERT: Festival detected! \n{message}")
                    logger.warning(f"ALERT: Festival detected! \n{message}")

                elif "parade" in message.lower():
                    print(f"NOTICE: Parade detected! \n{message}")
                    logger.info(f"NOTICE: Parade detected! \n{message}")

                elif "concert" in message.lower():
                    print(f"INFO: Concert mentioned! \n{message}")
                    logger.info(f"INFO: Concert mentioned! \n{message}")

                elif "sports" in message.lower():
                    print(f"NOTICE: Sports event spotted! \n{message}")
                    logger.info(f"NOTICE: Sports event spotted! \n{message}")

#####################################
# Define main function
#####################################

def main() -> None:
    """Main entry point."""
    logger.info("START consumer...")

    log_file_path = get_log_file_path()
    logger.info(f"Reading file located at {log_file_path}.")

    try:
        process_messages(log_file_path)
    except KeyboardInterrupt:
        print("User stopped the process.")

    logger.info("END consumer.....")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()
