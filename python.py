def loopp(lisst):
    for i in lisst:
        if type(i) is int:
            print(f'Цифра {i}')
            if i<=0:
                print(f'{i} мало')
        else:
            print(f'Буква {i}')

loopp([1,2,'f',6,-5])


