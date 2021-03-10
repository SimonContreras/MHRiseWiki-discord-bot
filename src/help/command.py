from discord.ext import commands
from src.help.embed import HelpEmbed
from src.orm.queries.command import db_command

class helpCog(commands.Cog):
    """
    Commands related to help
    ...

    Attributes
    ----------
    bot : commands.Bot
        Discord.ext class that implements Bot class

    Methods
    -------
    help(ctx, *args)
        Retrieve embeds related to command '?help',
        manage logic of interactive embed.

    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.name = 'Help Cog'
        self.description = 'Help commands MH Rise Wiki'
        self.__dbCommand = db_command

    @commands.command(name='ayuda', aliases=['help'])
    async def help(self, ctx: commands.Context, *args):
        """Manage rendered embeds of command '?help'

        Parameters
        ----------
        ctx : commands.Context
            context class that store data related to discord server
        *args : list
           List of params sent when the command was called

        Returns
        -------
        Message
            retrieve rendered embed
        """
        dct = self.__dbCommand.get_commands(str(ctx.guild.id), ctx.invoked_with, 'anyone')
        embed = HelpEmbed(ctx, dct)
        embed_main = embed.main()
        await ctx.send(embed=embed_main)


    @commands.command(name='ayudaAdmin', aliases=['adminHelp'])
    @commands.has_permissions(administrator=True)
    async def admin_help(self, ctx: commands.Context, *args):
        """Manage rendered embeds of command '?helpAdmin'

        Parameters
        ----------
        ctx : commands.Context
            context class that store data related to discord server
        *args : list
           List of params sent when the command was called

        Returns
        -------
        Message
            retrieve rendered embed
        """
        dct = self.__dbCommand.get_admin_commands(str(ctx.guild.id), ctx.invoked_with, 'admin')
        embed = HelpEmbed(ctx, dct)
        embed_main = embed.main()
        await ctx.send(embed=embed_main)
