n = int(input())

numbers = []

for i in range(1, n + 1):
    num = int(input())
    if num % 5 == 0:
        numbers = numbers + [num]
print(numbers)
    