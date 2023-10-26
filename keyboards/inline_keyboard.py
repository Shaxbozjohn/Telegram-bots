from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


inline_keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Pepperoni", callback_data="paperonpizza"),
            InlineKeyboardButton("Belissimo", callback_data="belissimopizza")

        ],
        [
            InlineKeyboardButton("Margarita", callback_data="margaritapizza"),
            InlineKeyboardButton("Alfredo", callback_data="alfredo")
        ]
    ]
)

inline_keyboard5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="25sm ",callback_data="ma38000"),
            InlineKeyboardButton(text="30sm ",callback_data="ma52000")
           ],
        [
            InlineKeyboardButton(text="35sm ", callback_data="ma62000")
        ]
]
)


inline_keyboard4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="-", callback_data="minus"),
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="+", callback_data="+")

        ],
        [
            InlineKeyboardButton(text="📥Savatga qo'shish",callback_data='savat')
        ]

    ],row_width=70
)