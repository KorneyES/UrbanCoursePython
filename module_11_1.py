# Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
# После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями. К каждой библиотеке дана ссылка на документацию ниже.
# Если вы выбрали:
# В приложении к ссылке на GitHub напишите комментарий о возможностях, которые предоставила вам выбранная библиотека и как вы расширили возможности Python с её помощью.
# Примечания:
# Можете выбрать не более 3-х библиотек для изучения.
# Желательно продемонстрировать от 3-х функций/классов/методов/операций из каждой выбранной библиотеки.

import numpy
import numpy as np
import requests
import requests as rq
import pandas as pd

# pandas
pd_data = {'Name' : ['Vladislav', 'Alexei', 'Roman', 'Maxim'],
           'Age' : [53,38,33,24],
           'City': ['Novak', 'Samara', 'Samara', 'Novak']
}
unsorted_matrix = pd.DataFrame(pd_data)
print(unsorted_matrix)
print('-------------')
filtered_matrix = unsorted_matrix[unsorted_matrix['Age'] > 30]
print(filtered_matrix)
print('-------------')
# requests
url = 'https://urban-university.ru/work-garantee'
response = requests.get((url))

if response.status_code == 200:
    print('Request successful!')
    print('Answer status:', response.status_code)
else:
    print('Unsuccessful request!')
    print('Answer status:', response.status_code)
print('-------------')
# numpy
array_1 = np.array([1,2,3,4,5])
array_2 = np.array([6,7,8,9,10])

print(array_1 - array_2)
print(array_1 * array_2)
print(numpy.mean(array_2))


