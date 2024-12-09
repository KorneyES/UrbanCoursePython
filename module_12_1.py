# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

# test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
# test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
# test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов вызываются методы run и walk соответственно.
# Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
# Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.
# Пункты задачи:
# Скачайте исходный код для тестов.
# Создайте класс RunnerTest и соответствующие описанию методы.
# Запустите RunnerTest и убедитесь в правильности результатов.

import unittest
from runner import Runner

# Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
class RunnerTest(unittest.TestCase):

# test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
    def test_walk(self):
        runner = Runner("TestWalker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

# test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100
    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

# test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов вызываются методы run и walk соответственно.
    def test_challenge(self):
        runner1 = Runner("TestRunner1")
        runner2 = Runner("TestRunner2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

# Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()









