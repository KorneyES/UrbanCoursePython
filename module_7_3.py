# Задача "Найдёт везде":
# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.
# Также объект класса WordsFinder должен обладать следующими методами:
# get_all_words - подготовительный метод, который возвращает словарь следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
# Где:
# 'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
# ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.

# В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().
#
# for name, words in get_all_words().items():
  # Логика методов find или count

class WordsFinder():
    def __init__(self,*files):
        self.file_names = files

    # Алгоритм получения словаря такого вида в методе get_all_words:
    # Создайте пустой словарь all_words.
    # Переберите названия файлов и открывайте каждый из них, используя оператор with.
    # Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
    # Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
    # Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
    # В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
    def get_all_words(self):
        all_words = {}
        exceptions = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for symbol in exceptions:
                    text = text.replace(symbol, ' ')
                words = text.split()
                all_words[file_name] = words
        return all_words

    # find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
    def find(self, word):
        word = word.lower()
        word_positions = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                word_positions[name] = words.index(word)
            else:
                word_positions[name] = None
        return word_positions

    # count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
    def count(self,word):
        word = word.lower()
        counts = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            counts[name] = words.count(word)
        return counts

texts = WordsFinder('txt1.txt','txt2.txt','txt3.txt')
print(texts.find('Император'))
print(texts.count('Адептус'))
print(texts.count('Freak'))