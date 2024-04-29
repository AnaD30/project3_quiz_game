# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
from rich import rich

def clear_terminal():
    """
    Wipes the terminal clean
    """
    os.system('cls' if os.name == 'nt' else 'clear')