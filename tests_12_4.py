import unittest
import logging
from rt_with_exceptions import Runner
from rt_with_exceptions import Tournament


logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s - %(message)s'
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner(name="John", speed=-5)
        except ValueError as e:
            logging.warning('Неверная скорость для Runner: %s', e)
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(name=123, speed=10)
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
        else:
            logging.info('"test_run" выполнен успешно')

if __name__ == '__main__':
    unittest.main()
