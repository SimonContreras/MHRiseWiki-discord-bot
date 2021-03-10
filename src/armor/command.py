from discord.ext import commands
from src.armor.embed import ArmorEmbed
from src.common.embed import CommonEmbed
from src.common.utils import InputParser
from src.orm.queries.header import db_header
from src.orm.queries.armor import db_armor

class ArmorCog(commands.Cog):
    """
    Commands related to Armor
    ...

    Attributes
    ----------
    bot : commands.Bot
        Discord.ext class that implements Bot class

    Methods
    -------
    armor(ctx, *args)
        Retrieve embeds related to command '?armor',
        manage logic of interactive embed.

    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.name = 'Armor Cog'
        self.description = '''Armor commands MH Rise Wiki'''
        self.__dbHeader = db_header
        self.__dbArmor = db_armor

    @commands.command(name='armadura', aliases=['armor'])
    async def armor(self, ctx: commands.Context, *args):
        """Manage rendered embeds of command '?armor', and behavior 
        of interactive embed.

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
        armor_name = InputParser(args).concat()
        dct = self.__dbArmor.get(str(ctx.guild.id), armor_name)
        if dct == None:
            dct = self.__dbHeader.entity_not_found(str(ctx.guild.id), 'armor_not_found')
            foooter = self.__dbHeader.get_footer(str(ctx.guild.id), 'general_footer')
            embed = CommonEmbed(dct, foooter, ctx)
            await ctx.send(embed=embed.notFound())

        else:
            headers = self.__dbHeader.get_headers(str(ctx.guild.id), ctx.invoked_with)
            embed = ArmorEmbed(dct,headers)
            page1 = embed.main()
            page2 = embed.details(0)
            page3 = embed.details(1)
            page4 = embed.details(2)
            page5 = embed.details(3)
            page6 = embed.details(4)
            
            pages = [page1, page2, page3, page4, page5, page6]

            message = await ctx.send(embed = page1)
            await message.add_reaction('⏮')
            await message.add_reaction('◀')
            await message.add_reaction('▶')
            await message.add_reaction('⏭')
            await message.add_reaction('⏭')
            await message.add_reaction('⏹') 

            def check(reaction, user):
                return user == ctx.author

            i = 0
            reaction = None

            while True:
                if str(reaction) == '⏮':
                    i = 0
                    await message.edit(embed = pages[i])
                elif str(reaction) == '◀':
                    if i > 0:
                        i -= 1
                        await message.edit(embed = pages[i])
                elif str(reaction) == '▶':
                    if i < 5:
                        i += 1
                        await message.edit(embed = pages[i])
                elif str(reaction) == '⏭':
                    i = 5
                    await message.edit(embed = pages[i])
                elif str(reaction) == '⏹':
                    break
                
                try:
                    reaction, user = await self.bot.wait_for(event='reaction_add', timeout = 30.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break

            await message.clear_reactions()
