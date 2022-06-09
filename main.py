from plistlib import UID
from re import A
from aiogram import *
from config.config import *
from keyboards import *
import requests
import user_model
### configuring bot
bot = Bot(token = token)
dp = Dispatcher(bot)
###

######### main handlers

global uid
global phone
global chatid


### asking to share
@dp.message_handler(commands = ['start'])
async def welcome(message: types.message):
    await message.answer("*Добро пожаловать!*\nДля продолжения поделитесь своим номером телефона с ботом.", 
    parse_mode = types.ParseMode.MARKDOWN,
    reply_markup = kb_sendContact)
    

# confirming sharing
@dp.message_handler(content_types=['contact'])
async def contact(message):
    await message.answer("*Для успешной регистрации нажмите на кнопку ниже. \nВам придет код для подтверждения в приложении.*", 
    parse_mode = types.ParseMode.MARKDOWN,
    reply_markup = kb_comeToApp)
    global uid
    uid = message.contact.user_id
    global phone
    phone = message.contact.phone_number
    global chatid
    chatid = message.chat.id


@dp.callback_query_handler(lambda data: data.data == "REG_FINISHED")
async def sendCode(message):
    global phones
    global uid
    # REMOVE TO CFG
    response = requests.get(f"{api_url}={uid}&telNum={phone}")
    global chatid
    await bot.send_message(chat_id=chatid, text=f"*Ваш код подтверждения: *{response.text}\n\nВведите его в приложении", parse_mode=types.ParseMode.MARKDOWN)


# default messages handler
@dp.message_handler()
async def unknownMessages(message: types.Message):
    await bot.send_message(message.chat.id, text="*Я не понимаю эту команду.*", parse_mode = types.ParseMode.MARKDOWN)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

