a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))

if a >= c:
    if a >= b:
        print(a)
    
    else:
        print(b)
else:
    if c >= b:
        print(c)

    else:
        print(b)