
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

# Carrega o .env localmente.
# Na Vertra, também utiliza as variáveis de ambiente cadastradas.
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

TOKEN = os.getenv("DISCORD_BOT_TOKEN")


class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True

        super().__init__(
            command_prefix="!",
            intents=intents
        )
    async def setup_hook(self):
        await self.load_extension("cogs.moderation")

bot = MyBot()


@bot.event
async def on_ready():
    print(f"Amora conectada como {bot.user}")


if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("Token DISCORD_BOT_TOKEN não encontrado!")

    bot.run(TOKEN)
