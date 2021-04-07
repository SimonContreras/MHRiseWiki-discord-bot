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
            print(self._monster_img_route+'icon/'+dct['img-url'])
            print(dct['img-url'])
            headers = self.__dbHeader.get_headers(str(ctx.guild.id), ctx.invoked_with)
            thumbnail_file = discord.File(self._monster_img_route+'icon/'+dct['img-url'], filename=dct['img-url'])
            embed = MonsterEmbed(ctx, dct, headers)
            page1, page2 = embed.main()
                       
            if page2 is None:
                await ctx.send(embed = page1, file=thumbnail_file)
            else:
                main_pages = [page1, page2]
                
                
                message = await ctx.send(embed = page1, file=thumbnail_file)
                await message.add_reaction('⏮')
                await message.add_reaction('◀')
                await message.add_reaction('▶')
                await message.add_reaction('⏭')
                await message.add_reaction('⏹')
                
                def check(reaction, user):
                    return user == ctx.author

                i = 0
                reaction = None

                while True:
                    if str(reaction) == '⏮':
                        i = 0
                        await message.edit(embed = main_pages[i])
                    elif str(reaction) == '◀':
                        if i > 0:
                            i -= 1
                            await message.edit(embed = main_pages[i])
                    elif str(reaction) == '▶':
                        if i < 1:
                            i += 1
                            await message.edit(embed = main_pages[i])
                    elif str(reaction) == '⏭':
                        i = 1
                        await message.edit(embed = main_pages[i])
                    elif str(reaction) == '⏹':
                            break
                    
                    try:
                        reaction, user = await self.bot.wait_for(event='reaction_add', timeout = 30.0, check = check)
                        await message.remove_reaction(reaction, user)
                    except:
                        break

                await message.clear_reactions()
    
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
            embed = MonsterEmbed(ctx, dct, headers)
            embed_hzv = embed.hzv()
            hzv_file = discord.File(self._monster_img_route+'hzv/'+dct['img-url'], filename=dct['img-url'])
            await ctx.send(embed=embed_hzv, file=hzv_file)
    

    def __drops_path(self, rank:str, lang:int):
        if lang == 1:
            if rank in ['high', 'alto']:
                return 'drops/alto/'
            elif rank in ['low', 'alto']:
                return 'drops/bajo/'
        elif lang == 2:
            if rank in ['high', 'alto']:
                return 'drops/high/'
            elif rank in ['low', 'alto']:
                return 'drops/low/'

    @commands.command(name='mats')
    async def drops(self, ctx: commands.Context, *args):
        monster_name, rank = InputParser(args).triplet()
        dct = self.__dbMonster.get_drops(str(ctx.guild.id), monster_name, rank)
        if dct is None:
            dct = self.__dbHeader.entity_not_found(str(ctx.guild.id), 'monster_not_found')
            foooter = self.__dbHeader.get_footer(str(ctx.guild.id), 'general_footer')
            embed = CommonEmbed(dct, foooter, ctx)
            await ctx.send(embed=embed.notFound())

        else:
            headers = {}
            embed = MonsterEmbed(ctx, dct, headers)
            embed_hzv = embed.drops()
            sub_path = self.__drops_path(rank, dct['language'])
            hzv_file = discord.File(self._monster_img_route+sub_path+dct['img-url'], filename=dct['img-url'])
            await ctx.send(embed=embed_hzv, file=hzv_file)
