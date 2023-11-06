'''def calculate_percentage(number, percentage):
    return (number * percentage) / 100

# Example usage:
number = int(input("Enter the number: "))
percentage = int(input("Enter the percentage: "))


result = calculate_percentage(number, percentage)
print(f"{percentage}% of {number} is: {result}")


Total = int(input("Enter diff amount": + {result}))'''
def calculate_percentage(number, percentage):
    return (number * percentage) / 100

# Example usage:
number = int(input("Enter the number: "))
percentage = int(input("Enter the percentage: "))

result = calculate_percentage(number, percentage)
print(f"{percentage}% of {number} is: {result}")

# Asking for an additional input
#total = int(input(f"Enter an additional amount to add to {result}: "))
#final_total = result + total
#print(f"Total after adding {total}: {final_total}")

Total = int(input(f"Enter an additional amount to add to {result} + "))
final_amount = result + Total
print(f"Total amount after adding {Total} is {final_amount}")
