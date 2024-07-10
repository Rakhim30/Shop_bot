from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import requests as rq
from api import*
url = 'https://dummyjson.com/products'
file = rq.get(url).json()

but = ReplyKeyboardMarkup(    
    keyboard=[
        [KeyboardButton(text='🛍 Shoping'),KeyboardButton(text='🛒 Korzina')],
        [KeyboardButton(text='🧑🏻‍💻 Admin')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

number = InlineKeyboardBuilder()
for i in range(1,10):
    number.add(InlineKeyboardButton(text=str(i), callback_data=str(i)))
number.adjust(3)

product = InlineKeyboardBuilder()


for row in cread_read():
    data = row[1]
    product.add(InlineKeyboardButton(text=data, callback_data=data))
product.add(InlineKeyboardButton(text='Back',callback_data='back'))
product.adjust(3)
print(product)

product2 = InlineKeyboardBuilder()
product2.add(InlineKeyboardButton(text="Add korzinka", callback_data='karzinka'))
back = InlineKeyboardBuilder()
back.add(InlineKeyboardButton(text="back", callback_data='back'))
d = InlineKeyboardBuilder()
d.add(InlineKeyboardButton(text="Delete", callback_data='dele'))
d.add(InlineKeyboardButton(text='Back', callback_data='back'))

adm = InlineKeyboardBuilder()     
adm.add(InlineKeyboardButton(text='Admin', callback_data='adm', url='https://t.me/imomaddin30'))

a = InlineKeyboardBuilder()
a.add(InlineKeyboardButton(text='Add', callback_data='add'))
a.add(InlineKeyboardButton(text='Delete', callback_data='dele'))
a.add(InlineKeyboardButton(text='Back', callback_data='back'))