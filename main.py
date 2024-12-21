from telethon import TelegramClient
from telethon.tl.functions.messages import ReportRequest
from colorama import Fore
import re
import asyncio
import os
import random

texts = [
    "Призывает устроить терракт",
    "Распространяет детскую порнографию",
    "Призывает убивать животных и скидывает видео как это делает",
    "Распространяет нацизм",
    "Распространяет шок-контент",
    "Скидывает видео где издивается над своим животным",
    "Скидывает видео где расстреливают людей...",
    "Призывает употреблять наркотики и рекламирует канал с продажей наркотиков",
    "Отправляет канал с продажей тяжелых наркотиков",
    "Отправлял канал где продают детскую порнографию"
]

async def main():

    url = input(Fore.LIGHTCYAN_EX + "Введи ссылку на сообщение: " + Fore.RESET)
    pattern = r'https:\/\/t\.me\/([^\/]+)\/(\d+)'
    match = re.match(pattern, url)
    if match:
        group_username = match.group(1)  # тег чата
        message_id = int(match.group(2))  # ид чата шоб не запутаца
    else:
        print(Fore.RED + "Ошибка: Не верная ссылка." + Fore.RESET)

    try:
        await session_1(group_username, message_id)
        await session_2(group_username, message_id)
        await session_3(group_username, message_id)
    except Exception as e:
        print(Fore.RED + f"Ошибка: {e}" + Fore.RESET)

    return group_username, message_id

async def session_1(group_username, message_id):
    count = 1

    client = TelegramClient('149495015_telethon', 123, 123, system_version="4.16.30-vxCUSTOM")
    await client.start()
    group = await client.get_entity(group_username)
    text = random.choice(texts)
    res = await client(ReportRequest(
        peer=group,
        id=[message_id],
        option='',
        message=text
    ))
    print(res)
    print(f'Жалоба №{count} отправленна!')

async def session_2(group_username, message_id):
    count = 2

    client = TelegramClient('149500508_telethon', 123, 123, system_version="4.16.30-vxCUSTOM")
    await client.start()
    group = await client.get_entity(group_username)
    text = random.choice(texts)
    res = await client(ReportRequest(
        peer=group,
        id=[message_id],
        option='',
        message=text
    ))
    print(res)
    print(f'Жалоба №{count} отправленна!')

async def session_3(group_username, message_id):
    count = 3

    client = TelegramClient('yota_maks', 123, 123, system_version="4.16.30-vxCUSTOM")
    await client.start()
    group = await client.get_entity(group_username)
    text = random.choice(texts)
    res = await client(ReportRequest(
        peer=group,
        id=[message_id],
        option='',
        message=text
    ))
    print(res)
    print(f'Жалоба №{count} отправленна!')

asyncio.run(main())
