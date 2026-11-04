import discord
from discord.ext import commands
import discord.app_commands
import os
from dotenv import load_dotenv
from pathlib import Path


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="kick", description="Expulsa um usuário do servidor.")
    @discord.app_commands.describe(user="O usuário a ser expulso.", reason="Motivo da expulsão.")
    async def kick(self, interaction: discord.Interaction, user: discord.Member, reason: str = None):
        if not interaction.user.guild_permissions.kick_members:
            await interaction.response.send_message("Você não tem permissão para expulsar membros.", ephemeral=True)
            return

        try:
            await user.kick(reason=reason)
            await interaction.response.send_message(f"{user.mention} foi expulso do servidor.", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"Não foi possível expulsar {user.mention}. Erro: {e}", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Moderation(bot))