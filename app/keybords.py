from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Каталог'),
        KeyboardButton(text='Корзина')],
        [KeyboardButton(text='Контакты')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт ниже'
)

inline_main = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text='Каталог', callback_data='catalog'),
     InlineKeyboardButton(text='Корзина', callback_data='cart')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])

back = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text='назад', callback_data='catalog')]
])


async def catalog_builder():
    brands = ['Nike', 'Adidas', 'Puma', 'Reebok', 'New Balance', 'Converse', 'Vans', 'Under Armour', 'Asics']
    keybord = InlineKeyboardBuilder()
    for brand in brands:
        keybord.add(InlineKeyboardButton(text=brand, callback_data=f"item_{brand}"))
    return keybord.adjust(2).as_markup()