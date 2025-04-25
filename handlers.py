from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram import Router, F

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer('Hello')