from dotenv import load_dotenv
import os
import discord

heyguysList = ["Hey Guys", "hey guys"]

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.channel.name == "hey-guys":
            if message.content in heyguysList:
                await message.add_reaction('✅')
            else:
                await message.add_reaction('❌')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
