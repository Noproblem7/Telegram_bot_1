from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text="1-dars", callback_data="2-dars")
button2 = InlineKeyboardButton(text="3-dars", callback_data="4-dars")
button3 = InlineKeyboardButton(text="5-dars", callback_data="6-dars")
button4 = InlineKeyboardButton(text="7-dars", callback_data="8-dars")
keyboard.add(button1, button2, button3, button4)
