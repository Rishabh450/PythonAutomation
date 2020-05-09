numbers = set([4, 2, 6, 4, 6, 3, 2])
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

