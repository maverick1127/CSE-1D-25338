num1 = int(input('Enter number 1: '))
num2 = int(input('enter number 2: '))
choice = input('''
add: Addition
sub: Subratcion
mul: Multiplication
div: Division
rem: Remainder
                              
''').lower()

if choice == 'add':
    print(num1 + num2)

if choice == 'sub':
    print(num1 - num2)

if choice == 'mul':
    print(num1 * num2)

if choice == 'div':
    print(num1 / num2)

if choice == 'rem':
    print(num1 % num2)