from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main_kb = [
    [KeyboardButton(text='Каталог'),
     KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Мой профиль'),
     KeyboardButton(text='Контакты')]
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')

socials = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Telegram', url='https://t.me/sudoteach')],
    [InlineKeyboardButton(text='YouTube', url='https://youtube.com/@sudoteach')]
])

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Смарт-часы", callback_data= 'smart watch')],
    [InlineKeyboardButton(text="Смарт-браслеты", callback_data='smart bracelets')],
    [InlineKeyboardButton(text="Беспроводные наушники", callback_data='wireless headphones')],
    [InlineKeyboardButton(text="Колонки", callback_data='smart speaker')]
])

main_kb = [
    [KeyboardButton(text='Каталог'),
     KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Мой профиль'),
     KeyboardButton(text='Контакты')]
]

admin_panel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить товар', callback_data='add_product')],
    [InlineKeyboardButton(text='Удалить товар', callback_data='del_product')],
    [InlineKeyboardButton(text='Сделать рассылку', callback_data='share')]
     ],
    resize_keyboard=True)