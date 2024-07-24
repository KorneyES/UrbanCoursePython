#Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала нужный пароль result, для одного введённого числа.

number = int(input("Введите число от 3 до 20: "))

result = []
for i in range(1, number + 1):
    for j in range(1, number + 1):
        if (i + j) % number == 0 and i < j:
            result.append(str(i) + str(j))

print(f"Пасс для {number} -> {result}")


#3 - 12
#4 - 13
#5 - 1423
#6 - 121524
#7 - 162534
#8 - 13261735
#9 - 1218273645
#10 - 141923283746
#11 - 11029384756
#12 - 12131511124210394857
#13 - 112211310495867
#14 - 1611325212343114105968
#15 - 1214114232133124115106978
#16 - 1317115262143531341251161079
#17 - 11621531441351261171089
#18 - 12151811724272163631545414513612711810
#19 - 118217316415514613712811910
#20 - 13141911923282183731746416515614713812911