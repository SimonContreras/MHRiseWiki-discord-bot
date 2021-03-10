from discord.ext import commands
from src.language.embed import LanguageEmbed
from src.orm.queries.language import db_language
from src.orm.queries.header import db_header
from src.orm.queries.guild import db_guild

class LanguageCog(commands.Cog):
    """
    Commands related to changeLanguage
    ...

    Attributes
    ----------
    bot : commands.Bot
        Discord.ext class that implements Bot class

    Methods
    -------
    change_language(ctx, lang)
        Retrieve embeds related to command '?changeLanguage'

    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.name = 'Language Cog'
        self.description = ''' Language management commands MH Rise Wiki '''
    
        self.__dbLanguage = db_language
        self.__dbGuild = db_guild
        self.__messageHandler = db_header
    
    @commands.command(name='cambiarIdioma', aliases=['changeLanguage'])
    @commands.has_permissions(administrator=True)
    async def change_language(self, ctx: commands.Context, lang: str):
        """Manage rendered embeds of command '?changeLanguage'

        Parameters
        ----------
        ctx : commands.Context
            context class that store data related to discord server
        lang : str
           Parameter wih the initials of the new language to set

        Returns
        -------
        Message
            retrieve rendered embed
        """
        languages = self.__dbLanguage.get_languages()
        if lang in languages:
            new_lang = self.__dbGuild.update_language(str(ctx.guild.id), lang)
            header = self.__messageHandler.get_error_msg(str(ctx.guild.id), 'language_changed')
        else:
            header = self.__messageHandler.get_error_msg(str(ctx.guild.id), 'language_not_supported')
        embed = LanguageEmbed(header,new_lang)
        await ctx.send(embed=embed.main())




    
