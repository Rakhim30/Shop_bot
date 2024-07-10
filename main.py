import asyncio
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import token , dp , admin
from aiogram import F
from aiogram.filters.command import CommandStart,Command
from aiogram.types import Message,CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup
from button import *
from aiogram.fsm.state import State,StatesGroup
from aiogram.filters import Filter,StateFilter
from states import *
from db import*


@dp.callback_query(StateFilter('*'),F.data=='back')
async def go_start(call: CallbackQuery,state:FSMContext):
    first_name = call.message.from_user.first_name
    await call.message.answer(f'{first_name}', reply_markup=but)
    await state.set_state(My_State.starts)

@dp.message(Command("start"))
async def go_start(message: Message,state:FSMContext):
    first_name = message.from_user.first_name
    await message.answer_photo(photo='https://images.khmer24.co/profiles/pictures/23-08-07/53268422b7724df553ce3658972311811691389971453396904907.jpg', caption=f'Assalomu alaykum {first_name}', reply_markup=but)
    await state.set_state(My_State.starts)                      


@dp.message(F.text=='🧑🏻‍💻 Admin', My_State.starts)
async def go_start(message: Message,state:FSMContext):
    user_id = message.from_user.id
    if 554507627 == user_id:
        await message.answer(f'Admin', reply_markup=a.as_markup())
        await state.set_state(My_State.adv)
    else:    
        first_name = message.from_user.first_name
        await message.answer("Adminga otish:", reply_markup=adm.as_markup())
        await state.clear()

@dp.callback_query(F.data=='add',My_State.adv)
async def ad(call:CallbackQuery, state: FSMContext):
    await call.message.answer(f'Add Id:')
    await state.set_state(My_State.osh)
    
@dp.message(F.text,My_State.osh)
async def ad(message:Message, state: FSMContext):
    await message.answer(f'Add name:')
    text = message.text
    await state.update_data({'id':text})
    await state.set_state(My_State.name)
    
@dp.message(F.text,My_State.name)
async def ad(message:Message, state: FSMContext):
    await message.answer(f'Add price:')
    text = message.text
    await state.update_data({'name':text})
    await state.set_state(My_State.prise)
    
@dp.message(F.text,My_State.prise)
async def ad(message:Message, state: FSMContext):
    await message.answer(f'Add URL(picture):')
    text = message.text
    await state.update_data({'prise':text})
    await state.set_state(My_State.imgg)
    
@dp.message(F.text,My_State.imgg)
async def ad(message:Message, state: FSMContext):
    await message.answer(f'Add description:')
    text = message.text
    await state.update_data({'img':text})
    await state.set_state(My_State.up)
    
@dp.message(F.text,My_State.up)
async def ad(message:Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    i = data.get('id')
    n = data.get('name')
    p = data.get('prise')
    imp = data.get('img')
    d = data.get('dict')
    cread_add(i,n,p,imp,text)
    await message.answer(f'Added!', reply_markup=back.as_markup())
    await state.clear()

@dp.callback_query(F.data=='dele',My_State.adv)
async def as_start(call:CallbackQuery,state:FSMContext):
    await call.message.answer(f'Chose products',reply_markup=product.as_markup())
    await state.set_state(My_State.low)

@dp.callback_query(F.data,My_State.low)    
async def deel(call:CallbackQuery,state:FSMContext):
    tw = call.data
    delet(tw)
    await call.message.answer('Deleted',reply_markup=back.as_markup())
    await state.clear()

@dp.message(F.text=='🛒 Korzina',My_State.starts)
async def carts(m:Message, state:FSMContext):
    user = m.from_user.id
    summm = ''
    for i in create_read():
        if user == i[0]:
            e = i[2] * i[3]
            summm += f'Name:{i[1]} \n Price:{i[2]} Quantity:{i[3]} \n\n'
    await m.answer(f'{summm}{e}',reply_markup=d.as_markup())
    await state.set_state(My_State.dele)

@dp.message(F.text=='🛍 Shoping',My_State.starts)
async def as_start(message: Message,state:FSMContext):
    await message.answer(f'Products',reply_markup=product.as_markup())
    await state.set_state(My_State.s_shop)

@dp.callback_query(F.data,My_State.s_shop)
async def reg_one(call: CallbackQuery, state: FSMContext):
    text=call.data
    print(text)
    for i in file['products']:
        if i['title'] == text:
            img=i['images'][0]
            dest=i['description']
            price=i['price']
            await state.update_data({'name':text,'price':price})
    await call.message.answer_photo(photo=f'{img}', caption=f"Name: {text}\n\nPrice: {price}\n\nDescription:{dest}",reply_markup=product2.as_markup())
    await state.set_state(My_State.son)

@dp.callback_query(F.data=="karzinka",My_State.son)
async def reg_one(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text="Qancha dona kerak:" , reply_markup=number.as_markup())
    await state.set_state(My_State.base)

@dp.callback_query(F.data,My_State.base)
async def find(call:CallbackQuery,state:FSMContext):
    a=await state.get_data()
    name=a.get('name')
    price=a.get("price")
    user = call.from_user.id
    text = call.data
    for i in range(1,10):
        if text == str(i):
            s=i
    create_add(user,name,price,s)
    await call.message.answer('koshildi', reply_markup=back.as_markup())

@dp.callback_query(F.data == 'dele',My_State.dele)
async def deel(call:CallbackQuery,state:FSMContext):
    user = call.from_user.id
    b = InlineKeyboardBuilder()
    for i in create_read():
        if user == i[0]:
            b.add(InlineKeyboardButton(text=i[1], callback_data=i[1]))
    b.add(InlineKeyboardButton(text='Orqaga', callback_data='back'))
    await call.message.answer(f'Ochirmoqchi bolganingizni tanlang', reply_markup=b.as_markup())
    await state.set_state(My_State.a)

@dp.callback_query(F.data,My_State.a)    
async def deel(call:CallbackQuery,state:FSMContext):
    tw = call.data
    delete(tw)
    await call.message.answer('Ochirildi',reply_markup=back.as_markup())
    await state.clear()

async def main():
    await dp.start_polling(token)

asyncio.run(main())