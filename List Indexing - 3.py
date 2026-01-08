num_elements = int(input())
num_indices = int(input())

numbers = [int(input()) for _ in range(num_elements)]

indices = [int(input()) for _ in range(num_indices)]

for idx in indices:
    print(numbers[idx])

