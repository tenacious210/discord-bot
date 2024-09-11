import json
from datetime import timezone
import discord
from dateutil import parser
from discord.ext import commands
from discord.ext.commands import Context

with open("config/config.json", "r") as config_json:
    config = json.load(config_json)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command(name="utc")
async def timestamp(ctx: Context, *, time_string: str):
    try:
        parsed_time = parser.parse(time_string)
        parsed_time = parsed_time.replace(tzinfo=timezone.utc)

        parsed_str = parsed_time.strftime("%H:%M")

        discord_timestamp = f"<t:{int(parsed_time.timestamp())}:R> "
        discord_timestamp += f"(<t:{int(parsed_time.timestamp())}:t> in your time) "
        discord_timestamp += "<:pepoturkey:937794779817857024>"

        await ctx.send(f"{parsed_str} UTC is {discord_timestamp}")
    except Exception as e:
        await ctx.send(f"error: {e} <:temmiedank:1268096818974031915>")


if __name__ == "__main__":
    bot.run(config["disc_auth"])
