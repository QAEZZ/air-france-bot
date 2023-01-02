import discord
from discord.ext import commands


class Book(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def book(self, ctx, flnum="MISSING"):
        if flnum != "MISSING":
            with open("./data/active_flights.txt", "r") as f:
                content = f.read()
                if flnum in content:
                    economy_class = discord.utils.get(ctx.guild.roles, name="[ Economy Class ]")
                    business_class = discord.utils.get(ctx.guild.roles, name="[ Business Class ]")
                    first_class = discord.utils.get(ctx.guild.roles, name="- [ First Class ]")

                    if first_class in ctx.author.roles:
                        class_ = "a First Class"
                    elif business_class in ctx.author.roles:
                        class_ = "a Business Class"
                    elif economy_class in ctx.author.roles:
                        class_ = "an Economy Class"
                    else:
                        class_ = "NONE"
                    
                    if class_ == "NONE":
                        await ctx.reply(f"Unable to book a flight for AF {flnum}. You do not have a class role.")
                    else:
                        with open("./data/roster/")
                        await ctx.reply(f"Booked {class_} flight for AF {flnum}")
                else:
                    await ctx.reply(f"That flight number does not exist!")
        else:
            await ctx.reply("Please enter a flight number.")

async def setup(bot):
    await bot.add_cog(Book(bot))
