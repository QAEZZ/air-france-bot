import discord
from discord.ext import commands


"""
Air France help
    help                        :   Shows this
    info                        :   Shows information about the bot
    charts                      :   Sends a link of the PTFS map charts
    latency                     :   Replies with the latency of the client
    schedule                    :   Schedule a flight
    atis <ICAO Code: String>    :   Sends ATIS information for the specified airport
"""


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def help(self, ctx, switch: str = None):
        try:

            embed: discord.Embed = discord.Embed(
                title="Air France Bot Information", description="```<required>\n[optional]\n\nTypes of parameters\nstr - all characters\ninteger - numbers only\nbool - true/false```", color=self.eColor)
            
            embed.add_field(name="help", value="```Shows this```", inline=True)
            embed.add_field(name="info", value="```Shows bot info```", inline=True)
            embed.add_field(name="charts", value="```Sends a link for the PTFS charts```", inline=True)
            embed.add_field(name="latency", value="```Replies with the latency of the client```", inline=True)
            embed.add_field(name="schedule", value="```Schedule a flight```", inline=True)
            embed.add_field(name="atis <ICAO: str>", value="```Sends ATIS information for the specified airport```", inline=True)

            await ctx.reply(embed=embed)

        except Exception as e:
            await ctx.reply(e)


async def setup(bot):
    await bot.add_cog(Help(bot))
