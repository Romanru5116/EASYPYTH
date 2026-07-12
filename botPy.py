# Инициализация (лучше вынести за пределы функции)
import requests
from bs4 import BeautifulSoup
import time
import telebot
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.session.aiohttp import AiohttpSession
# Импортируем прокси-коннектор
from aiohttp_proxy import ProxyConnector

# Пример адреса прокси: socks5://user:password@host:port или http://host:port
PROXY_URL = 'socks5://user:password@127.0.0.1:1080'

# --- КОНФИГУРАЦИЯ ---
BOT_TOKEN = '8784460831:AAEgLnjKw7Smrrk2fgZT4aiweV3i6UTO0WE'
CHAT_ID = '5968252107'
session = AiohttpSession(proxy=PROXY_URL)
bot = Bot(token=BOT_TOKEN, session=session)
dp = Dispatcher()
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я работаю через прокси.")
# message='бот_живой'
# bot.send_message(CHAT_ID, message)