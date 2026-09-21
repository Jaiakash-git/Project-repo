numbers = []

n = int(input("Enter how many natural numbers: "))

for i in range(1, n + 1):
    numbers.append(i)

total = sum(numbers)

print("Natural numbers are:", numbers)
print("Sum =", total)
