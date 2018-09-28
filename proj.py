"""
Project 1 for CS 341
Semester: Fall 2018
Written by: Patrick Delong pgd22
Instructor:  Marvin Nakayama, marvin@njit.edu
"""
import sys
import string

range_s1 = ["www."]  # s1
range_s2 = string.ascii_lowercase  # s2
range_s3 = [".com", ".com.co", ".co"]  # s3


# Recursive function that takes a parameter message to instruct the user as what to do next
def ask_input(msg):
    ans = input(msg)  # Save the input answer
    if ans == "y":  # User wants to continue entering in websites
        url = input("Enter website: ")  # Save the input website
        parse_url(url)  # Here we will call our parse function to check if its accepted or rejected
        ask_input("Would you like to enter another website (y or n)?: ")  # Recursive call
    elif ans == "n":  # User is done
        return  # End the program
    else:
        ask_input("Must type 'y' or 'n': ")  # User didn't format the answer right


# Parse the url character by character
def parse_url(url):
    for char in url:
        print(char)

print("Project 1 for CS 341\n"
      "Semester: Fall 2018\n"
      "Written by: Patrick Delong\ pgd22\n"
      "Instructor:  Marvin Nakayama, marvin@njit.edu\n")

# Get input from the user OR cat in the file from stdout to stdin using command cat cases.txt | python3 proj.py
ask_input("Would you like to enter a website?(enter 'y' -> yes, 'n' -> no): ")
