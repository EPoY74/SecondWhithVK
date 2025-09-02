"""
Telegram Bot: Daily Percentage Calculator

Bot URL: http://t.me/Percents_Per_Day_bot

Description:
This bot calculates the monetary value of an annual interest rate 
broken down into daily, weekly, and 30-day periods.

User inputs:
1. The principal amount (base sum of money)
2. The annual interest rate (in percent)

The bot then computes and displays:
- Interest per day
- Interest per week
- Interest per 30-day month

Author: Eugenii Petrov (epoy74@gmail.com)
"""

# import os
import time

import telebot

import lib.project_log as proj_log
import lib.secrets as proj_sec

logger = proj_log.logging.getLogger(__name__)

extract_bot_token: str | None = proj_sec.get_bot_api_from_dotenv()

if extract_bot_token:
    BOT_TOKEN: str = str(extract_bot_token)
else:
    logger.critical("Can't resive telegram bot token" )
    raise # TODO: Implement a custom exception handler

bot = telebot.TeleBot(BOT_TOKEN)

bot.delete_webhook()

Deposit_Amount = 0.0
Deposit_Percent = 0.0
Deposit_Profit_Per_Day = 0.0


@bot.message_handler(content_types=["text"])
def start(message):
    User_Name = bot.get_me()
    logger.debug(User_Name)
    if message.text == "/start" or message.text == "/help":
        bot.send_message(
            message.from_user.id,
            ("Рассчитываю процент от суммы."
            "Для расчета требуется ввести сумму и процент (в годовых)."
            " Рассчет ориентировочный \nВведите сумму:"
            ),
        )
    # bot.send_message(message.from_user.id, 'Введите сумму: ');
    else:
        bot.send_message(
            message.from_user.id,
            "Рассчитаю тебе процент от суммы. \nВведите сумму:",
        )
    # bot.send_message(message.from_user.id, 'Введите сумму: ');
    bot.register_next_step_handler(
        message, get_Deposit_Amount
    )  # следующий шаг – получаем сумму


def get_Deposit_Amount(message):  # Получаем сумму для расчета
    global Deposit_Amount
    Deposit_Amount_temp = message.text
    logger.debug(Deposit_Amount_temp)
    if Deposit_Amount_temp.isdigit():
        Deposit_Amount = float(Deposit_Amount_temp)
        bot.send_message(
            message.from_user.id, "Введите годовую процентную ставку"
        )

    elif Deposit_Amount_temp != "/start" or Deposit_Amount_temp != "/help":
        bot.send_message(
            message.from_user.id,
            "Введите данные числом. \nРассчет ориентировочный.\n",
        )
        bot.register_next_step_handler(message, start)
    else:
        bot.send_message(
            message.from_user.id,
            "Введите данные числом. \nРассчет ориентировочный.\n",
        )
        bot.register_next_step_handler(message, start)
    bot.register_next_step_handler(message, get_Deposit_Percent)


def get_Deposit_Percent(message):  # Получаем процентную ставку для расчета
    global Deposit_Percent
    global Deposit_Profit_Per_Day
    # bot.register_next_step_handler(message, get_Deposit_Percent);
    Deposit_Percent_temp = message.text
    logger.debug(Deposit_Percent_temp)
    if Deposit_Percent_temp.isdigit() and Deposit_Amount:
        Deposit_Percent = float(Deposit_Percent_temp)
        logger.debug(Deposit_Percent)
        bot.send_message(
            message.from_user.id,
            "От суммы "
            + str(Deposit_Amount)
            + " руб.,  при заданной процентной ставке "
            + str(Deposit_Percent)
            + " доход(штраф) составляет: \n ",
        )
        Deposit_Profit_Per_Day = Deposit_Amount * (
            (Deposit_Percent / 100) / 365
        )
        Deposit_Profit_Per_7Day = (
            Deposit_Amount * ((Deposit_Percent / 100) / 365) * 7
        )
        Deposit_Profit_Per_30Day = (
            Deposit_Amount * ((Deposit_Percent / 100) / 365) * 30
        )
        logger.debug(Deposit_Profit_Per_Day)
        bot.send_message(
            message.from_user.id,
            "За 1 день: "
            + str(round(Deposit_Profit_Per_Day, 2))
            + " руб. в  день\n"
            + "За 7 дней:  "
            + str(round(Deposit_Profit_Per_7Day, 2))
            + " руб. за 7 дней\n"
            + "За 30 дней: "
            + str(round(Deposit_Profit_Per_30Day, 2))
            +  (" руб. за 30 дней\n"
            'Для продолжения напиши /start' 
            ' или введи любой символ и нажми "Enter"'
            ),
        )
    # bot.send_message(message.from_user.id, 'Введите сумму: ')
    bot.register_next_step_handler(message, start)


if __name__ == "__main__":
    while True:
        try:
            logger.info("--- start ---")
            bot.polling(none_stop=True)
        except Exception as e:
            logger.warning("--- reset ---")
            time.sleep(10)
            logger.error(e)
