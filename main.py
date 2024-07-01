import discord
from discord.ext import commands
import asyncio
import threading
import logging
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Disable discord.py's default INFO level logging
logging.basicConfig(level=logging.WARNING)

# ANSI color codes for styling
SKY_BLUE = '\033[1;36m'  # Bold Sky Blue
YELLOW = '\033[1;33m'    # Bold Yellow
RESET = '\033[0m'        # Reset to default

# Filter out specific discord.py INFO messages
logging.getLogger('discord.client').setLevel(logging.ERROR)
logging.getLogger('discord.gateway').setLevel(logging.ERROR)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Global variable to store the recipient user ID
recipient_id = None

def terminal_chat():
    global recipient_id
    username = input(f"{YELLOW}Enter your username: {RESET}")
    chat_option = input(f"{YELLOW}Type '1' to confirm you are not a bot: {RESET}").strip().lower()

    if chat_option == '1':
        recipient_id = input(f"{YELLOW}Enter recipient user ID: {RESET}")
        while True:
            message = input(f"{SKY_BLUE}{username}: {RESET}").strip()  # Strip whitespace from input
            if recipient_id and message:
                asyncio.run_coroutine_threadsafe(send_message(recipient_id, message), bot.loop)

async def send_message(user_id, message):
    user = await bot.fetch_user(user_id)
    if user:
        try:
            await user.send(message)
        except discord.HTTPException as e:
            print(f"{YELLOW}Failed to send message: {e.text}{RESET}")
        except discord.Forbidden:
            print(f"{YELLOW}Failed to send message: Bot does not have permission to send DMs to this user.{RESET}")
        except Exception as e:
            print(f"{YELLOW}Failed to send message: {type(e).__name__} - {e}{RESET}")
    else:
        print(f"{YELLOW}Failed to find the user.{RESET}")

@bot.event
async def on_ready():
    print(f'''
{SKY_BLUE}
    ┌──────────────────────────────┐
    │                              │
    │         DM Bot Online        │
    │                              │
    └──────────────────────────────┘
{RESET}
    Made by yoosid41210 😎
    ''')
    threading.Thread(target=terminal_chat).start()

@bot.event
async def on_message(message):
    global recipient_id

    if message.author == bot.user:
        return

    if str(message.author.id) == recipient_id:
        print(f"\n{SKY_BLUE}{message.author}: {RESET}{message.content}")  # Print recipient's message in a new line
    else:
        print(f"{SKY_BLUE}{message.author}: {RESET}{message.content}")

# Read the bot token from the environment variable
bot_token = os.getenv('DISCORD_BOT_TOKEN')
if bot_token:
    bot.run(bot_token)
else:
    print(f"{YELLOW}Error: DISCORD_BOT_TOKEN environment variable not set.{RESET}")
