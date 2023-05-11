import discord
from textblob_de import TextBlobDE as TextBlob
import json
import os
intents = discord.Intents.default()
intents.message_content = True
stinker = {}
bot_token = os.environ.get('BOT_KEY')
class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!stinker'):
            stinker_antwort = "Dein Stinker Score ist " + str(stinker[message.author.id])
            if message.author.id not in stinker:
                return
            await message.reply(stinker_antwort, mention_author=True)
            return
        data = message.content
        blob = TextBlob(data)
        ai_data = blob.sentiment
        print(ai_data)

client = MyClient(intents=intents)
client.run('')
