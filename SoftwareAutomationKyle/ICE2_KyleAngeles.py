#ICE2_KyleAngeles
#Names: Kyle
#Date: 5-30-25

#The Boundary value analysis technique checks the program with input values that are on or close to
# boundary values. The Boundary value analysis is best suited when input values are expected to be within
# some domain. We would like to go beyond the legitimate domain of input values. This is what we call
# Robustness testing. Here, we also select invalid values and see the responses of the program. Invalid
# values are also important to check for the behavior of the program.


valid_numbers = []

#Prompt for the user
user = input("Enter space-separated numbers: ")

#This just splits the numbers separated by space's
items = user.split()


#Checks for valid integer using try and exception block
for item in items:
    try:
        num = int(item)
        valid_numbers.append(num)
    except ValueError:
        print(f"{item} The integer is not a valid integer and will be ignored. ")


#Handles case with no valid number
if not valid_numbers:
    print("No valid numbers entered. ")
else:
#Manual for loop to find the smallest number
    smallest = valid_numbers[0]
    for num in valid_numbers[1:]:
        if num < smallest:
             smallest = num
        print(f"The smallest number is: {smallest}")


