# Создайте и дополните клавиатуры:
# Создайте хэндлеры и функции к ним:

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = 'key'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
# В главную (обычную) клавиатуру меню добавьте кнопку "Купить".
button_buy = KeyboardButton('Купить')
keyboard.add(button_calculate, button_info, button_buy)

# Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4". У всех кнопок назначьте callback_data="product_buying"
inline_keyboard = InlineKeyboardMarkup()
for i in range(1, 5):
    button = InlineKeyboardButton(f'Product{i}', callback_data='product_buying')
    inline_keyboard.add(button)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=keyboard)

# Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).
@dp.message_handler(text=['Купить'])
# Функция get_buying_list должна выводить надписи 'Название: Product<number> | Описание: описание <number> | Цена: <number * 100>' 4 раза.
# После каждой надписи выводите картинки к продуктам. В конце выведите ранее созданное Inline меню с надписью "Выберите продукт для покупки:".
async def get_buying_list(message: types.Message):
    for i in range(1, 5):
        description = f'Описание {i}'
        price = i * 100
        await message.answer(f'Название: Product{i} | Описание: {description} | Цена: {price}')

        await bot.send_photo(message.chat.id, photo='img_path')
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_keyboard)

# Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
@dp.callback_query_handler(text='product_buying')
# Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

# Остальной код для расчета калорий
@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(
        'Формула Миффлина-Сан Жеора:\n'
        'Для мужчин: BMR = (10 * вес) + (6.25 * рост) - (5 * возраст) + 5'
    )
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)

async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)

async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)

async def send_calories(message: types.Message, state: FSMContext):
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
