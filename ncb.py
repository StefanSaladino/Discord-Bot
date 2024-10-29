import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
import re

load_dotenv()

# Retrieve token from token.env file
with open('token.env', 'r') as file:
    TOKEN = file.read().strip()

# Retrieve guild name from guild.env file
with open('guild.env', 'r') as file:
    GUILD_NAME = file.read().strip()

with open('guild2.env', 'r') as file:
    GUILD_NAME_2 = file.read().strip()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    # Check both guilds
    guild = discord.utils.get(bot.guilds, name=GUILD_NAME)
    guild2 = discord.utils.get(bot.guilds, name=GUILD_NAME_2)

    if guild:
        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
    else:
        print(f'Bot is not connected to the guild: {GUILD_NAME}')

    if guild2:
        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild2.name}(id: {guild2.id})'
        )
    else:
        print(f'Bot is not connected to the guild: {GUILD_NAME_2}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Use regular expression to find the exact word "nice" in the message
    matches = re.findall(r"\bnice\b", message.content.lower())
    cockMatch = re.findall(r"\bcock\b", message.content.lower())

    if matches:
        user_tag = message.author.mention

        num_nice_occurrences = len(matches)
        response = f'Hey, {user_tag} ' + 'NICE COCK!\n' * num_nice_occurrences
        
        if len(response) > 3999:
            await message.channel.send(f"Listen {user_tag}, that's too much cock for me to handle. Who do you think I am? Kim Kardashian?")
        else:
            await message.channel.send(response)
    
    if cockMatch:
        embed = discord.Embed(
            title="Did someone say cock!?", 
            url="https://youtu.be/4dJO0n1Wqjg", 
            description="Nice cock!",
            color=discord.Color.blue()
    )
        # Set a thumbnail image, which will display the YouTube video thumbnail
        embed.set_thumbnail(url="https://img.youtube.com/vi/4dJO0n1Wqjg/hqdefault.jpg")
        # Send the embedded message
        await message.channel.send(embed=embed)

    await bot.process_commands(message)
    

bot.run(TOKEN)

