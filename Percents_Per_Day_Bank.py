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
Deposit_Profit_Pet_Day = 0.0;

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start' or message.text == '/help':
        bot.send_message(message.from_user.id, "Рассчитываю процент от суммы. Для расчета требуется ввести сумму и процент (в годовых)."
                                               " Рассчет ориентировочный");
    else:
        bot.send_message(message.from_user.id, "Рассчитаю тебе процент от суммы.");
        bot.send_message(message.from_user.id, 'Введите сумму: ');
        bot.register_next_step_handler(message, get_Deposit_Amount); #следующий шаг – функция get_name;

def get_Deposit_Amount(message): # Получаем сумму для расчета
    Deposit_Amount_temp = message.text;
    print(Deposit_Amount_temp)
    if Deposit_Amount_temp.isdigit():
        Deposit_Amount = float(Deposit_Amount_temp)
        bot.send_message(message.from_user.id, 'Введите годовую процентную ставку');
       
    elif Deposit_Amount_temp != '/start' or Deposit_Amount_temp != '/help':
        bot.send_message(message.from_user.id,
                         "Рассчитываю процент от суммы. Для расчета требуется ввести сумму и процент (в годовых)."
                         " \nРассчет ориентировочный.\nВведите любой символ  для продолжения:  ");
    
        bot.register_next_step_handler(message, start);
    else:
        bot.register_next_step_handler(message, start);

    bot.register_next_step_handler(message, get_Deposit_Percent);



def get_Deposit_Percent(message): # Получаем процентную ставку для расчета
    # bot.register_next_step_handler(message, get_Deposit_Percent);
    Deposit_Percent_temp = message.text;
    print(Deposit_Percent_temp)
    if Deposit_Percent_temp.isdigit():
        Deposit_Percent = float(Deposit_Percent_temp)
        print(Deposit_Percent)
    bot.send_message(message.from_user.id, "---111---");
    bot.register_next_step_handler(message, Calculate_Result);

def Calculate_Result(message): # Расчитываем доход от суммы в день при заданной ставке
    Deposit_Profit_Per_Day = Deposit_Amount * ((Deposit_Percent / 100) / 365)
    print(Deposit_Profit_Per_Day)
    bot.send_message(message.from_user.id, "От суммы" + str(Deposit_Amount) + " руб. При заданной прооцентной ставке " + str(Deposit_Percent) +
                      " доход составляет " + str(round(Deposit_Profit_Per_Day,2)) + "руб./ день")
    #bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?')


if __name__ == '__main__':
    while True:
        try:
            print ("--- start ---")
            bot.polling(none_stop=True)
        except Exception as e:
            print("--- reset ---")
            time.sleep(3)
            print(e)


