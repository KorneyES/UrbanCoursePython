#Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word, а далее неограниченную последовательность в параметр *other_words.
#Функция должна составить новый список same_words только из тех слов списка other_words, которые содержат root_word или наоборот root_word содержит одно из этих слов. После вернуть список same_words в качестве результата своей работы.

#Пункты задачи:
#Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
#Создайте внутри функции пустой список same_words, который пополнится нужными словами.
#При помощи цикла for переберите предполагаемо подходящие слова.
#Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
#После цикла верните образованный функцией список same_words.
#Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.

def single_root_words(root_word, *other_words):
    root_word_l = root_word.lower()
    same_words = []
    for word in other_words:
        word_l = word.lower()
        if root_word_l in word_l or word_l in root_word_l:
            same_words.append(word)
    return same_words

print(single_root_words('VoZ','A VOZ i nine tam', 'govnoVoz, mnogo v mire tuplanov i roZ', 'poVozka', 'Lenin - Vozhd'))
print(single_root_words('TON','Tons', 'Tetramagaton', 'TOnometer', 'Sabaton', 'PrOtoN'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
