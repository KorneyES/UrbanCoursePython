#Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
#Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
#Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
#Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
#В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
#Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
#За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.

if_missing = (".com",".ru",".net")

def send_email(message, recipient, sender = "university.help@gmail.com"):
    if '@' not in recipient or not recipient.endswith(if_missing):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif '@' not in sender or not sender.endswith(if_missing):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com',)
send_email('Стас Васильев', 'Kotik@mail.ru')
send_email('Договор на бла-бла-бла', 'sibinkek@chom')

