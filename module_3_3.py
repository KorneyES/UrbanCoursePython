#1.Функция с параметрами по умолчанию:
#Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
#Функция должна выводить эти параметры.
#Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
#Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
#2.Распаковка параметров:
#Создайте список values_list с тремя элементами разных типов.
#Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
#Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
#3.Распаковка + отдельные параметры:
#Создайте список values_list_2 с двумя элементами разных типов

def print_params(a = 1, b = 'строка' , c = True):
    print(f"a: {a}, b: {b}, c: {c}")

print_params(3, 'integer')
print_params()
print_params(10, [(1,2),{3,4}])
print()
value_list = [1, 'stroke', False]
value_dict = {'a' : value_list[0], 'b' : value_list[1] ,'c' : value_list[2]}

print_params(*value_list)
print_params(**value_dict)