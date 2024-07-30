#Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
#Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.
#Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких ст#руктур он не нашёл.
#Помогите сокурснику осуществить его задумку.
#Что должно быть подсчитано:
#Все числа (не важно, являются они ключами или значениям или ещё чем-то).
#Все строки (не важно, являются они ключами или значениям или ещё чем-то)

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data):
    summ_elements = 0
    if isinstance(data, (int, float)):
        summ_elements += data
    elif isinstance(data, str):
        summ_elements += len(data)
    elif isinstance(data, (list, set, tuple)):
        for item in data:
            summ_elements += calculate_structure_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            summ_elements += calculate_structure_sum(key)
            summ_elements += calculate_structure_sum(value)
    else:
        print('All is broken')

    return summ_elements

result = calculate_structure_sum(data_structure)
print(result)