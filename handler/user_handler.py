
from datetime import datetime
import json
from sqlalchemy import delete
from aiogram.types import Message
from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import ChatTypeFilter
from data.database import User, add_user, Session, Product, Basket
from sqlalchemy import func
from keyboards.main_keyboard import start_keyboard

session = Session()


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), commands=['start'])
async def cmd_start(message: types.Message):
    existing_user = session.query(User).filter_by(user_id=message.from_user.id).first()

    if existing_user:
        await message.answer(f"Salom {message.from_user.full_name} xush kelibsiz",
                             reply_markup = start_keyboard)
    else:
        await add_user(
            full_name=message.from_user.full_name,
            user_id=message.from_user.id,
            data_register= datetime.now()

        )
        await message.answer(f"Salom {message.from_user.full_name} xush kelibsiz",
                             reply_markup=start_keyboard)

@dp.message_handler(text = "🔖Statistika")
async def cmd_users(message: types.Message):
    session = Session()

    count = session.query(func.count(User.user_id)).scalar()
    # count_left = session.query(func.count(User.username)).filter(User.left_bot == True).scalar()



    if count:
        await message.answer(f"Jami obunachilar soni:  {count} - kishi\n"
                             f"Bugungi kun: {datetime.now().strftime('%d-%m-%Y')}📆\n"
                             f"Hozirgi vaqt: {datetime.now().strftime('%H:%M:%S')}⏱"
                             )


#


@dp.callback_query_handler(text='savat')
async def buy_product(call: types.CallbackQuery):

   # product_name = call.get_args()
   data_dict = json.loads(str(call))
   caption = data_dict['message']['caption']
   product_name = caption.split(': ')[1]


   product = session.query(Product).filter_by(product_name=product_name).first()

   user_id = call.from_user.id


   if product:
       # Create a new Basket record
       basket = Basket(product=product,user_id=user_id)
       session.add(basket)
       session.commit()
       session.close()


       await call.message.answer(f"You have successfully purchased {product_name}!")
   else:
       await call.message.answer("Product not found.")

@dp.message_handler(text='🛍Buyurtmalarim')
async def show_basket(message: types.Message):
   # Query the basket items for the user

   # user = session.query(User).filter_by(user_id=users_id).first()
   basket_items = session.query(Basket).all()


   if basket_items:
       basket_message = "Your products:\n"
       for basket_item in basket_items:
           product = basket_item.product

           basket_message += f"{product.product_name}: ${product.product_price}\n"

       await message.answer(basket_message)
   else:
       await message.answer("Your basket is empty.")


@dp.message_handler(commands=['clear'])
async def clear_basket(message: types.Message):
    # Clear the basket for the user
    session = Session()
    session.query(Basket).delete()
    session.commit()
    session.close()

    await message.answer("Your basket has been cleared.")