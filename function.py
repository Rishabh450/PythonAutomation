def greet_user(name):
    print(f'Hi there!{name}')
    print('Welcome Abroad')


greet_user("Shraddha")

try:
    age = int(input("Enter Age : "))
    print(age)
except ValueError:
    print('Invalid')



