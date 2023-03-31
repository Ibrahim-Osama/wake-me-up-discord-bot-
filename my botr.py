import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.command()
async def move(ctx, channel: discord.VoiceChannel):
    # Get the current voice channel of the member who sent the command
    voice_channel = ctx.author.voice.channel

    # Move the member to the specified channel
    await ctx.author.move_to(channel)

    # Wait for 10 seconds before moving the member back
    await asyncio.sleep(10)

    # Move the member back to the original channel
    await ctx.author.move_to(voice_channel)

    # Repeat the above steps three more times
    for i in range(3):
        # Wait for 10 seconds before moving the member to the next channel
        await asyncio.sleep(10)

        # Alternate between the original channel and the specified channel
        if i % 2 == 0:
            await ctx.author.move_to(channel)
        else:
            await ctx.author.move_to(voice_channel)

    # Move the member back to the original channel
    await ctx.author.move_to(voice_channel)

bot.run('MTA5MTMwNTYyNjUyMjYyODEyNw.GsazXB.M9wBAQ4kdHfQjTpYXyYkthrk9vN66uPPAH-xAA')
