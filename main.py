import os
import telebot
from openai import OpenAI

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@bot.message_handler(func=lambda message: True)
def reply(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo"
        messages=[{"role": "user", "content": message.text}]
    )
    bot.reply_to(message, response.choices[0].message.content)

bot.infinity_polling()
