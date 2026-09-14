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
# BOT ONLINE
# =========================

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")


# =========================
# NORMAL MESSAGE REPLIES
# =========================

@bot.event
async def on_message(message):

    # Ignore messages from bots
    if message.author.bot:
        return

    text = message.content.lower().strip()

    # Hi
    if text == "hi":
        await message.channel.send(
            f"Hi {message.author.mention} 👋"
        )

    # Hello
    elif text == "hello":
        await message.channel.send(
            f"Hello {message.author.mention}! 👋"
        )

    # Good morning
    elif text == "good morning":
        await message.channel.send(
            f"Good morning {message.author.mention}! ☀️"
        )

    # Good afternoon
    elif text == "good afternoon":
        await message.channel.send(
            f"Good afternoon {message.author.mention}! 🌤️"
        )

    # Good evening
    elif text == "good evening":
        await message.channel.send(
            f"Good evening {message.author.mention}! 🌆"
        )

    # Good night
    elif text == "good night":
        await message.channel.send(
            f"Good night {message.author.mention}! 🌙"
        )

    # Important: allows ! commands to work
    await bot.process_commands(message)


# =========================
# !HELLO COMMAND
# =========================

@bot.command()
async def hello(ctx):
    await ctx.send(
        f"Hello {ctx.author.mention}! 👋"
    )


# =========================
# !RULES COMMAND
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
# !HELP COMMAND
# =========================

# Function is called bot_help instead of help
# but Discord command remains !help

@bot.command(name="help")
async def bot_help(ctx):
    await ctx.send(
        "**Bot Commands 🤖**\n\n"
        "`!hello` - Say hello\n"
        "`!rules` - Show server rules\n"
        "`!help` - Show commands\n\n"
        "**Automatic Greetings 👋**\n"
        "`hi` - Get a greeting\n"
        "`hello` - Get a greeting\n"
        "`good morning` - Morning greeting\n"
        "`good afternoon` - Afternoon greeting\n"
        "`good evening` - Evening greeting\n"
        "`good night` - Night greeting"
    )


# =========================
# START BOT
# =========================

bot.run(os.environ["DISCORD_TOKEN"])
