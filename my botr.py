import discord
import random
from discord.ext import commands, tasks

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    change_channels.start()

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

@bot.command()
async def move(ctx):
    members = ctx.author.voice.channel.members
    for member in members:
        channel = random.choice(ctx.guild.voice_channels)
        await member.move_to(channel)

@bot.command()
async def back(ctx):
    members = ctx.author.voice.channel.members
    for member in members:
        await member.move_to(ctx.author.voice.channel)

@tasks.loop(count=4)
async def change_channels():
    guild = bot.get_guild(865951724249939969)
    channels = guild.voice_channels
    for channel in channels:
        members = channel.members
        if len(members) > 0:
            new_channel = random.choice(channels)
            while new_channel == channel:
                new_channel = random.choice(channels)
            for member in members:
                await member.move_to(new_channel)
    await discord.utils.sleep_until(change_channels.next_iteration)
    members = guild.voice_channels[0].members
    for member in members:
        await member.move_to(guild.voice_channels[0])
        
@bot.command()
async def helpme(ctx):
    embed = discord.Embed(title="Bot Commands", description="Here are the bot commands you can use:", color=0x00ff00)
    embed.add_field(name="!ping", value="Returns a 'pong!' message to check if the bot is working", inline=False)
    embed.add_field(name="!move", value="Moves all members in your voice channel to a random voice channel in the server", inline=False)
    embed.add_field(name="!back", value="Brings all members in your voice channel back to the original voice channel", inline=False)
    embed.add_field(name="!helpme", value="Displays this help message", inline=False)
    await ctx.send(embed=embed)

bot.run('MTA5MTMwNTYyNjUyMjYyODEyNw.GSTL6n.xhWdTAZuYy2fHyi8-SDmkaIDr5fn8-1AS7eNQ0')
