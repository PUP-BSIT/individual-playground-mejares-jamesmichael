print ("Synthesize your Learning\n")

# Function to process the list
def process_list(numbers):
    return numbers

# Create an empty list
user_list = []

# Ask for 5 numbers from the user
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    user_list.append(num)

# Call the function with the list
returned_list = process_list(user_list)

# Print the returned list
print("The returned list is:", returned_list)

