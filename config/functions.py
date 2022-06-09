from config.config import *
from keyboards import *

async def verificationCodeAwaiting(message, types):
    await message.answer("*Для успешной регистрации нажмите на кнопку ниже. \nВам придет код для подтверждения в приложении.*", 
    parse_mode = types.ParseMode.MARKDOWN,
    reply_markup = kb_comeToApp)
    