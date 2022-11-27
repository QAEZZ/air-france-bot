import discord

from discord import ui
from discord.ext import commands
from discord.ui import Select, View, Button


class scheduleModal(ui.Modal, title="Flight Schedule Dialog"):
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
    


    async def on_submit(self, interaction: discord.Interaction):
        embed: discord.Embed = discord.Embed(
            title=f"Air France Flight {self.flight_number}", color=discord.Color.from_rgb(47, 49, 54),
            description=f"""```
{self.trip_type}
Departing from - {self.departing_airport}
Arriving to    - {self.arriving_airport}

Departing at   - {self.departing_time} Zulu (UTC)```"""
        )
        embed.set_footer("This is a test")
        await interaction.response.send_message(embed=embed)


class Schedule(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.eColor = discord.Color.from_rgb(47, 49, 54)

    @commands.command()
    async def schedule(self, ctx):
        embed: discord.Embed = discord.Embed(
            title="Schedule a flight?", color=self.eColor
        )

        async def schedule_callback(interaction):
            await interaction.response.send_modal(scheduleModal())
            await interaction.message.edit(view=view)

        schedule_button = Button(label="Schedule", style=discord.ButtonStyle.green)
        view = View(timeout=300)

        schedule_button.callback = schedule_callback

        view.add_item(schedule_button)

        await ctx.reply(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Schedule(bot))
