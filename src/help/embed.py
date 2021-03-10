from discord.ext import commands
import discord
import datetime


class HelpEmbed(discord.Embed):
    """
    Embed that renders help command, listing all commands available for anyone
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
    main(self)
        Retrieves embed with message related to available commands

    """
    def __init__(self, ctx: commands.Context, dct: dict):
        self.__ctx = ctx
        self.__dct = dct

    def main(self):
        """ Retrieve embed with commands information

        Parameters
        ----------

        Returns
        -------
        Embed
            Embed with commands information
        """
        embed= discord.Embed(title=self.__dct['title'], color=discord.Color.green())
        for command in self.__dct['commands']:
            text = '**' + self.__ctx.prefix + command['name'] + ' ' + command['params'] + '**'
            embed.add_field(name=text, value=command['description'], inline=False)
       
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text='Mh Rise Wiki')

        return embed