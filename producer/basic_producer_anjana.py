

"""
basic_generator_places_events.py

Generate some streaming buzz messages about events happening in different places. 
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os
import random
import time
import pathlib  # if needed

# Import external packages (must be installed in .venv first)
from dotenv import load_dotenv

# Import functions from local modules
from utils.utils_logger import logger 


#####################################
# Load Environment Variables
#####################################

# Load environment variables from .env
load_dotenv()

#####################################
# Define Getter Functions for .env Variables
#####################################

# Define a function to fetch the message interval from the environment
def get_message_interval() -> int:
    """
    Fetch message interval from environment or use a default value.
    """
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 3)
    interval: int = int(return_value)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval


#####################################
# Define global variables
#####################################

# Define some lists for generating buzz messages
PLACES: list = ["New York", "Chicago", "Los Angeles", "Miami", "Dallas"]
EVENTS: list = ["concert", "festival", "conference", "sports game", "parade"]

#####################################
# Define a function to generate buzz messages
#####################################


def generate_messages():
    """
    Generate a stream of buzz messages.

    This function uses a generator, which yields one buzz at a time.
    Generators are memory-efficient because they produce items on the fly
    rather than creating a full list in memory.

    Because this function uses a while True loop, it will run continuously 
    until we close the window or hit CTRL c (CMD c on Mac/Linux).
    """
    while True:
        place = random.choice(PLACES)
        event = random.choice(EVENTS)
        yield f"Breaking News: A {event} just started in {place}!"


#####################################
# Define main() function to run this producer.
#####################################


def main() -> None:
    """
    Main entry point for this producer.
    """

    logger.info("START producer...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    interval_secs: int = get_message_interval()

    for message in generate_messages():
        logger.info(message)
        time.sleep(interval_secs)

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END producer.....")


#####################################
# Conditional Execution
#####################################

# If this file is the one being executed, call the main() function
if __name__ == "__main__":
    # Call the main function by writing its name followed by parentheses.
    main()

