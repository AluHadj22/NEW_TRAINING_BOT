from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp
from aiogram import types
from aiogram.dispatcher import Dispatcher




class Form(StatesGroup):
    gender = State()
    age = State()
    height = State()
    weight = State()
    weight_loss_goal = State()

# Обработчик команды /start
@dp.message_handler(commands=['calories'])
async def command_call(message: types.Message):
    await Form.gender.set()
    await message.reply("Привет! Давай начнем. Введите ваш пол (м/ж):")

# Обработчик ответа на вопрос о поле
@dp.message_handler(state=Form.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
    await Form.next()
    await message.reply("Введите ваш возраст:")

# Обработчик ответа на вопрос о возрасте
@dp.message_handler(state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await Form.next()
    await message.reply("Введите ваш рост в сантиметрах:")

# Обработчик ответа на вопрос о росте
@dp.message_handler(state=Form.height)
async def process_height(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['height'] = message.text
    await Form.next()
    await message.reply("Введите ваш вес в килограммах:")

# Обработчик ответа на вопрос о весе
@dp.message_handler(state=Form.weight)
async def process_weight(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['weight'] = message.text
    await Form.next()
    await message.reply("Выберите вариант похудения:\n1. Похудеть и сохранить мышцы\n2. Похудеть быстро\n3. Похудеть постепенно")

# Обработчик ответа на вопрос о варианте похудения
@dp.message_handler(state=Form.weight_loss_goal)
async def process_weight_loss_goal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['weight_loss_goal'] = message.text
    
    # Вычисление калорийного дефицита в зависимости от варианта похудения
    weight_loss_goal = data['weight_loss_goal']
    if weight_loss_goal == '1':
        # Вычисление калорийного дефицита для сохранения мышц
        if data['gender'] == 'м':
            bmr = 88.362 + (13.397 * int(data['weight'])) + (4.799 * int(data['height'])) - (5.677 * int(data['age']))
            with_muscles = int(bmr + 480 - 300)    # С сохранением мышц
        else:
            bmr = 447.593 + (9.247 * int(data['weight'])) + (3.098 * int(data['height'])) - (4.330 * int(data['age']))
            with_muscles = int(bmr + 550 - 300)    # С сохранением мышц
        await message.reply("Ваш вариант дефицита калорий:  " + str(with_muscles) + '  для сохранения мышц')
    elif weight_loss_goal == '2':
        if data['gender'] == 'м':
            bmr = 88.362 + (13.397 * int(data['weight'])) + (4.799 * int(data['height'])) - (5.677 * int(data['age']))
            quick_loss = int(bmr + 400 - 500)      # Быстрое похудение
        else:
            bmr = 447.593 + (9.247 * int(data['weight'])) + (3.098 * int(data['height'])) - (4.330 * int(data['age']))
            quick_loss = int(bmr + 600 - 450)      # Быстрое похудение
        await message.reply("Ваш вариант дефицита калорий:  " + str(quick_loss) + '  Это быстрое похудение')
    elif weight_loss_goal == '3':
        if data['gender'] == 'м':
            bmr = 88.362 + (13.397 * int(data['weight'])) + (4.799 * int(data['height'])) - (5.677 * int(data['age']))
            optimal_loss = int(bmr + 500 - 250)
        else:
            bmr = 447.593 + (9.247 * int(data['weight'])) + (3.098 * int(data['height'])) - (4.330 * int(data['age']))
            optimal_loss = int(bmr + 559 - 250)
        await message.reply("Ваш вариант дефицита калорий: " + str(optimal_loss) + '  Это оптимальное похудение')
        
    await state.update_data(**data)
    await state.finish()



def register_handlers_call(dp : Dispatcher):
    dp.register_message_handler(command_call, commands=['calories'])
    dp.register_message_handler(process_gender, state=Form.gender )
    dp.register_message_handler(process_age, state=Form.age )
    dp.register_message_handler(process_height, state=Form.height )
    dp.register_message_handler(process_weight, state=Form.weight )
    dp.register_message_handler(process_weight_loss_goal, state=Form.weight_loss_goal )