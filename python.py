

def loopp(lisst):
    for i in lisst:
        if type(i) is int:
            print(f'Цифра {i}')
        else:
            print(f'Буква {i}')

loopp([1,2,'f',6])


