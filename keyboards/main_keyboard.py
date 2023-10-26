from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🍴Menyu"),
            KeyboardButton('📥Savat')
        ],
        [
            KeyboardButton("🛍Buyurtmalarim"),
            KeyboardButton("⚙️Sozlamalar")
        ],
        [
            KeyboardButton("🔖Statistika")
        ]
    ],resize_keyboard=True
)

start_keyboard2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🍕Pizza"),
            KeyboardButton("🍹Ichimliklar")
            ],
        [
            KeyboardButton("🔙Orqaga")
        ]
    ],resize_keyboard=True
)
