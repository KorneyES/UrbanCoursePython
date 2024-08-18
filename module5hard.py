#Каждый объект класса User должен обладать следующими атрибутами и методами:
#Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
#Каждый объект класса Video должен обладать следующими атрибутами и методами:
#Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
#Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
# Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
#Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного.
# Помните, что password передаётся в виде строки, а сравнивается по хэшу.
#Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname).
#Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
#Метод log_out для сброса текущего пользователя на None.
#Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
#Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
#Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
#После текущее время просмотра данного видео сбрасывается.
#Для метода watch_video так же учитывайте следующие особенности:
#Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
#Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
#Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
#После воспроизведения нужно выводить: "Конец видео"

from time import sleep as sl
class User:                                                                                                             #???зочем
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        #self.user = [self.nickname, self.password, self, age]

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []                                                                                                 #users list form
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):                                                                        #rega
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)                                                                                     #users list +
        self.current_user = new_user
        print(f'Пользователь {nickname} успешно зарегистрирован и вошёл в систему')


    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f'Пользователь {nickname} успешно вошёл в систему')
                return
        print('Неправильный логин или пароль')


    def log_out(self):
        if self.current_user:
            print(f'{self.current_user.nickname} вышел из системы')
        self.current_user = None


    def add(self, *videos):
        for video in videos:
            if any(vid.title == video.title for vid in self.videos):
                print(f'Видео с названием {video.title} уже есть')
            else:
                print(f'Видео {video.title} добавлено')
                self.videos.append(video)                                                                               #video list +


    def get_videos(self, searching_form):
        searching_form_lower = searching_form.lower()
        result = [video.title for video in self.videos if searching_form_lower in video.title.lower()]
        if result:
            return result
        else:
            print('Ничего не найдено, попробуй поискать что-нибудь ещё!')


    def watch_video(self, title):
        if not self.current_user:                                                                                       #acc check
            print('Войдите в аккаунт для просмотра')
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Несовершеннолетним доступ запрещён')
                else:
                    print(f'Начало воспроизведения {video.title}')
                    for sec in range(video.time_now, video.duration):
                        print(f'Время просмотра: {sec} сек')
                        sl(1)
                    video.time_now = 0
                    print('Видео закончилось, как насчёт нового запроса?')
        print('Ничего не найдено, попробуй поискать что-нибудь ещё!')


#urtube = UrTube()
#urtube.register('Amogus', 'password123', 54)
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.watch_video('Лучший язык программирования 2024 года!')