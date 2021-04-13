import os
import discord
from discord.ext import commands
from src.skill.embed import SkillEmbed
from src.common.embed import CommonEmbed
from src.common.utils import InputParser
from src.orm.queries.header import db_header
from src.orm.queries.skill import db_skill

class SkillCog(commands.Cog):
    """
    Commands related to skill

    Attributes
    ----------
    bot : commands.Bot
        Discord.ext class that implements Bot class

    Methods
    -------
    skill(ctx, *args)
        Retrieve embeds related to command '?skill'

    """
    def __init__(self, bot: commands.Bot):
        self._bot = bot
        self.name = 'Skill Cog'
        self.description = '''Skill commands MH Rise Wiki'''
        self.__dbHeader = db_header
        self.__dbSkill = db_skill
        self._skill_img_route=os.getenv('SKILL_LOCATION_ROUTE')

    @commands.command(name='hab', aliases=['skill'])
    async def skill(self, ctx: commands.Context, *args):
        """Manage rendered embeds of command '?skill'

        Parameters
        ----------
        ctx : commands.Context
            context class that store data related to discord server
        *args : list
           List of params sent when the command is called

        Returns
        -------
        Message
            retrieve rendered embed
        """
        skill_name = InputParser(args).concat()
        dct = self.__dbSkill.get(str(ctx.guild.id), skill_name)
        if dct == None:
            dct = self.__dbHeader.entity_not_found(str(ctx.guild.id), 'skill_not_found')
            foooter = self.__dbHeader.get_footer(str(ctx.guild.id), 'general_footer')
            embed = CommonEmbed(dct, foooter, ctx)
            await ctx.send(embed=embed.notFound())

        else:
            headers = self.__dbHeader.get_headers(str(ctx.guild.id), ctx.invoked_with)
            thumbnail_file = discord.File(self._skill_img_route+dct['icon'], filename=dct['icon'])
            embed = SkillEmbed(dct, headers)
            embed_main, embed_deco = embed.main()

            if embed_deco is None:
                await ctx.send(embed = embed_main, file=thumbnail_file)
            else:
                message = await ctx.send(embed=embed_main, file=thumbnail_file)
                await message.add_reaction('▶')
                valid_reactions = ['▶']
                
                def check(reaction, user):
                    return user == ctx.author

                reaction = None
                reaction_used = []
                while True:
                    if str(reaction) in valid_reactions and str(reaction) not in reaction_used:
                        reaction_used.append(str(reaction))
                        deco_file = discord.File(self._skill_img_route+dct['icon'], filename=dct['icon'])
                        await ctx.send(embed=embed_deco, file=deco_file)
                    try:
                        reaction, user = await self._bot.wait_for(event='reaction_add', timeout = 60.0, check = check)
                        await message.remove_reaction(reaction, user)
                    except:
                        break

                await message.clear_reactions()
    
