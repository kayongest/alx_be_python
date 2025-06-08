# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Ensure the size is a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    while row < size:
        # Print one row of asterisks
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1