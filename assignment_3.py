fr = input('Enter initial unit(km, mi, m): ').lower()
to = input('Enter final unit(km, mi, m): ').lower()

val = float(input('ENter the n=initial value: '))

if fr == 'km':
    if to == 'mi':
        print(val * 0.62)

    if to == 'm':
        print(val * 1000)

if fr == 'm':
    if to == 'mi':
        print(val * 0.00062)

    if to == 'km':
        print(val / 1000)

if fr == 'mi':
    if to == 'km':
        print(val * 1.62)

    if to == 'm':
        print(val * 1609.344)