"""
Этот бот, можно сказать, первый который что-то делает нужное.
Считает сумму штрафа в день при 20% годовых. Требуется ввести сумму задолжности.
Что бы не считать на калькуляторе.
"""
import telebot;

bot = telebot.TeleBot('5416611054:AAFkdAkCTK5Kt8cWYJOb87w-QfDqzWxHKcE');

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    if message.text == "/start" or message.text ==  "/help":
        bot.send_message(message.from_user.id, "Считаю сумму штрафа в день при 20% годовых. Требуется ввести сумму задолжности.")

    pers1 = message.text
    if pers1.isdigit():
        pers2 = float(pers1)
        bot.send_message(message.from_user.id,'Штраф за просрочку платежа составляет ' + str(round(pers2 * (0.2 / 365),2)) + ' руб/день')
    elif message.text != "/start":
        bot.send_message(message.from_user.id, "Считаю сумму штрафа в день при 20% годовых. \nВведи число в рублях")

#    if message.text == "Привет":
#       bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#    elif message.text == "/help":
#        bot.send_message(message.from_user.id, "Напиши привет")
#    else:
#        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

#bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)