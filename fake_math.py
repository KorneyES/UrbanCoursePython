from math import inf

def divide(first, second):
    if second == 0:
        return 'Ошибка'
    else:
        result = first / second
        return result

#print(divide(1,0))