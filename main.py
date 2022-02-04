from aiogram import Bot, Dispatcher, executor, types
from api import api_request


TOKEN = "5223569017:AAGw4gFbYGKrI_t3AOlp0rJPzPZYLsh2iLs"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

# @dp.message_handler(commands=["start"])
# async def do_start(message: types.Message):
#     await message.answer("Multik botqa xosh kelibsiz!!!")


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    
    await message.answer("Multik rasm yasovchi botga xush kelibsiz!!!\nRasmingizni yuboring va kelgan rasmni yuklab oling👌🏻\n👨🏼‍💻Admin: @duysenbaevs")


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def get_image_from_user(message: types.Message):
    message_id = (await message.answer("Yuklanmoqda...🚀")).message_id
    photo_id = message.photo[-1].file_id
    photo_info = await bot.get_file(photo_id)
    file_path = photo_info["file_path"]
    photo_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"


    data = await api_request(photo_url)

    if data is not None:
        await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
        await message.answer_photo(photo=data)
    else:
        await message.answer("Iltimos boshqa sifatliroq rasm jo'nating!")

if __name__ == "__main__":
    executor.start_polling(dp)