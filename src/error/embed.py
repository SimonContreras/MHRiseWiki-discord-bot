import discord
from discord.ext import commands
from src.orm.models import Header

class ErrorEmbed(discord.Embed):
    """
    Embed with standard structure to show a simple error message
    ...

    Attributes
    ----------
    header :Header
        Header obj with info related to the error
    ctx: commands.Context
        obj with info related to discord server that triggers the error
    
    Methods
    -------
    main(self)
        Embed object with info related to an error triggered by an exception

    """
    def __init__(self, header: Header, ctx: commands.Context):
        self.__h = header
        self.__ctx = ctx

    def main(self):
        """ Retrieve embed with message related to an error triggered by an Exception

        Parameters
        ----------

        Returns
        -------
        Embed
            retrieve embed with error info
        """
        embed= discord.Embed(color=discord.Color.red())
        if self.__h.type in ['disabled_command', 'private_message_only', 'no_private_message']:
            embed.add_field(name=self.__h.name, value=self.__h.translation.format(command=self.__ctx.command), inline=True)
        elif self.__h.type == 'missing_required_argument':
            embed.add_field(name=self.__h.name, value=self.__h.translation.format(params=self.__ctx.invoked_with,
                prefix=self.__ctx.prefix, command=self.__ctx.command), inline=True)
        else:
            embed.add_field(name=self.__h.name, value=self.__h.translation, inline=True)
        return embed

   