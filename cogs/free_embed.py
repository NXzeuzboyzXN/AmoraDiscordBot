import discord
from discord import app_commands
from discord.ext import commands


class FreeEmbed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="embed", description="Cria uma mensagem embed personalizada.")
    @app_commands.describe(
        title="O título do embed",
        description="A descrição do embed"
    )
    async def embed(self, interaction: discord.Interaction, title: str, color: discord.Color, *, description: str):

        embed = discord.Embed(title=title, description=description, color=color)
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
        
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(FreeEmbed(bot))
