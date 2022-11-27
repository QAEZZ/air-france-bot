import random
import discord
from discord.ext import commands


def get_code():
    alpha_list = [
        "alpha",
        "bravo",
        "charlie",
        "delta",
        "echo",
        "foxtrot",
        "golf",
        "hotel",
        "india",
        "juliet",
        "kilo",
        "lima",
        "mike",
        "november",
        "oscar",
        "papa",
        "quebec",
        "romeo",
        "sierra",
        "tango",
        "uniform",
        "victor",
        "whiskey",
        "xray",
        "yankee",
        "zulu"
    ]
    
    return random.choice(alpha_list)


class ATIS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def atis(self, ctx, airport: str = "MISSING"):
        self.airport = airport
        if self.airport == "MISSING":
            await ctx.reply("``Please define an airport via ICAO code!``")
        else:
            embed: discord.Embed = discord.Embed(
                title=f"Information \"{get_code()}\" for {self.airport.upper()}", color=self.eColor
            )
            embed.set_footer(text="Soon™")
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(ATIS(bot))
