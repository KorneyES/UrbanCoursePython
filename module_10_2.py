# Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
# В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
# После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
# Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.

import threading
import time
from time import sleep

# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
# Атрибут name - имя рыцаря. (str)
# Атрибут power - сила рыцаря. (int)
class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        if not isinstance(self.name, str) and isinstance(self.power, int):
            raise TypeError('Имя должно быть строкой, сила рыцаря целым числом')
        else:
            self.name = name
            self.power = power
            self.enemies = 100
            self.days = 0

# А также метод run, в котором рыцарь будет сражаться с врагами:
# При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power
            print(f'{self.name} сражается {self.days} дней, осталось {self.enemies} воинов.')

            if self.enemies <= 0:
                print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

knight1 = Knight('Король Артур', 35)
knight2 = Knight('Cэр Ланцеврот', 20)
knight3 = Knight('Сир Мордред', 25)

knight1.start()
knight2.start()
knight3.start()

knight1.join()
knight2.join()
knight3.join()
print('Все битвы закончились!')