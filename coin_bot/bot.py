#!/usr/bin/env python3
from gc import callbacks
import telebot
import config
from telebot import types
import coin_flip
import time


bot = telebot.TeleBot(config.BOT_TOKEN)


def func1(toss):
    for i in range(exp):
        coin_toss = coin_flip.coin_toss(toss)
        resh = coin_toss.count(0)
        orel = coin_toss.count(1)
        if resh > orel:
            return (f"Победа решка {resh}:{orel}", False)
        if orel > resh:
            return (f"Победа орёл {orel}:{resh}", True)
        elif orel == resh:
            return (f"Ничья {resh}:{orel}", "Ничья")


def scoring_result(list_quantity_experiments):
    count_vicrory = {}
    count_vicrory["Орёл"] = list_quantity_experiments.count(True)
    count_vicrory["Решка"] = list_quantity_experiments.count(False)
    count_vicrory["Одинаково"] = list_quantity_experiments.count("Ничья")
    return f"""
Результаты:
Всего побед решек: {count_vicrory["Решка"]}
Всего побед орлов: {count_vicrory["Орёл"]}
Всего ничьих: {count_vicrory["Одинаково"]}
Попробовать заново /start
"""


def button():
    markup = types.InlineKeyboardMarkup(row_width=3)
    ten_exp = types.InlineKeyboardButton("10", callback_data="ten_exp")
    twenty_exp = types.InlineKeyboardButton("20", callback_data="twenty_exp")
    fifty_exp = types.InlineKeyboardButton("50", callback_data="fifty_exp")
    markup.add(ten_exp, twenty_exp, fifty_exp)
    return markup


@bot.message_handler(commands=["start", "restart"])
def cmd_start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton("Да", callback_data="yes")
    item2 = types.InlineKeyboardButton("Нет", callback_data="no")
    markup.add(item, item2)
    bot.send_message(message.chat.id, """Привет, я предлагаю тебе провести эксперимент с монеткой
ты этого хочешь?""", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global toss
    global exp
    if call.message:
        if call.data == "yes":
            markup = types.InlineKeyboardMarkup(row_width=3)
            item_ten = types.InlineKeyboardButton("10", callback_data="ten")
            item_twenty = types.InlineKeyboardButton(
                "20", callback_data="twenty")
            item_fifty = types.InlineKeyboardButton(
                "50", callback_data="fifty")
            markup.add(item_ten, item_twenty, item_fifty)
            bot.send_message(call.message.chat.id, """
Дорогой друг чтож приступим к эксперементу
Cколько раз ты хочешь подкинуть монетку""", reply_markup=markup)
        elif call.data == "ten":
            toss = 10
            bot.send_message(
                call.message.chat.id, """введи кол-во эксериментов""", reply_markup=button())
        elif call.data == "twenty":
            toss = 20
            bot.send_message(
                call.message.chat.id, """Выбери кол-во эксериментов""", reply_markup=button())
        elif call.data == "fifty":
            toss = 50
            bot.send_message(
                call.message.chat.id, """введи кол-во эксериментов""", reply_markup=button())
        elif call.data == "ten_exp":
            exp = 10
            bot.send_message(call.message.chat.id, f"""Подкидуем монетку {toss} раз
Проводим {exp} экспериментов""")
            my_list = []
            for i in range(1, exp + 1):
                a = func1(toss)
                time.sleep(1)
                bot.send_message(call.message.chat.id, f"""
Эксперимент - {i}
{a[0]} """)
                my_list.append(a[1])
            time.sleep(2)
            bot.send_message(call.message.chat.id,
                             f"""
Всего проведено {exp} эксперементов
{scoring_result(my_list)} """)

        elif call.data == "twenty_exp":
            exp = 20
            bot.send_message(call.message.chat.id, f"""Подкидуем монетку {toss} раз
Проводим {exp} экспериментов""")
            my_list = []
            for i in range(1, exp + 1):
                a = func1(toss)
                time.sleep(1)
                bot.send_message(call.message.chat.id, f"""
Эксперимент - {i}
{a[0]} """)
                my_list.append(a[1])
            time.sleep(2)
            bot.send_message(call.message.chat.id,
                             f"""
Всего проведено {exp} эксперементов
{scoring_result(my_list)} """)
        elif call.data == "fifty_exp":
            exp = 50
            bot.send_message(call.message.chat.id, f"""Подкидуем монетку {toss} раз
Проводим {exp} экспериментов""")
            my_list = []
            for i in range(1, exp + 1):
                a = func1(toss)
                time.sleep(1)
                bot.send_message(call.message.chat.id, f"""
Эксперимент - {i}                
{a[0]} """)
                my_list.append(a[1])
            time.sleep(2)
            bot.send_message(call.message.chat.id,
                             f"""
Всего проведено {exp} эксперементов
{scoring_result(my_list)} """)
        elif call.data == "no":
            bot.send_message(
                call.message.chat.id, """Ты сделай свой выбор, изменишь решение введи /start""")


if __name__ == "__main__":
    bot.infinity_polling()
