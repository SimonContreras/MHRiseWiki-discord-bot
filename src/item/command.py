from discord.ext import commands
from src.common.utils import InputParser
from src.item.embed import ItemEmbed
from src.common.embed import CommonEmbed
from src.orm.queries.item import db_item
from src.orm.queries.header import db_header

class ItemCog(commands.Cog):
    """
    Commands related to Item
    ...

    Attributes
    ----------
    bot : commands.Bot
        Discord.ext class that implements Bot class

    Methods
    -------
    item(ctx, *args)
        Retrieve embeds related to command '?item'

    """
    def __init__(self, bot: commands.Bot):
        self._bot = bot
        self.name = 'Item Cog'
        self.description = '''Items commands MH Rise Wiki'''
        self.__dbItem = db_item
        self.__dbHeader = db_header

    @commands.command(name='item')
    async def item(self, ctx: commands.Context, *args):
        """Manage rendered embed of command '?item'

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
        item_name = InputParser(args).concat()
        dct = self.__dbItem.get_item(str(ctx.guild.id), item_name)
        if dct == None:
            dct = self.__dbHeader.entity_not_found(str(ctx.guild.id), 'item_not_found')
            foooter = self.__dbHeader.get_footer(str(ctx.guild.id), 'general_footer')
            embed = CommonEmbed(dct, foooter, ctx)
            await ctx.send(embed=embed.notFound())

        else:
            headers = self.__dbHeader.get_headers(str(ctx.guild.id), ctx.invoked_with)
            embed = ItemEmbed(dct, headers)
            embed_main = embed.main()
            await ctx.send(embed=embed_main)
    
    
