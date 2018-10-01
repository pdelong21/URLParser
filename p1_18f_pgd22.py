"""
Project 1 for CS 341
Semester: Fall 2018
Written by: Patrick Delong pgd22@njit.edu
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
        if flow == [1, 2, 3]:  # Went from state 1 -> 2 -> 3
            print(url + " ACCEPTED and the flow was ", flow, " ==> L1")
        elif flow == [2, 3]:   # Went from state 2 -> 3
            print(url + " ACCEPTED and the flow was ", flow, " ==> L2")
        else:  # Either went to state 1 -> 3, just to 2, or just to 3...
            print(url + " REJECTED")
        ask_input("Would you like to enter another website (y or n)?: ")  # Recursive call to input more sites
    elif ans == "n":  # User is done
        print("Bye!!")
        return  # End the program
    else:
        ask_input("Must type 'y' or 'n': ")  # User didn't format the answer right


# Parse the url character by character and return whether it was accepted or rejected
def parse_url(url):
    sub_str = ""  # Start with a blank sub string to build and compare
    state = 0  # We have no state yet
    s_flow = []  # Start with a blank list

    for char in url:  # Character by character in the url
        sub_str += char  # Build up the string to compare against s1, s2, or s3

        if char is '.' and sub_str in range_s1 and state == 0:  # if we are just starting and we notice the substring
            s_flow += [1]                                       # is in s1, push back the state
            sub_str = ''                                        # clear the string
            state = 2                                           # next state should be this
            continue

        # We are either starting off in s2 or coming from s1, either way it has been taken note of in s_flow
        # which contains a collection of states as they are transitioned. This if statement says IF everything before
        # the dot is lowercase and is not a string contained in range_s3 and we aren't in state 3. Then,
        elif char is '.' and sub_str[0:-1].islower() and state != 3 and sub_str not in range_s3:
            s_flow += [2]  # Push back the state
            sub_str = '.'  # Clear the substring and keep the dot as its need for a later comparison
            state = 3      # Change the state to s3 so we don't get back in here
            continue
    #  If we went through state 2 then this will get executed so as long the substring is contained in range_s3
    if state == 3 and sub_str in range_s3:
        s_flow += [state]  # push back the state
        return s_flow      # return our list of states


print("Project 1 for CS 341\n"
      "Semester: Fall 2018\n"
      "Written by: Patrick Delong pgd22@njit.edu\n"
      "Instructor:  Marvin Nakayama, marvin@njit.edu\n")


# Get input from the user OR cat in the file from stdout to stdin using command cat cases.txt | python3 p1_18f_pgd22.py
ask_input("Would you like to enter a website?(enter 'y' -> yes, 'n' -> no): ")