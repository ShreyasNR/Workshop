"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:

      integer = int(input("Enter the required integer:"))
      finished = True

    except :
        print("Please enter a valid integer.")
print("Valid result is:", integer)


