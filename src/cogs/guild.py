import discord

from discord.ext import commands


class Guild(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    def get_guild(self):
        airfrance_guild = self.bot.guilds[0]
        print(airfrance_guild)
        return airfrance_guild


async def setup(bot):
    await bot.add_cog(Guild(bot))
