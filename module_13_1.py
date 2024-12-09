# Необходимо сделать имитацию соревнований по поднятию шаров Атласа.
import asyncio

# Напишите асинхронную функцию start_strongman(name, power), где name - имя силача, power - его подъёмная мощность. Реализуйте следующую логику в функции:
# В начале работы должна выводиться строка - 'Силач <имя силача> начал соревнования.'
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        # Задержка обратно пропорциональная силе
        await asyncio.sleep(1 / power)
# После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>' с задержкой обратно пропорциональной его силе power. Для каждого участника количество шаров одинаковое - 5.
        print(f'Силач {name} поднял {i} шар.')
# В конце поднятия всех шаров должна выводится строка 'Силач <имя силача> закончил соревнования.'
    print(f'Силач {name} закончил соревнования.')


# Также напишите асинхронную функцию start_tournament, в которой создаются 3 задачи для функций start_strongman. Имена(name) и силу(power) для вызовов функции start_strongman можете выбрать самостоятельно.
async def start_tournament():
    strongman1 = asyncio.create_task(start_strongman('Иван', 10))
    strongman2 = asyncio.create_task(start_strongman('Петр', 5))
    strongman3 = asyncio.create_task(start_strongman('Сергей', 8))

# После поставьте каждую задачу в ожидание (await).
    await strongman1
    await strongman2
    await strongman3

# Запустите асинхронную функцию start_tournament методом run.
asyncio.run(start_tournament())