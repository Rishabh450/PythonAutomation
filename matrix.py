
matrix =[
    [1, 2 ,3],
    [4, 5 ,5],
    [7, 7 ,8]
]
#remove append insert pop index
matrix.remove([1, 2, 3])
matrix.insert(0, [1, 2, 3])
matrix.insert(2, [2, 3, 8])


print(matrix)

for row in matrix:
    for item in row:
        print(item , end=" ")
    print()
#returns error if there is no such element
print(matrix.index([1, 2, 3]))

#in operator is safer than index() if we wanna check existenca
print([1, 2, 3] in matrix)

numbers = [5, 4, 3, 5, 8, 10, 9]

#frequency of element in list count
print(numbers.count(5))
numbers.sort()
numbers.reverse()
print(numbers)



