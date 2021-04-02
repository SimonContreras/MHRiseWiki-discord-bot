import os
import discord
from discord.ext import commands
from src.monster.embed import MonsterEmbed
from src.common.embed import CommonEmbed
from src.common.utils import InputParser
from src.orm.queries.header import db_header
from src.orm.queries.monster import db_monster

class MonsterCog(commands.Cog):
    """
    Commands related to Monster
    ...

    Attributes
    ----------
    bot : commands.Bot
        Discord.ext class that implements Bot class

    Methods
    -------
    monster(ctx, *args)
        Retrieve embeds related to command '?monster',
        manage logic of interactive embed.

    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.name = 'Monster Cog'
        self.description = '''Monsters info commands MH Rise Wiki'''
        self.__dbHeader = db_header
        self.__dbMonster = db_monster
        self.__assets_route = os.getenv('THUMBNAIL_ROUTE')
        self._monster_img_route = os.getenv('MONSTER_IMG_ROUTE')
        

    @commands.command(name='monstruo', aliases=['monster'])
    async def monster(self, ctx: commands.Context, *args):
        """Manage rendered embeds of command '?monster', manage interactive
        actions in embed via reactions.

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
        monster_name = InputParser(args).concat()
        dct = self.__dbMonster.get_monster(str(ctx.guild.id), monster_name)
        if dct == None:
            dct = self.__dbHeader.entity_not_found(str(ctx.guild.id), 'monster_not_found')
            foooter = self.__dbHeader.get_footer(str(ctx.guild.id), 'general_footer')
            embed = CommonEmbed(dct, foooter, ctx)
            await ctx.send(embed=embed.notFound())

        else:
            headers = self.__dbHeader.get_headers(str(ctx.guild.id), ctx.invoked_with)
            thumbnail_file = discord.File(self.__assets_route+dct['img-url'], filename=dct['img-url'])
            embed = MonsterEmbed(dct, headers)
            page1, page2 = embed.main()
            page1_1, page2_1 = embed.details()
                       
            if page2 is None:
                await ctx.send(embed = page1, file=thumbnail_file)
                await ctx.send(embed=page1_1)
            else:
                main_pages = [page1, page2]
                detail_pages = [page1_1, page2_1]
                
                
                message = await ctx.send(embed = page1, file=thumbnail_file)
                message2 = await ctx.send(embed=page1_1)
                await message2.add_reaction('⏮')
                await message2.add_reaction('◀')
                await message2.add_reaction('▶')
                await message2.add_reaction('⏭')
                await message2.add_reaction('⏹')
                
                def check(reaction, user):
                    return user == ctx.author

                i = 0
                reaction = None

                while True:
                    if str(reaction) == '⏮':
                        i = 0
                        await message.edit(embed = main_pages[i])
                        await message2.edit(embed = detail_pages[i])
                    elif str(reaction) == '◀':
                        if i > 0:
                            i -= 1
                            await message.edit(embed = main_pages[i])
                            await message2.edit(embed = detail_pages[i])
                    elif str(reaction) == '▶':
                        if i < 1:
                            i += 1
                            await message.edit(embed = main_pages[i])
                            await message2.edit(embed = detail_pages[i])
                    elif str(reaction) == '⏭':
                        i = 1
                        await message.edit(embed = main_pages[i])
                        await message2.edit(embed = detail_pages[i])
                    elif str(reaction) == '⏹':
                            break
                    
                    try:
                        reaction, user = await self.bot.wait_for(event='reaction_add', timeout = 30.0, check = check)
                        await message2.remove_reaction(reaction, user)
                    except:
                        break

                await message2.clear_reactions()
    
    @commands.command(name='hitzones')
    async def hzv(self, ctx: commands.Context, *args):
        monster_name = InputParser(args).concat()
        dct = self.__dbMonster.get_hzv(str(ctx.guild.id), monster_name)
        if dct is None:
            dct = self.__dbHeader.entity_not_found(str(ctx.guild.id), 'monster_not_found')
            foooter = self.__dbHeader.get_footer(str(ctx.guild.id), 'general_footer')
            embed = CommonEmbed(dct, foooter, ctx)
            await ctx.send(embed=embed.notFound())

        else:
            headers = {}
            embed = MonsterEmbed(dct,headers)
            embed_hzv = embed.hzv()
            hzv_file = discord.File(self._monster_img_route+'hzv/'+dct['img-url'], filename=dct['img-url'])
            await ctx.send(embed=embed_hzv, file=hzv_file)
