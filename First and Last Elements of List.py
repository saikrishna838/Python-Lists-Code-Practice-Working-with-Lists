n = int(input())

numbers = []
for i in range(1, n + 1):
    num = int(input())
    if i <=2:
        numbers = numbers + [num]
    elif (i == n-1) or (i == n)  :
        numbers = numbers + [num]
print(numbers)
    
        