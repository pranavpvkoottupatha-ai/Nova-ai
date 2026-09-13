

import discord
from discord.ext import commands
import os

# =========================
# BOT SETTINGS
# =========================

intents = discord.Intents.default()
intents.message_content = True

# Disable Discord.py's built-in !help command
bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)


# =========================
# BOT STARTUP
# =========================

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")
    print("Nova AI is ready! 🤖")


# =========================
# AUTOMATIC MESSAGE REPLIES
# =========================

@bot.event
async def on_message(message):

    if message.author.bot:
        return

    text = message.content.lower().strip()

    if text == "hi":
        await message.channel.send(
            f"Hi {message.author.mention} 👋"
        )

    elif text == "hello":
        await message.channel.send(
            f"Hello {message.author.mention}! 👋"
        )

    elif text == "good morning":
        await message.channel.send(
            f"Good morning {message.author.mention}! ☀️"
        )

    elif text == "good afternoon":
        await message.channel.send(
            f"Good afternoon {message.author.mention}! 🌤️"
        )

    elif text == "good evening":
        await message.channel.send(
            f"Good evening {message.author.mention}! 🌆"
        )

    elif text == "good night":
        await message.channel.send(
            f"Good night {message.author.mention}! 🌙"
        )

    # Allows ! commands to work
    await bot.process_commands(message)


# =========================
# !HELLO
# =========================

@bot.command()
async def hello(ctx):
    await ctx.send(
        f"Hello {ctx.author.mention}! 👋"
    )


# =========================
# !RULES
# =========================

@bot.command()
async def rules(ctx):
    await ctx.send(
        "**Server Rules 📜**\n"
        "1. Respect everyone.\n"
        "2. No spam.\n"
        "3. No unnecessary arguments.\n"
        "4. Follow Discord rules."
    )


# =========================
# !HELP
# =========================

@bot.command()
async def help(ctx):
    await ctx.send(
        "**Nova AI Commands 🤖**\n\n"
        "`!hello` - Say hello\n"
        "`!rules` - Show server rules\n"
        "`!help` - Show commands\n\n"
        "**Automatic Replies 💬**\n"
        "`hi` - Greeting\n"
        "`hello` - Greeting\n"
        "`good morning` - Morning greeting\n"
        "`good afternoon` - Afternoon greeting\n"
        "`good evening` - Evening greeting\n"
        "`good night` - Night greeting"
    )


# =========================
# START BOT
# =========================

bot.run(os.environ["DISCORD_TOKEN"])
