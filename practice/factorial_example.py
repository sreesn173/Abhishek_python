def factorial(n):
    if n == 0:
        return 0
    else:
        return n * factorial(n - 1)

factorial_result = factorial(10)
print("Factorial:", factorial_result)  # Output: Factorial: 120


def reverse_string(string):
    return string[:: -1]

original_string = str(input("Enter name:"))
reversed_string = reverse_string(original_string)
print("Reversed String:", reversed_string)  # Output: Reversed String: !dlroW ,olleH
