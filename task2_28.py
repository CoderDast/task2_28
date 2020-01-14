def plus1_minus1(numbers):
    ''' Меняет четные на "1" а нечетные на "-1" '''
    new_list = []   # новый список где будут 1, -1 и 0
    for number in numbers:
        try:               # если введен не integer, пропускает элемент списка
            if int(number) > 0:
                new_list.append(1)
            elif int(number) < 0:
                new_list.append(-1)
            else:
                new_list.append(0)
        except ValueError:
            print ('Вы ввели число некорректно.')
            
    return new_list 


numbers_list = input('Type numbers divided by space\n').split(' ')

new_list= plus1_minus1(numbers_list)

print (f'Полученный список: {new_list}.')