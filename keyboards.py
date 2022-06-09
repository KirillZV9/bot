from aiogram import *
from config.config import *


### reply kb
kb_sendContact = types.ReplyKeyboardMarkup().row(
    types.KeyboardButton(text="Поделиться контактом", callback_data="number", request_contact=True),
)
###

### reply kb_goToApp
kb_comeToApp = types.InlineKeyboardMarkup().row(
    types.InlineKeyboardButton(text="Закончить регистрацию", callback_data="REG_FINISHED")
)