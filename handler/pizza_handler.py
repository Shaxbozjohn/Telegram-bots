from aiogram.types import Message
from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import ChatTypeFilter
from data.database import User, add_user, Session, Product
from sqlalchemy import func
from keyboards.main_keyboard import start_keyboard2,start_keyboard
from keyboards.inline_keyboard import inline_keyboard1, inline_keyboard5, inline_keyboard4

@dp.message_handler(text="🍴Menyu")
async def cmd_start(message: types.Message):
    await message.answer(f"Kategoriyani tanlang!",
                         reply_markup=start_keyboard2)

@dp.message_handler(text="🍕Pizza")
async def cmd_start(message: types.Message):
    await message.answer(f"O'zingizga yoqqan pitsani tanlang!",
                         reply_markup=inline_keyboard1,
                        )
#
# @dp.message_handler(text="🍹Ichimliklar")
# async def cmd_start(message: types.Message):
#     await message.answer(f"O'zingizga yoqqan icgimlikni tanlang!",
#                          reply_markup=inline_keyboard7,

@dp.message_handler(text="🔙Orqaga")
async def cmd_start(message: types.Message):
    await message.answer(f"{message.from_user.full_name} siz bosh menyuga qaytdingiz✔️",
                         reply_markup=start_keyboard)

@dp.callback_query_handler(text="paperonpizza")
async def cmd_peperon(call: types.CallbackQuery):
    photo = open('menu_image/photo_2023-09-24_19-20-06.jpg', "rb")
    session = Session()
    menyu = session.query(Product).filter(Product.id == 1).first()
    if menyu:
        product_name = menyu.product_name
        await call.message.answer_photo(photo=photo, caption= f"Pizza name: {product_name}\n",
                                  reply_markup=inline_keyboard4)
    else:
        await call.message.answer("No pizza found with that id.")


@dp.callback_query_handler(text="belissimopizza")
async def cmd_peperon(call: types.CallbackQuery):
    photo = open('menu_image/beli.jpg', "rb")
    session = Session()
    menyu = session.query(Product).filter(Product.id == 2).first()
    if menyu:
        product_name = menyu.product_name
        await call.message.answer_photo(photo=photo, caption=f"Pizza name: {product_name}\n",
                                        reply_markup=inline_keyboard4)
    else:
        await call.message.answer("No pizza found with that id.")


# @dp.callback_query_handler(text="paperonpizza")
# async def cmd_paper(call: types.CallbackQuery):
#     photo = open('photos/photo_2023-09-24_19-20-06.jpg', "rb")
#     await call.message.answer_photo(photo=photo, caption=f"Pepperoni", reply_markup=inline_keyboard5)



# @dp.message_handler(text='savat')
# async def buy_product(message: types.Message):
#    session = Session()
#    # Parse the product name from the message
#    product_name = message.get_args()
#
#    # Query the product from the database
#    product = session.query(Product).filter_by(product_name=product_name).first()
#
#    if product:
#        # Create a new Basket record
#        basket = Basket(product=product)
#        session.add(basket)
#        session.commit()
#
#        await message.answer(f"You have successfully purchased {product_name}!")
#    else:
#        await message.answer("Product not found.")
































@dp.callback_query_handler(text="ma38000")
async def cmd_paper(call: types.CallbackQuery):
    await call.message.answer(text= "Pitsa narxi: 38000so'm",reply_markup=inline_keyboard4)

@dp.callback_query_handler(text="ma52000")
async def cmd_paper(call: types.CallbackQuery):
    await call.message.answer(text= "Pitsa narxi: 52000so'm", reply_markup=inline_keyboard4)

@dp.callback_query_handler(text="ma62000")
async def cmd_paper(call: types.CallbackQuery):
    await call.message.answer(text="Pitsa narxi: 62000so'm", reply_markup=inline_keyboard4)
