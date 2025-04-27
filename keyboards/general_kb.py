from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def starting_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Информация')
    kb.button(text='Подать заявку')
    kb.button(text='Поддержать проект')
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)