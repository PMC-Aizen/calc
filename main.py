import math
import string

mode = 0
errorMessage = 'Выбранного режима не существует!'
expressionPromt = 'Введите выражение: '
userModeChoice = int(input('Выберите режим работы: 1 - обычные выражения, 2 - вычисление факториала числа: '))

def isValidExpression(arg: str):
    for word in expression:
        if (word.lower() in string.ascii_lowercase):
            print('Невалидное выражение!')
            return False
        elif word == '@':
            print('САМ ТЫ СОБАКА!!!')
            return False
    
    return True

if (math.isnan(userModeChoice)):
    print(errorMessage)
else:
    if (userModeChoice in range(1, 3)):
        mode = userModeChoice

        if (mode == 1):
            expression = input(expressionPromt)
            
            if (isValidExpression(expression)):
                print(f'Ответ: {eval(expression)}')
        if (mode == 2):
            expression = input(expressionPromt)

            if (isValidExpression(expression)):
                print(f'Ответ: {math.factorial(int(expression))}')
    else:
        print(errorMessage)
