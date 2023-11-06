def calculate_percentage(number, percentage):
    return (number * percentage) / 100

# Example usage:
number = int(input("Enter the number: "))
percentage = int(input("Enter the percentage: "))

result = calculate_percentage(number, percentage)
print(f"{percentage}% of {number} is: {result}")

