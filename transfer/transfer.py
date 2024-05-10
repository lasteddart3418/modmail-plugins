#test
import discord
from datetime import datetime
from discord.ext import commands


from core import checks
from core.models import PermissionLevel

options_menu="You have provided invalid dept code.\n\n`dge` - Discord Growth Experts\n`pt` - Partnership Team\n`sales` - Sales team\n`et` - Events Team\n`mod` - Moderation Team\n`management` - Management Team\n`bugs` - Bug Handlers\n`purchases` - Sales Team Purchase Setup"

DEPS_DATA = {
    "dge": {
        "category_id": 692462165470478337,
        "pretty_name": "DISCORD GROWTH EXPERT",
        "reminders": "1. Do __NOT__ DM the invite link unless asked to.\n2. Be patient. It will take some time to wait for DGE to get to you.\n3. Please read the pins in #growth-questions channel before asking for help here.",
        "role_id": 692411479936335993,
        "send_message_to_user": True
    },
    "pt": {
        "category_id": 692462475009982515,
        "pretty_name": "PARTNERSHIP TEAM",
        "reminders": None,
        "role_id": 692411386789232681,
        "send_message_to_user": True
    },
    "sales": {
        "category_id": 706568047271608391,
        "pretty_name": "SALES TEAM",
        "reminders": None,
        "role_id": 706568993627963434,
        "send_message_to_user": True
    },
    "mod": {
        "category_id": 707459219393347634,
        "pretty_name": "TRUST AND SAFETY TEAM",
        "reminders": "If you are reporting an offense please send us the user's ID and proof of the offense.",
        "role_id": 1065596123332481084,
        "send_message_to_user": True
    },
    "et": {
        "category_id": 736571220585349140,
        "pretty_name": "EVENTS TEAM",
        "reminders": None,
        "role_id": 737065323647205598,
        "send_message_to_user": True
    },
    "management": {
        "category_id": 692463503633547406,
        "pretty_name": "MANAGEMENT TEAM",
        "reminders": None,
        "role_id": 692394098396627004,
        "send_message_to_user": True
    },
    "purchases": {
        "category_id": 1134556566348124232,
        "pretty_name": "PREMIUM SERVICES / PURCHASES TEAM",
        "reminders": None,
        "role_id": 706568993627963434,
        "send_message_to_user": True
    },
    "bugs": {
        "category_id": 692514669591789608,
        "pretty_name": "BUG REPORTS DEPARTMENT",
        "reminders": None,
        "role_id": 1063109499600257044,
        "send_message_to_user": True
    },
}
class AYS(commands.Cog, name="AYS Main Commands"):
    def __init__(self, bot):
        self.bot = bot
        
        
       
    @commands.command()
    @checks.thread_only()
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def transfer(self, ctx, *, to: str=None):
        """Command that transfers thread to other departments."""
        if to is None:
            embed = discord.Embed(title=f"Department Transfer", description=options_menu,
                                  color=discord.Color.red(), timestamp=datetime.utcnow())
            return await ctx.send(embed=embed)
        to = to.lower()
        data = None
        try:
            data = DEPS_DATA[to]
        except:
            embed = discord.Embed(title=f"Department Transfer",description=options_menu,
                                  color=discord.Color.red(), timestamp=datetime.utcnow())
            await ctx.send(embed=embed)
            return

        if data["send_message_to_user"]:
            mes = "You are being transferred to **`"
            mes += data["pretty_name"]
            mes += "`**.\n"
            mes += "Please remain __patient__ while we find a suitable staff member to assist in your request.\n\n"
            
            if data["reminders"] is not None:
                mes += "**__Reminders__**\n"
                mes += data["reminders"]

            msg = ctx.message
            msg.content = mes
            
            await ctx.thread.reply(msg, anonymous = False)
        
        await ctx.channel.edit(category=self.bot.get_channel(data["category_id"]), sync_permissions=True) 
        await ctx.send("<@&%s>" % str(data["role_id"]))

    @commands.command()
    @checks.thread_only()
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def stransfer(self, ctx, to: str=None):
        """Silently transfers thread"""
        if to is None:
            embed = discord.Embed(title=f"Silent Transfer", description=options_menu,
                                  color=discord.Color.red(), timestamp=datetime.utcnow())
            return await ctx.send(embed=embed)
        to = to.lower()
        data = None
        try:
            data = DEPS_DATA[to]
        except:
            embed = discord.Embed(title=f"Silent Transfer",description=options_menu,
                                  color=discord.Color.red(), timestamp=datetime.utcnow())
            await ctx.send(embed=embed)
            return

        await ctx.channel.edit(category=self.bot.get_channel(data["category_id"]), sync_permissions=True) 
        await ctx.send("Silent Transfer - <@&%s>" % str(data["role_id"]))

    @commands.command()
    @checks.thread_only()
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def id(self, ctx):
        await ctx.send(ctx.thread.id)

async def setup(bot):
    await bot.add_cog(AYS(bot))
