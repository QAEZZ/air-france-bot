import discord

import datetime

from discord import ui, utils
from discord.ext import commands
from discord.ui import Select, View, Button


class postModal(ui.Modal, title="Post Flight Schedule Dialog"):
    try:
        fl_year = ui.TextInput(label="Year", style=discord.TextStyle.short,
                            placeholder="Format: Integer. Ex. 2023", required=True)
        
        fl_month = ui.TextInput(label="Month", style=discord.TextStyle.short,
                            placeholder="Format: Integer. Ex. 11", required=True)
        
        fl_day = ui.TextInput(label="Day", style=discord.TextStyle.short,
                            placeholder="Format: Integer. Ex. 05", required=True)
        
        fl_time = ui.TextInput(label="Time (UTC)", style=discord.TextStyle.short,
                            placeholder="Format: HH:MM. Ex. 23:05", required=True)
        
        fl_number = ui.TextInput(label="Flight Number", style=discord.TextStyle.short,
                            placeholder="Format: Integer. Ex. 4452", required=True)
        
        async def on_submit(self, interaction: discord.Interaction):
            await interaction.response.send_message("Coming soon...")

    except Exception as e:
        print(e)



class scheduleModal(ui.Modal, title="Flight Schedule Dialog"):
    try:
        flight_number = ui.TextInput(label="Flight Number", style=discord.TextStyle.short,
                            placeholder="Format: Integer. Ex. 4452", required=True, min_length=1)
        
        departing_airport = ui.TextInput(label="Departing Airport", style=discord.TextStyle.short,
                            placeholder="Format: AIRPORT [ICAO]. Ex. Chicago O'Hare Int'l [KORD]", required=True)
        
        arriving_airport = ui.TextInput(label="Arriving Airport", style=discord.TextStyle.short,
                            placeholder="Format: AIRPORT [ICAO]. Ex. Los Angeles Int'l [KLAX]", required=True)

        departing_date = ui.TextInput(label="Departing Date and Time", style=discord.TextStyle.short,
                            placeholder="Format: DD.MM.YYYY HH:MM Ex. 06.11.2022 08:20", required=True)
        
        trip_type = ui.TextInput(label="Trip Type", style=discord.TextStyle.short,
                            placeholder="One-way/Round-trip", required=True)

    except Exception as e:
        print(e)
    
    async def on_submit(self, interaction: discord.Interaction):
        try:
            with open("./data/active_flights.txt", "a") as f:
                f.write(f"{str(self.flight_number)}\n")
                f.close()
            embed: discord.Embed = discord.Embed(
                title=f"Flight AF {self.flight_number}", color=discord.Color.from_rgb(47, 49, 54),
                description=f"""
**{self.trip_type} Trip**

**Departing from**
    ``{self.departing_airport}``

**Arriving to**
    ``{self.arriving_airport}``

**Departing at**
    ``{self.departing_date} Zulu (UTC)``"""
            )
            embed.set_footer(text="Crew will be manually assigned and sent seperately")
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)


class testScheduleModal(ui.Modal, title="Test Flight Schedule Dialog"):
    try:
        flight_number = ui.TextInput(label="Flight Number", style=discord.TextStyle.short,
                            placeholder="Format: Integer. Ex. 4452", required=True, min_length=1)
        
        trip_type = ui.TextInput(label="Trip Type", style=discord.TextStyle.short,
                            placeholder="Format: One-way/Round-trip. Ex. Round-trip", required=True)
        
        departing_airport = ui.TextInput(label="Departing Airport", style=discord.TextStyle.short,
                            placeholder="Format: AIRPORT [ICAO]. Ex. Chicago O'Hare Int'l [KORD]", required=True)
        
        arriving_airport = ui.TextInput(label="Arriving Airport", style=discord.TextStyle.short,
                            placeholder="Format: AIRPORT [ICAO]. Ex. Los Angeles Int'l [KLAX]", required=True)
        
        departing_time = ui.TextInput(label="Departing Time", style=discord.TextStyle.short,
                            placeholder="In Zulu time (UTC). Ex. 22:00", required=True)

    except Exception as e:
        print(e)
    
    async def on_submit(self, interaction: discord.Interaction):
        try:
            embed: discord.Embed = discord.Embed(
                title=f"TEST\nFlight AF {self.flight_number}", color=discord.Color.from_rgb(47, 49, 54),
                description=f"""
**{self.trip_type} Trip**

**Departing from**
    ``{self.departing_airport}``

**Arriving to**
    ``{self.arriving_airport}``

**Departing at**
    ``{self.departing_time} Zulu (UTC)``"""
            )
            embed.set_footer(text="Crew will be manually assigned and sent seperately")
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)


class Schedule(commands.Cog):

    def __init__(self, bot):
        global airfrance_guild
        airfrance_guild = bot.guilds[0]
        print(airfrance_guild)
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def schedule(self, ctx):
        print(f"scheduled by {ctx.author}")

        async def schedule_callback(interaction):
            await ctx.message.delete()
            await msg.delete()
            await interaction.response.send_modal(scheduleModal())

        async def test_schedule_callback(interaction):
            await ctx.message.delete()
            await msg.delete()
            await interaction.response.send_modal(testScheduleModal())

        schedule_button = Button(label="Click to schedule a flight!", style=discord.ButtonStyle.green)
        test_schedule_button = Button(label="Click to schedule a test flight!", style=discord.ButtonStyle.blurple)

        view = View(timeout=300)

        schedule_button.callback = schedule_callback
        test_schedule_button.callback = test_schedule_callback

        view.add_item(schedule_button)
        view.add_item(test_schedule_button)

        msg = await ctx.reply(view=view)
    
    @commands.command()
    async def active(self, ctx, reset="MISSING"):
        if reset == "reset":
            with open("./data/active_flights.txt", "w") as f:
                f.write("")
                f.close()
                await ctx.reply("**Cleared all active flights**")

        else:
            with open("./data/active_flights.txt", "r") as f:
                embed: discord.Embed = discord.Embed(
                    title="Active Flights", description=f.read(), color=discord.Color.from_rgb(47, 49, 54)
                )
                f.close()
                await ctx.reply(embed=embed)
    
    @commands.command()
    async def post(self, ctx):
        print(f"posted by {ctx.author}")

        async def post_callback(interaction):
            await ctx.message.delete()
            await msg.delete()
            await interaction.response.send_modal(postModal())
        
        post_button = Button(label="Click to post a flight", style=discord.ButtonStyle.green)

        view = View(timeout=300)

        post_button.callback = post_callback

        view.add_item(post_button)

        msg = await ctx.reply(view=view)


async def setup(bot):
    await bot.add_cog(Schedule(bot))
