from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, Message, InputFile, Update
import sqlite3
from aiogram import types
API_TOKEN = '6838775063:AAEEWy4xRxh918W-2vfeG9m9PfsIMaBfS48'  # replace with your actual token

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# Add these imports at the top of your code


# Add this function to create a table if it doesn't exist
def create_table():
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Call create_table() at the beginning of your script
create_table()

# Replace the global users_udata list with SQLite queries
async def is_user_in_db(user_id: int) -> bool:
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user is not None

async def add_user_to_db(user_id: int, username: str):
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()
    conn.close()

async def get_user_data(user_id: int) -> str:
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM users WHERE id = ?', (user_id,))
    username = cursor.fetchone()[0]
    conn.close()
    return username

async def send_pdf(message: Message, pdf_path: str):
    with open(pdf_path, 'rb') as pdf_file:
        await message.answer_document(document=InputFile(pdf_file))




mod = ReplyKeyboardMarkup(resize_keyboard=True)
mod1 = KeyboardButton(text='/Réseaux')
mod2 = KeyboardButton(text='/Développement_d’application_Web')
mod3 = KeyboardButton(text='/Base_de_données')
mod4 = KeyboardButton(text='/Système_dexploitation_1')
mod5 = KeyboardButton(text='/Programmation_orientée_objets')
mod6 = KeyboardButton(text='/Théorie_de_langage')
mod7 = KeyboardButton(text='/Anglais_3')

mod.add(mod1).add(mod2).add(mod3).add(mod4).add(mod5).add(mod6).add(mod7)

res = ReplyKeyboardMarkup(resize_keyboard=True)
res1 = KeyboardButton(text='/COURS')
res2 = KeyboardButton(text='/TD')
res3 = KeyboardButton(text='/TP')
res4 = KeyboardButton(text='/BACK_MENU')
res.add(res1,res2).add(res3, res4)

webd = ReplyKeyboardMarkup(resize_keyboard=True)
webd1 = KeyboardButton(text='/COURS')
webd2 = KeyboardButton(text='/TD')
webd3 = KeyboardButton(text='/TP')
webd4 = KeyboardButton(text='/BACK_MENU')
webd.add(webd1,webd2).add(webd3, webd4)

basd = ReplyKeyboardMarkup(resize_keyboard=True)
basd1 = KeyboardButton(text='/COURS')
basd2 = KeyboardButton(text='/TD')
basd3 = KeyboardButton(text='/TP')
basd4 = KeyboardButton(text='/BACK_MENU')
basd.add(basd1,basd2).add(basd3, basd4)

sys = ReplyKeyboardMarkup(resize_keyboard=True)
sys1 = KeyboardButton(text='/COURS')
sys2 = KeyboardButton(text='/TD')
sys3 = KeyboardButton(text='/TP')
sys4 = KeyboardButton(text='/BACK_MENU')
sys.add(sys1,sys2).add(sys3, sys4)

pro = ReplyKeyboardMarkup(resize_keyboard=True)
pro1 = KeyboardButton(text='/COURS')
pro2 = KeyboardButton(text='/TD')
pro3 = KeyboardButton(text='/TP')
pro4 = KeyboardButton(text='/BACK_MENU')
pro.add(pro1,pro2).add(pro3, pro4)

th = ReplyKeyboardMarkup(resize_keyboard=True)
th1 = KeyboardButton(text='/COURS')
th2 = KeyboardButton(text='/TD')
th3 = KeyboardButton(text='/TP')
th4 = KeyboardButton(text='/BACK_MENU')
th.add(th1,th2).add(th3, th4)

an = ReplyKeyboardMarkup(resize_keyboard=True)
an1 = KeyboardButton(text='/COURS')
an2 = KeyboardButton(text='/TD')
an3 = KeyboardButton(text='/TP')
an4 = KeyboardButton(text='/BACK_MENU')
an.add(an1,an2).add(an3, an4)


# Define the start command handler
# Modify your start command handler to use SQLite
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    is_user_exist = await is_user_in_db(user_id)

    if is_user_exist:
        await message.answer(f"Bonjour, your id is {user_id}", reply_markup=mod)
    else:
        await add_user_to_db(user_id, message.from_user.username)
        await message.answer("Hello!", reply_markup=mod)




@dp.message_handler(commands=['Réseaux'])
async def reseaux(message: types.Message):
    await message.answer("Réseaux", reply_markup=res)
    await message.delete()

@dp.message_handler(commands=['Développement_d’application_Web'])
async def web(message: types.Message):
    await message.answer("Développement d’application Web", reply_markup=webd)
    await message.delete()

@dp.message_handler(commands=['Base_de_données'])
async def basedd(message: types.Message):
    await message.answer("Base_de_données", reply_markup=basd)
    await message.delete()

@dp.message_handler(commands=['Système_dexploitation_1'])
async def system(message: types.Message):
    await message.answer("Système dexploitation 1", reply_markup=sys)
    await message.delete()

@dp.message_handler(commands=['Programmation_orientée_objets'])
async def programmation(message: types.Message):
    await message.answer("Programmation orientée objets", reply_markup=pro)
    await message.delete()

@dp.message_handler(commands=['Théorie_de_langage'])
async def theorie(message: types.Message):
    await message.answer("Théorie de langage", reply_markup=th)
    await message.delete()

@dp.message_handler(commands=['Anglais_3'])
async def anglais(message: types.Message):
    await message.answer("Anglais 3", reply_markup=an)
    await message.delete()


@dp.message_handler(commands=['BACK_MENU'])
async def back_menu(message: types.Message):
  await message.answer("menu",reply_markup=mod)


@dp.message_handler(commands=['COURS'])
async def TDSI01(message : Message):
    pdf_path = 'moudle/td1_ao.pdf'

    with open(pdf_path, 'rb') as pdf_file:
        await message.answer_document(document=InputFile(pdf_file))
async def get_all_user_ids() -> list:
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users')
    user_ids = [row[0] for row in cursor.fetchall()]
    conn.close()
    return user_ids

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def echo(message: types.Message):
    sender_id = message.from_user.id
    if sender_id == 6808061138:
        all_user_ids = await get_all_user_ids()
        for user_id in all_user_ids:
            await message.copy_to(user_id)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
