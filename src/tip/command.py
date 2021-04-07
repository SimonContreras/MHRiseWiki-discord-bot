from discord.ext import commands
from src.tip.embed import TipEmbed
from src.orm.queries.tip import db_tip

class TipCog(commands.Cog):
    """
    Commands related to tip
    ...

    Attributes
    ----------
    bot : commands.Bot
        Discord.ext class that implements Bot class

    Methods
    -------
    tip(ctx, *args)
        Retrieve embeds related to command '?tipList',
        manage logic of interactive embed.
    create(ctx, *args)
        Retrieve embeds related to command '?tipCreate [name] [link]',
        manage logic of interactive embed.
    delete(ctx, *args)
        Retrieve embeds related to command '?tipDelete [tip-name]',
        manage logic of interactive embed.

    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.name = 'Tip Cog'
        self.description = 'Tips commands MH Rise Wiki'
        self._dbTip = db_tip

    @commands.command(name='tipLista', aliases=['tipList'])
    async def tipList(self, ctx: commands.Context, *args):
        """Manage rendered embeds of command '?tipList'

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
        dct = self._dbTip.get_tips()
        embed = TipEmbed(ctx, dct)
        embed_list = embed.list()
        await ctx.send(embed=embed_list)

    @commands.command(name='tipCrear', aliases=['tipCreate'])
    async def tipCreate(self, ctx: commands.Context, *args):
        """Manage rendered embeds of command '?tipCreate'

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
        success = self._dbTip.create(args[0],args[1])
        embed = TipEmbed(ctx, success)
        embed_status = embed.status_create()
        await ctx.send(embed=embed_status)
    
    @commands.command(name='tipEliminar', aliases=['tipDelete'])
    async def tipDelete(self, ctx: commands.Context, *args):
        """Manage rendered embeds of command '?tipDelete'

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
        dct = self._dbTip.delete(args[0])
        embed = TipEmbed(ctx, dct)
        embed_status = embed.status_delete()
        await ctx.send(embed=embed_status)