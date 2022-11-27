import discord
from discord.ext import commands


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def info(self, ctx):
        embed: discord.Embed = discord.Embed(
            title=f"Air France Bot Information", color=self.eColor
        )
        embed.add_field(name="Wrapper", value="``discord.py``", inline=True)
        embed.add_field(name="License", value="``GNU GPL v3.0``")
        embed.add_field(name="Made and maintained by", value="``Some Guy#2451``", inline=False)
        embed.set_footer(text="Created on 11.26.22")
        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Info(bot))
