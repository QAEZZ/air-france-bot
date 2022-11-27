import discord
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def help(self, ctx, switch: str = None):
        try:

            embed: discord.Embed = discord.Embed(
                description="""```
Air France help
    help    :   Shows this
    charts  :   Sends a link of the PTFS map charts
    latency :   Replies with the latency of the client```""",
                color=self.eColor
            )

            await ctx.reply(embed=embed)

        except Exception as e:
            await ctx.reply(e)


async def setup(bot):
    await bot.add_cog(Help(bot))
