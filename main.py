import os
import discord
from discord.ext import commands
from src.orm.queries.guild import db_guild

from src.monster.command import MonsterCog
from src.prefix.command import PrefixCog
from src.error.handler import CommandErrorHandler
from src.help.command import helpCog
from src.armor.command import ArmorCog
from src.item.command import ItemCog
from src.skill.command import SkillCog
from src.weapon.command import WeaponCog
from src.language.command import LanguageCog
from src.tip.command import TipCog

TOKEN = os.getenv('DISCORD_TOKEN')

def get_prefix(bot: commands.Bot, message: discord.Message):
    guild_id = str(message.guild.id)
    prefix = db_guild.get_prefix(guild_id)
    return prefix

def setup():
    description = ''' MH Rise Wiki Bot'''
    bot = commands.Bot(command_prefix=get_prefix,
                        description=description,
                        help_command=None)
    

    bot.add_cog(MonsterCog(bot))
    bot.add_cog(helpCog(bot))
    bot.add_cog(CommandErrorHandler(bot))
    bot.add_cog(PrefixCog(bot))
    bot.add_cog(ArmorCog(bot))
    bot.add_cog(ItemCog(bot))
    bot.add_cog(SkillCog(bot))
    bot.add_cog(WeaponCog(bot))
    bot.add_cog(LanguageCog(bot))
    bot.add_cog(TipCog(bot))

    return bot

if __name__ == "__main__":
    bot = setup()

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'''MH Rise Wiki Bot, running!!''')
    await bot.change_presence(status=discord.Status.online,
                                activity=discord.Game(name='Monster Hunter Rise',
                                                    type=discord.ActivityType.playing))
    print(f'Successfully build in and booted...!')

bot.run(TOKEN, bot=True, reconnect=True)