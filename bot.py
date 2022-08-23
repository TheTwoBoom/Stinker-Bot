import discord
from textblob_de import TextBlobDE as TextBlob
import json
intents = discord.Intents.default()
intents.message_content = True
stinker = {}
bot_token = ""
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
        result = TextBlob(data)
        ai_data = result.sentiment
        print(type(ai_data))
        if "subjectivity" == 0.0 in result.sentiment:
            if message.author.id not in stinker:
                user_start = {message.author.id:0}
                stinker.update(user_start)
            count = stinker[message.author.id] + 1
            user_stats = {message.author.id:count}
            stinker.update(user_stats)
            print(stinker)
        if "" in result.sentiment:
            if message.author.id not in stinker:
                user_start = {message.author.id:0}
                stinker.update(user_start)
            count = stinker[message.author.id] - 1
            user_stats = {message.author.id:count}
            stinker.update(user_stats)
            print(stinker)

client = MyClient(intents=intents)
client.run('')
