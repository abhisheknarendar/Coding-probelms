#Find the smallest number in a list
numbers = [5, 3, 8, 6, 7, 2]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print(smallest)