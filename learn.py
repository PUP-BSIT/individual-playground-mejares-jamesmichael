#No. 1 Problem Write a program that takes 2 numbers and tell whether the numbers are equal or not.
"""
print ("Problem 1")
Num1 = int (input("Enter first number: "))
Num2 = int (input("Enter second number: "))

if Num1 == Num2:
    print("Both are equal")
else:
    print ("Both are not equal")
"""

#No.2 Write a program that takes a number and tell whether the number is odd, even, or zero.
"""
print ("Problem 2")
Num1 = int (input("Enter first number: "))

if Num1 == 0:
    print ("the number is zero") 
elif Num1 % 2 == 0:
    print ("the number is even")
else:
    print ("the number is odd")
"""

#No. 3 Write a program that takes 3 numbers and prints the highest number
"""
print ("Problem 3")
Num1 = int (input("Enter first number: "))
Num2 = int (input("Enter second number: "))
Num3 = int (input("Enter third number: "))

if Num1 >= Num2 and Num1 >= Num3:
    print ("The highest number is num1 ")
elif Num2 >= Num2 and Num2 >= Num3:
    print ("The highest number is num2")
else:
    print ("The highest number is num3")

"""
#No. 4 Write a program that takes a a coordinate and tell which quadrant the coordinate falls.
"""
print ("Problem 4")
Num1 = int (input("Enter first number: "))
Num2 = int (input("Enter second number: "))

if Num1 >= 0 and Num2 <= 0:
    print ("Fourth Quadrant")
elif Num1 <= 0 and Num2 >= 0:
    print ("Second Quadrant")
elif Num1 <= 0 and Num2 <= 0:
    print ("Third Quadrant")
else: 
    print ("First Quadrant")

"""

#No. 5 Write a program that takes a character and tells whether it is consonant or vowel.
"""
print ("Problem 5")
letter = str(input("Enter a letter: "))

if letter == "a" or letter == "e" or  letter == "i" or letter == "o" or letter == "u":
    print ("The letter is a vowel")
else:
    print ("Thee letter is a consonant")
"""

#No. 6 Write a program that takes a 2 digit number and returns the sum of the 2 digits. Ex. 24 -> 6

# Get the user input (integer)
user_digit = input("Enter a number: ")

# Convert the string input into integers
digit_1 = int(user_digit[0])
digit_2 = int(user_digit[1])

# A variable that adds the two digits
sum_of_digits = digit_1 + digit_2

# Print the sum of the two digits
print(sum_of_digits)