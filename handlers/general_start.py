from aiogram.filters.command import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Router, F
from keyboards.general_kb import starting_kb

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(text='Выберите действие', reply_markup=starting_kb())

@router.message(F.text == 'Информация')
async def info(message: Message):
    await message.answer(text='Некоторая информация')

@router.message(F.text == 'Подать заявку')
async def apply(message: Message):
    await message.answer(text='Передаем вашу заявку...')

@router.message(F.text == 'Поддержать проект')
async def donate(message: Message):
    await message.answer('Перевожу вас на форму оплаты...')