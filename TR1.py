number_1 = int(input('enter your first number: '))
number_2 = int(input('enter your second number: '))


if number_1 < 0 or number_1 > 20 or number_2 < 0 or number_2 > 20:
    print('Number must be between 0 and 20. Try again')
else:
    miyangin = (number_1 + number_2) / 2
    
    if miyangin >= 10:
        print(f"PASS SHODI ba {miyangin}")
    else:
        print(f"OFTADI ba {miyangin}")