import os
import discord
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
        self._item_img_route = os.getenv('ITEM_IMG_ROUTE')
        self._map_img_route = os.getenv('ITEM_LOCATION_ROUTE')

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
            thumbnail_file = discord.File(self._item_img_route+dct['icon'], filename=dct['icon'])
            embed = ItemEmbed(dct, headers)
            embed_main, maps_embeds = embed.main()

            if len(maps_embeds) == 0:
                await ctx.send(embed = embed_main, file=thumbnail_file)
            else:
                
                number_to_emoji = {0: '0️⃣', 1:'1️⃣', 2:'2️⃣', 3:'3️⃣', 4:'4️⃣', 
                                    5:'5️⃣', 6:'6️⃣', 7:'7️⃣', 8:'8️⃣', 9:'9️⃣', 10:'🔟'}
                emoji_to_number = {'0️⃣':0, '1️⃣':1, '2️⃣':2, '3️⃣':3, '4️⃣':4, 
                                    '5️⃣':5, '6️⃣':6, '7️⃣':7, '8️⃣':8, '9️⃣':9, '🔟':10}
                message = await ctx.send(embed = embed_main, file=thumbnail_file)
                valid_reactions = []
                for k in range(0,len(maps_embeds)):
                    await message.add_reaction(number_to_emoji[k+1])
                    valid_reactions.append(number_to_emoji[k+1])
                
                def check(reaction, user):
                    return user == ctx.author

                reaction = None
                while True:
                    if str(reaction) in valid_reactions:
                        i = emoji_to_number[str(reaction)]
                        map_file = discord.File(self._map_img_route+maps_embeds[i-1]['map-img'], 
                                                filename=maps_embeds[i-1]['map-img'])
                        await ctx.send(embed=maps_embeds[i-1]['embed'], file=map_file)
                    try:
                        reaction, user = await self._bot.wait_for(event='reaction_add', timeout = 60.0, check = check)
                        await message.remove_reaction(reaction, user)
                    except:
                        break

                await message.clear_reactions()
    
    
