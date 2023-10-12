from aiogram import Router, F

from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Filter

from dotenv import load_dotenv
import os
import app.keyboard as kb


load_dotenv()
router2 = Router()

class NewOrder(StatesGroup):
    type = State()
    name = State()
    desc = State()
    price = State()
    #photo = State()

# AUTORIZATION ADMIN
class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in [int(os.getenv('ADMIN_ID'))]

@router2.message(Admin(), F.text == '/admin')
async def cmd_admin(message: Message):
    await message.answer('Вы админ', reply_markup=kb.admin_panel)


# CATALOG !!!
@router2.message(F.text == 'Добавить товар')
async def catalog(message: Message):
    await message.answer('Выберите категорию', reply_markup=kb.catalog)


#@router2.callback_query(F.data == 'smart watch')     # у каллбака нет текста есть дата
#async def adidas(callback: CallbackQuery):
#    await callback.message.answer(f'Вы выбрали {callback.data}')   # обращатся к message нужно только через callback

@router2.callback_query(F.data == 'smart watch')
async def get_form(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(f'Вы выбрали {callback.data} категорию')
    await state.set_state(NewOrder.type)

@router2.message(F.state == NewOrder.type)
async def get_type(message: Message, state: FSMContext):
    await message.answer(f'Категория товара {message.text}\nТеперь добавьте наименование товара')
    await state.update_data(type=message.text)
    await state.set_state(NewOrder.name)

@router2.message(F.state == NewOrder.name)
async def get_name(message: Message, state: FSMContext):
    await message.answer(f'Наименование товара {message.text}\nТеперь добавьте описание')
    await state.update_data(name=message.text)
    await state.set_state(NewOrder.desc)

@router2.message(F.state == NewOrder.desc)
async def get_desc(message: Message, state: FSMContext):
    await message.answer(f'Наименование товара {message.text}\nТеперь укажите стоимость')
    await state.update_data(desc=message.text)
    await state.set_state(NewOrder.price)

@router2.message(F.state == NewOrder.price)
async def get_price(message: Message, state: FSMContext):
    await message.answer(f'Цена товара {message.text}')
    context_data = await state.get_data()
    await message.answer(f"Сохраненные данные в состоянии:\n"
                         f"{context_data['type']}")

