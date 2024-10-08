#Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
#На вход даны следующие данные:
#Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
#Например: 'Aaron' - [5, 3, 3, 5, 4]
#Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
#Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort_stud = sorted(students)
avr_mark = []
#print(sort_stud)
for grade in grades:
    avr_m = sum(grade) / len(grade)
    avr_mark.append(avr_m)
#print(avr_mark)
result_dict = dict(zip(sort_stud, avr_mark))
print(result_dict)