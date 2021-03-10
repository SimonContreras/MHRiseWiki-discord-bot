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
        self.bot = bot
        self.name = 'Skill Cog'
        self.description = '''Skill commands MH Rise Wiki'''
        self.__dbHeader = db_header
        self.__dbSkill = db_skill

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
            embed = SkillEmbed(dct, headers)
            embed_main = embed.main()
            await ctx.send(embed=embed_main)
    
    
