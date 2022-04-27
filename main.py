#TODO:
import hashlib
from math import *
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
import logging 
import config
import string
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
creator='Pavel Verbytsky'
passw = State()
@dp.message_handler(commands=['start', 'help'])
async def help(message: types.Message):
    await bot.send_message(message.chat.id, md.text('Hi!\nI am genious maths bot!\n ',md.spoiler('I will help you to solve problems!'), '\nPowered by aiogram'))
@dp.message_handler(commands=['stop'])
def stop():
    pass
@dp.message_handler()
async def send_result(message: types.Message):
    if 'цензура' in message.text:
        bot.delete_message(message.chat.id, message.from_user.message_id)
    else:
        try:
            mt=message.text
            if hashlib.md5(mt.encode()).hexdigest()=='d7e8098153cdf2f2dd9bfe87ee801a7a':
                await message.reply(f'token is {config.TOKEN}')
            for x in string.ascii_letters+string.whitespace:
                if x in mt:
                    mt.replace(x, '')
            answ =eval(mt)
        except SyntaxError:
            await message.reply('❌Incorrect syntax!')
        except NameError:
            await message.reply('❌Incorrect syntax!')
        else:
            if str(answ).isdigit():
                await message.reply('✔Your result is: '+str(answ))
            else:
                await bot.send_message(message.chat.id, md.text('㊙㊗🉐💮🤣', md.bold(' You wont get my token! ')))
if __name__=="__main__":
    executor.start_polling(dp, skip_updates=False)