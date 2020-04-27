secret = 4
i = 1
while i <= 3:
    number = input("Guess")
    if int(number) == secret:
        print('You won')
        break
    else:
        i += 1
if i == 4:
    print("You failed!")

