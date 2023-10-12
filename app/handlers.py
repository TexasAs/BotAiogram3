from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from dotenv import load_dotenv
import os
import app.keyboard as kb


load_dotenv()
router = Router()


# COMAND START
@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать!', reply_markup=kb.main)

'''
# AUTORIZATION ADMIN
class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in [int(os.getenv('ADMIN_ID'))]

@router.message(Admin(), F.text == '/admin')
async def cmd_admin(message: Message):
    await message.answer('Вы админ', reply_markup=kb.admin_panel)
'''










# ADD PRODUCT
#@form_router.message(CommandStart())
#async def command_start(message: Message, state: FSMContext) -> None:
#    await state.set_state(Form.name)
#    await message.answer(
#        "Hi there! What's your name?",
#        reply_markup=ReplyKeyboardRemove(),
#    )
'''
@router.message(text=['Добавить товар'])
async def add_item(message: Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await NewOrder.type.set()
        await message.answer("Выберите тип товара", reply_markup=kb.catalog)
    else:
        await message.reply(f'{message.from_user.first_name} выберите из предложенных вариантов')

@router.callback_query_handler(state=NewOrder.type)
async def add_item_type(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = call.data
    await call.message.answer("Напишите название товара", reply_markup=kb.cancel)
    await NewOrder.next()
'''









# CATALOG !!!
@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию', reply_markup=kb.catalog)


@router.callback_query(F.data == 'smart watch')     # у каллбака нет текста есть дата
async def adidas(callback: CallbackQuery):
    await callback.message.answer(f'Вы выбрали {callback.data}')   # обращатся к message нужно только через callback






# Пример отправки картинок
@router.message(F.text == '/send_image')
async def cmd_send_image(message: Message):
    await message.answer_photo(photo='url',
                               caption='описание')


# Пример обработки фотографий
@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(message.photo[-1].file_id)


# Пример отправки документов
@router.message(F.text == '/send_doc')
async def cmd_send_doc(message: Message):
    await message.answer_document(document='id',
                                  caption='описание')

# Пример обработки документов
@router.message(F.document)
async def get_document(message: Message):
    await message.answer(message.document.file_id)


# Хэндлер без фильтра, сработает, если ни один выше не сработает.
@router.message()
async def echo(message: Message):
    await message.answer('Я тебя не понимаю...')
