import random

def generate_zero_sum_list(count=12, min_val=-50, max_val=50):
    """Generates a list of specified numbers that sum to 0."""
    # Generate count - 1 random numbers
    #numbers = [random.randint(min_val, max_val) for _ in range(count - 1)]
    numbers = []
    for x in range(count - 1):
        print(random.randint(min_val, max_val))
        numbers.append(random.randint(min_val, max_val))

    # Calculate the negative sum of the generated numbers to find the balancing final number
    balancing_number = -sum(numbers)
    print("balancing_number", balancing_number)

    # Append the balancing number to complete the list
    numbers.append(balancing_number)

    return numbers


# Generate the list of 12 numbers
zero_sum_list = generate_zero_sum_list(12)

print("Generated List:", zero_sum_list)
print("Sum of List:", sum(zero_sum_list))
'''
-28
13
-49
2
-10
-45
30
-32
28
-20
-35
balancing_number -61
Generated List: [18, 37, -26, 31, -4, -4, 6, -5, 20, -19, 7, -61]
Sum of List: 0
'''