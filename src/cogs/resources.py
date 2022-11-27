import discord

from discord.ext import commands


class Resources(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def charts(self, ctx):
        embed: discord.Embed = discord.Embed(
            title="Treelon/ptfs-charts", url="https://github.com/Treelon/ptfs-charts", color=self.eColor
        )
        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Resources(bot))
