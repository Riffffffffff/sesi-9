numbers = [8, 3, 12, 4, 7, 2]
numbers = [num if num >= 5 else 0 for num in numbers]
numbers.sort(reverse=True)

print(numbers)