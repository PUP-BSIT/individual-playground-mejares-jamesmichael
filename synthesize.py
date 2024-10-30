# Function to process the list (this could be expanded for any processing logic)
def process_list(numbers):
    return numbers

# Function to compute sum
def sum_of_list(numbers):
    return sum(numbers)

# Function to compute average
def average_of_list(numbers):
    average = sum(numbers) / len(numbers)
    return average

# Function to find the highest value
def highest_value_list(numbers):
    highest_val = max(numbers)
    return highest_val

# Create an empty list
user_list = []

# Ask for 5 numbers from the user
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    user_list.append(num)

# Call the function with the list
returned_list = process_list(user_list)

# Print the returned list
print("\nThe returned list is:", returned_list)

#NUMBER 1 SYNTHESIZE
# Call the sum_of_list function and print the sum
total_sum = sum_of_list(returned_list)
print(f"The total sum of the list is: {total_sum}")

#NUMBER 2 SYNTHESIZE
total_average = average_of_list (returned_list)
print(f"The total average of the list is: {total_average}")

#NUMBER 3 SYNTHESIZE
highest_value = highest_value_list (returned_list)
print(f"The highest value in the list is: {highest_value}")