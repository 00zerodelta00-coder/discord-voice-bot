import os
import asyncio
import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Твой ID канала и токен уже зашиты сюда
CHANNEL_ID = 1503770910283389320  
TOKEN = "MTUzMjQyNzQ0ODg0MzM5NDIzMA.GOJgmw.vZOQmUWJrRMUjmC1GOVTSgJ-5_cRVj0YbtDsQo"

@client.event
async def on_ready():
    print(f"Робот {client.user} успешно включился!")
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        try:
            await channel.connect()
            print("УСПЕХ! Бот зашел в канал.")
        except Exception as e:
            print(f"Ошибка подключения: {e}")

client.run(TOKEN)
