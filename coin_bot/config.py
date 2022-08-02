#!/usr/bin/env python3

from enum import Enum

BOT_TOKEN = "5358182286:AAHj5r9YONEUkHe71O9IdGS31H_oGGVPCEU"
db_file = "db/database_bot_coin.vdb"


class States(Enum):
    S_START = "0"  # Начало нового диалога
    S_YES = "1"
    S_ENTER_QUANTITY_TOSS = "2"
    S_ENTER_QUANTITY_EXPERIMENT = "3"
