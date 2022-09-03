from email import message
from re import M
import discord
from discord.ext import commands
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'),intents=intents ) 

@bot.event
async def on_ready(): #開啟
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1015537158133657671)
    await channel.send(f"@{member} 早安")
    print('join')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1015537158133657671)
    await channel.send(f"@{member} 滾")
    print(f"{member}leave")

@bot.command()
async def test(ctx,hi):
    await ctx.send(hi)

@bot.event
async def on_message(message):

    if message.content == '機器人':
        await message.channel.send('誰叫我？')



bot.run("MTAxNTUzNDcwOTQ4MjIwMTExOQ.GuNeI-.Tw6ui-wGmdqkuLl7UK1NdbOGkEWVu26XoFTre8")
