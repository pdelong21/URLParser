"""
Project 1 for CS 341
Semester: Fall 2018
Written by: Patrick Delong pgd22
Instructor:  Marvin Nakayama, marvin@njit.edu
"""
import string

range_s1 = ["www."]  # s1
range_l = string.ascii_lowercase  # s2
range_s3 = [".com", ".com.co", ".co"]  # s3


# Recursive function that takes a parameter message to instruct the user as what to do next
def ask_input(msg):
    ans = input(msg)  # Save the input answer
    if ans == "y":  # User wants to continue entering in websites
        url = input("Enter website: ")  # Save the input website
        flow = parse_url(url)  # Here we will call our parse function to check if its accepted or rejected
        if flow == [1, 2, 3]:
            print(url + " ACCEPTED and the flow was ", flow, " ==> L1")
        elif flow == [2, 3]:
            print(url + " ACCEPTED and the flow was ", flow, " ==> L2")
        else:
            print(url + " REJECTED")
        ask_input("Would you like to enter another website (y or n)?: ")  # Recursive call
    elif ans == "n":  # User is done
        print("Bye!!")
        return  # End the program
    else:
        ask_input("Must type 'y' or 'n': ")  # User didn't format the answer right


# Parse the url character by character and return wether it was accepted or rejected
def parse_url(url):
    sub_str = ""  # Start with a blank sub string to build and compare
    state = 0  # We have no state yet
    s_flow = []

    for char in url:
        sub_str += char

        if char is '.' and sub_str in range_s1 and state == 0:
            s_flow += [1]
            sub_str = ''
            state = 2
            continue

        elif char is '.' and sub_str[0:-1].islower() and state != 3 and sub_str not in range_s3:
            s_flow += [2]
            sub_str = '.'
            state = 3
            continue

    if state == 3 and sub_str in range_s3:
        s_flow += [state]
        return s_flow


print("Project 1 for CS 341\n"
      "Semester: Fall 2018\n"
      "Written by: Patrick Delong pgd22\n"
      "Instructor:  Marvin Nakayama, marvin@njit.edu\n")


# Get input from the user OR cat in the file from stdout to stdin using command cat cases.txt | python3 p1_18f_pgd22.py
ask_input("Would you like to enter a website?(enter 'y' -> yes, 'n' -> no): ")