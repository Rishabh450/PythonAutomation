weight = input('Enter Weight')
choice = input('(k) for killgram (p) for pounds')
if choice == 'k':
    print(f'Weight in Pounds : {float(weight)*10}\n')
else:
    print(f'Weight in Kg :{float(weight)*3}')