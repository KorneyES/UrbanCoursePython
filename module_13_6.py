from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = '7424899623:AAEKTtC5JoVx4eDhk6HT0NhlFWDQ7x9XWl4'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
keyboard.add(button_calculate, button_info)

# Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
# С текстом 'Рассчитать норму калорий' и callback_data='calories'
# С текстом 'Формулы расчёта' и callback_data='formulas'
inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=keyboard)

# Создайте новую функцию main_menu(message), которая:
# Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
# Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)

# Создайте новую функцию get_formulas(call), которая:
# Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
# Будет присылать сообщение с формулой Миффлина-Сан Жеора.
@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(
        'Формула Миффлина-Сан Жеора:\n'
        'Для мужчин: BMR = (10 * вес) + (6.25 * рост) - (5 * возраст) + 5'
    )
    await call.answer()

# Измените функцию set_age и декоратор для неё:
# Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
# Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    calories = (10 * weight) + (6.25 * growth) - (5 * age) + 5
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
