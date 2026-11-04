
import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Comando para testar se o Cog foi carregado
    @commands.command(name="testecog")
    async def testecog(self, ctx):
        await ctx.reply("✅ Cog de moderação carregado com sucesso!")

    # Comando para limpar mensagens
    @commands.command(name="limpar", aliases=["clear"])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(
        manage_messages=True,
        read_message_history=True
    )
    async def limpar(self, ctx, quantidade: int):
        if quantidade < 1 or quantidade > 100:
            await ctx.reply(
                "Informe uma quantidade entre 1 e 100."
            )
            return

        apagadas = await ctx.channel.purge(
            limit=quantidade + 1
        )

        total = max(0, len(apagadas) - 1)

        await ctx.send(
            f"🧹 {total} mensagens foram apagadas!",
            delete_after=5
        )


# Função obrigatória para carregar a extensão
async def setup(bot):
    await bot.add_cog(Moderation(bot))
