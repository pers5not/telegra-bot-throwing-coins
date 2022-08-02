#!/usr/bin/env python3
from itertools import count
import random
import bot



coin_value_dict = {
    0: "решка",
    1: "орёл"
}


def coin_toss(num_quantity):
    coin_values = []
    for throw in range(num_quantity):
        coin_val = random.randint(0, 1)
        coin_values.append(coin_val)
    return coin_values


# def coin_values_count(coin_values):
#     quant_tails = coin_values.count(0)
#     quant_eagle = coin_values.count(1)
#     if quant_tails > quant_eagle:
#         return False
#     elif quant_eagle > quant_tails:
#         return True
#     else:
#         return "одинаково"


# def quantity_experiments(len_experiments):
#     list_result = []
#     for i in range(len_experiments):
#         coin_toss_q = coin_toss(num_quantity)
#         print(
#             f"{coin_toss_q} Решка - {coin_toss_q.count(0)} Орёл - {coin_toss_q.count(1)}")
#         if coin_values_count(coin_toss_q) == True:
#             list_result.append(True)
#         elif coin_values_count(coin_toss_q) == False:
#             list_result.append(False)
#         elif coin_values_count(coin_toss_q) == "одинаково":
#             list_result.append("одинаково")
#     return list_result


# list_quantity_experiments = quantity_experiments(len_experiments)


# def scoring_result(list_quantity_experiments):
#     count_vicrory = {}
#     count_vicrory["Орёл"] = list_quantity_experiments.count(True)
#     count_vicrory["Решка"] = list_quantity_experiments.count(False)
#     count_vicrory["Одинаково"] = list_quantity_experiments.count("одинаково")
#     return count_vicrory


