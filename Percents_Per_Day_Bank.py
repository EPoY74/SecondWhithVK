"""
http://t.me/Percents_Per_Day_bot

Телеграм бот. Считает проценты на каждый день
Вводим сумму и проценты, которые требуется посчитать.

6272876979:AAG67KaMwaTPVsL0AN9nXDnwTpk1FLbP2rg

"""

"""
Этот бот, можно сказать, первый который что-то делает нужное.
Считает сумму штрафа в день при 20% годовых. Требуется ввести сумму задолжности.
Что бы не считать на калькуляторе.
"""
import telebot;
import time;

bot = telebot.TeleBot('6272876979:AAG67KaMwaTPVsL0AN9nXDnwTpk1FLbP2rg');

"""@bot.message_handler(content_types=['text'])

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
"""

Deposit_Amount = 0.0;
Deposit_Percent = 0.0;


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start' or message.text == '/help':
        bot.send_message(message.from_user.id, "Рассчитываю процент от суммы. Для расчета требуется ввести сумму и процент (в годовых)."
                                               " Рассчет ориентировочный");
        bot.register_next_step_handler(message, get_Deposit_Amount); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_Deposit_Amount(message): #получаем фамилию
    bot.send_message(message.from_user.id, 'Введите сумму: ');
    Deposit_Amount_temp = message.text;
    if Deposit_Amount_temp.isdigit():
        Deposit_Amount = float(Deposit_Amount_temp)
        bot.send_message(message.from_user.id, 'Введите годовую процентную ставку');
        bot.register_next_step_handler(message, get_Deposit_Percent);
    elif Deposit_Amount_temp != '/start' or Deposit_Amount_temp != '/help':
        bot.send_message(message.from_user.id,
                         "Рассчитываю процент от суммы. Для расчета требуется ввести сумму и процент (в годовых)."
                         " \nРассчет ориентировочный.\nВведите сумму: ");

    bot.register_next_step_handler(message, get_surname);

def get_Deposit_Percent(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id,'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?')


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)


