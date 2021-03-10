import discord
from discord.ext import commands
import datetime
from src.orm.models import Header

class CommonEmbed(discord.Embed):
    """
    Embed with standard structure to show a simple message
    ...

    Attributes
    ----------
    dct : dict
        Dictionary with info to show in embed
    footer : Header
        Header with footer info based in command that trigger this embed
    ctx: commands.Context
        Data related to discord server and user that triggers the command
    
    Methods
    -------
    notFound(self)
        Retrieves embed with message related to resource not found in the Wiki

    """
    def __init__(self, dct: dict, foooter: Header, ctx: commands.Context):
        self.__dct = dct
        self.__foooter = foooter
        self.__ctx = ctx
    
    def notFound(self):
        """ Retrieve embed with message related to resource not found in the Wiki

        Parameters
        ----------

        Returns
        -------
        Embed
            retrieve embed with 'not found' info
        """
        embed= discord.Embed(title=self.__dct['name'], description=self.__dct['translation'], color=discord.Color.red())
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text=self.__foooter.translation.format(prefix=self.__ctx.prefix))
        return embed
