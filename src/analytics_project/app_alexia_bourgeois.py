"""app_alexia_bourgeois.py - Project script.

Author: Alexia Bourgeois
Date: 2026-01-15

  Practice key Python skills related to:
    - imports
    - logging
    - variables
    - type hints
    - global constants
    - f-strings
    - functions
    - main function
    - conditional execution guard

OBS:
  This is your file to practice and customize.
  Find the TODO comments, and as you complete each task, remove the TODO note.

"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
import statistics
from typing import Final

from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

LOG: logging.Logger = get_logger("P01", level="INFO")

# === DECLARE GLOBAL CONSTANTS ===

# All these global variables are CONSTANT, they do NOT change when the program runs.
# By convention, constants are named in UPPERCASE_WITH_UNDERSCORES.
# The following illustrates variables that hold these common types:
#    str, int, float, bool, list of strings.
# `Final` is added to indicate these variables should not be reassigned.
# Examples:

MY_ANALYTICS_COMPANY: Final[str] = "DataFun Analytics"
MY_EMPLOYEE_COUNT: Final[int] = 150

MY_FAVORITE_COLOR: Final[str] = "Blue"

MY_AGE: Final[int] = 25

MY_HEIGHT: Final[float] = 5.167

IS_A_TEACHER: Final[bool] = True

STATES_I_HAVE_VISITED: Final[list[str]] = [
    "California",
    "Mississippi",
    "Oklahoma",
    "Arizona",
    "New York",
    "Louisianna",
    "New Mexico",
    "Texas",
    "Alabama",
    "Nevada",
    "Hawaii"
]

# === DECLARE A FUNCTION TO FORMAT THE INFORMATION ===

def get_summary() -> str:
    """Get a formatted summary of the information held in the global variables.

    Arguments: None (nothing is passed in the parentheses after `get_summary`).

    Returns: - a formatted multi-line string (starts with f and wrapped in triple quotes).
    """

    summary: str = f"""
    Custom Information:
        Company name: {MY_ANALYTICS_COMPANY}
        Employee count: {MY_EMPLOYEE_COUNT}
    All About Me:
        My favorite color: {MY_FAVORITE_COLOR}
        My age: {MY_AGE}
        My height: {MY_HEIGHT} feet
        Is a teacher: {IS_A_TEACHER}
        States I have visted: {STATES_I_HAVE_VISITED}

    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary

# === DECLARE A FUNCTION TO FORMAT DESCRIPTIVE STATISTICS ===

def get_statistics() -> str:
    """Get a formatted summary showing descriptive statistics.

    Arguments: None (nothing is passed in the parentheses).

    Returns: - a formatted multi-line string.
    """
    # Initialize sample data - snowfall measurements in inches.
    # REQ: Vary ONE of the sample data values.
    # See how the statistics change when you do.
    # TODO: Change one of the values in the list below.
    snowfall_inches: list[float] = [2.5, 3.2, 4.5, 5.5, 6.5]

    # Calculate descriptive statistics below - see other file for examples.

    # Example: Calculate total snowfall.
    total: float = sum(snowfall_inches)

    # Example : Calculate count of measurements.
    count: int = len(snowfall_inches)

    minimum: float = min(snowfall_inches) 
    maximum: float = max(snowfall_inches)
    
    # Use the statistics module to calculate average.
    average: float = statistics.mean(snowfall_inches) if count > 0 else 0.0

    std_dev: float = statistics.stdev(snowfall_inches) if count > 0 else 0.0

    # Build a formatted multi-line string using f and triple quotes.
    #.2f is rounding the float, makes a lot of sense

    summary: str = f"""
    Descriptive Statistics for Snowfall (inches):
        Total snowfall: {total:.2f} inches
        Count of measurements: {count}
        Minimum snowfall: {minimum:.2f} inches
        Maximum snowfall: {maximum:.2f} inches
        Average snowfall: {average:.2f} inches
        TODO: Add your standard deviation below:
        Standard Deviation: {std_dev:.3f} inches

    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Entry point when running this file as a Python script.

    Arguments: None.

    Returns: None.
    """
    # Log a header for the application.
    LOG.info("=================")
    log_header(LOG, "Foundations of Professional Python")
    LOG.info("=================")

    # Log start of main processing.
    LOG.info("START main()..................")

    # Call functions to get formatted strings and log them.
    summary: str = get_summary()
    LOG.info(summary)

    stats: str = get_statistics()
    LOG.info(stats)

    # Log end of main processing.
    LOG.info("END main()..................")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If running this file as a script, then call main() function.
# OBS: This is just standard Python boilerplate.

if __name__ == "__main__":
    main()
