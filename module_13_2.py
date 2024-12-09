from aiogram import  Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

# Задача "Бот поддержки (Начало)":
# К коду из подготовительного видео напишите две асинхронные функции:

api = 'key'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# @dp.message_handler(text= ['Aboba', 'ff'])
# async def urban_messa(message):
#     print('Urban message')

# start(message) - печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.' . Запускается только когда написана команда '/start' в чате с ботом. (используйте соответствующий декоратор)
@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')

# all_massages(message) - печатает строку в консоли 'Введите команду /start, чтобы начать общение.'. Запускается при любом обращении не описанном ранее. (используйте соответствующий декоратор)
@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')

# Запустите ваш Telegram-бот и проверьте его на работоспособность.
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)