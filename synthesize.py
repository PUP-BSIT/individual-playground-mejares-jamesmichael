# Function to process the list (this could be expanded for any processing logic)
def process_list(numbers):
    return numbers

# Function to compute sum
def sum_of_list(numbers):
    return sum(numbers)

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

# Call the sum_of_list function and print the sum
total_sum = sum_of_list(returned_list)
print(f"The total sum of the list is: {total_sum}")
