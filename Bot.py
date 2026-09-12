import discord
from discord.ext import commands
import os

# Bot permissions
intents = discord.Intents.default()
intents.message_content = True

# Create bot
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)


# When bot starts
@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")


# Normal message replies
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    text = message.content.lower().strip()

    if text == "hi":
        await message.channel.send(f"Hi {message.author.mention} 👋")

    elif text == "hello":
        await message.channel.send(f"Hello {message.author.mention}! 👋")

    elif text == "good morning":
        await message.channel.send(f"Good morning {message.author.mention}! ☀️")

    elif text == "good afternoon":
        await message.channel.send(f"Good afternoon {message.author.mention}! 🌤️")

    elif text == "good evening":
        await message.channel.send(f"Good evening {message.author.mention}! 🌆")

    elif text == "good night":
        await message.channel.send(f"Good night {message.author.mention}! 🌙")

    # Required for ! commands
    await bot.process_commands(message)


# !hello command
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}! 👋")


# !rules command
@bot.command()
async def rules(ctx):
    await ctx.send(
        "**Server Rules 📜**\n"
        "1. Respect everyone.\n"
        "2. No spam.\n"
        "3. No unnecessary arguments.\n"
        "4. Follow Discord rules."
    )


# !help command
@bot.command()
async def help(ctx):
    await ctx.send(
        "**Bot Commands 🤖**\n"
        "`!hello` - Say hello\n"
        "`!rules` - Show server rules\n"
        "`!help` - Show commands\n"
        "`hi` - Get a greeting\n"
        "`hello` - Get a greeting"
    )


# Start bot using GitHub Secret
bot.run(os.environ["DISCORD_TOKEN"])
