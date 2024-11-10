import random

numbers = [random.randint(-10, 10) for _ in range(20)]

min = min(numbers)
max = max(numbers)

negative = sum(1 for num in numbers if num < 0)
positive = sum(1 for num in numbers if num > 0)
zero = numbers.count(0)

print("List of numbers:", numbers)
print("Minimum element:", min)
print("Maximum element:", max)
print("Number of negative elements:", negative)
print("Number of positive elements:", positive)
print("Number of zeros:", zero)
