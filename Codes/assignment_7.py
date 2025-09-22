from math import sqrt

a = int(input('Enter co-efficient of x^2: '))
b = int(input('Enter co-efficient of x: '))
c = int(input('Enter co-efficient of constant: '))

val1, val2 = ((-b + sqrt(b**2 - 4*a*c))/2, (-b - sqrt(b**2 - 4*a*c))/2)

print(f'The roots of the quadratic equations are {val1} and {val2}')