from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📸 Зробити фото маркування")],
        [KeyboardButton(text="♻️ Обрати екомаркування")],
        [KeyboardButton(text="🌿 Дізнатися більше про екомаркування")],
    ],
    resize_keyboard=True,
)
