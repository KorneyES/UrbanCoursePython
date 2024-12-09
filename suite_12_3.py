import unittest
from module_12_1 import RunnerTest  # Импортируйте ваш тест RunnerTest
from module_12_2 import TournamentTest  # Импортируйте ваш тест TournamentTest

# Декоратор для пропуска тестов
def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_func(self, *args, **kwargs)
    return wrapper

# Обновление классов тестов
class RunnerTest(unittest.TestCase):
    is_frozen = False  # Атрибут для контроля заморозки

    @skip_if_frozen
    def test_challenge(self):
        # Ваш тестовый код
        pass

    @skip_if_frozen
    def test_run(self):
        # Ваш тестовый код
        pass

    @skip_if_frozen
    def test_walk(self):
        # Ваш тестовый код
        pass

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Атрибут для контроля заморозки

    @skip_if_frozen
    def test_first_tournament(self):
        # Ваш тестовый код
        pass

    @skip_if_frozen
    def test_second_tournament(self):
        # Ваш тестовый код
        pass

    @skip_if_frozen
    def test_third_tournament(self):
        # Ваш тестовый код
        pass

# Создание тестового набора
test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(RunnerTest))
test_suite.addTest(unittest.makeSuite(TournamentTest))

# Запуск тестов
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
