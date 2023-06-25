list=input()

numbers=[int(num) for num in list.split()]

positive_numbers = []
for num in numbers:
    if num > 0:
        positive_numbers.append(num)

print(positive_numbers)
