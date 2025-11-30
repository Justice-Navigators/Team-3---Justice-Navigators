import justice_navigator_info
import pandas as pd
import numpy as np
import os
import datetime
from colorama import init, Fore, Back, Style      # type: ignore   
import colorama                                   # type: ignore

autoreset=True

def welcome_message():
    """introduction to journal"""
    print(f"\n{"="*14} Welcome to your Journal Companion {"="*15}\n")
    print(f"This is a private space to reflect on your journey.")
    print(f"All entries will be securely saved on your device.")
    print(f"Take your time, there's no rush.\n")

def user_info():
    """capture basic information from user"""
    print(f"As we begin this journey, let's get to know some more ...")

    # capture user name with validation
    while True:
        name = input("What is your first name, or what would like to be addressed as? ").strip()
        if name:
            break
        else:
            print(f"Please enter you name to continue.")

    # date capture for time stamps
    while True:
        reentry_date = input("When did you reenter society? (MM/DD/YYYY) ")
        try:
            datetime.datetime.strptime(reentry_date, "%m/%d/%Y")
            break
        except ValueError:
            print(f"Please enter a valid date in MM/DD/YYYY format.")

    return name, reentry_date

def daily_reflection(name):
    """guide user through daily reflection"""
    print(f"\n Hello {name}, let's reflect on today...")

    # record date and time
    current_date = datetime.datetime.now().strftime("%m/%d/%Y")
    current_time = datetime.datetime.now().strftime("%I:%M %p")

    print(f"\nToday's Date: {current_date}")
    print(f"Current Time: {current_time}")