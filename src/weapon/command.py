from discord.ext import commands
from src.weapon.embed import WeaponEmbed
from src.common.embed import CommonEmbed
from src.common.utils import InputParser
from src.orm.queries.header import db_header
from src.orm.queries.weapon import db_weapon


class WeaponCog(commands.Cog):
    """
    Commands related to weapon
    ...

    Attributes
    ----------
    bot : commands.Bot
        Discord.ext class that implements Bot class

    Methods
    -------
    weapon(ctx, *args)
        Retrieve embeds related to command '?help',
        manage logic of interactive embed.

    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.name = 'Weapon Cog'
        self.description = '''Weapon info commands MH Rise Wiki'''
        self._dbWeapon = db_weapon
        self.__dbHeader = db_header

    @commands.command(name='arma', aliases=['weapon'])
    async def weapon(self, ctx: commands.Context, *args):
        """Manage rendered embeds of command '?weapon', manage
        interactive embeds via reactions

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
        weapon_name = InputParser(args).concat()
        dct = self._dbWeapon.get(str(ctx.guild.id), weapon_name)        
        if dct == None:
            dct =self.__dbHeader.entity_not_found(str(ctx.guild.id), 'weapon_not_found')
            foooter = self.__dbHeader.get_footer(str(ctx.guild.id), 'general_footer')
            embed = CommonEmbed(dct, foooter, ctx)
            await ctx.send(embed=embed.notFound())
        else:
            headers = self.__dbHeader.get_headers(str(ctx.guild.id), ctx.invoked_with)
            embed = WeaponEmbed(dct, ctx, headers)

            page1 = embed.main()

            
            if not embed.extra_page:
                await ctx.send(embed = page1)
            else:
                
                page2 = embed.details()
                pages = [page1, page2]

                message = await ctx.send(embed = page1)
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
                        await message.edit(embed = pages[i])
                    elif str(reaction) == '◀':
                        if i > 0:
                            i -= 1
                            await message.edit(embed = pages[i])
                    elif str(reaction) == '▶':
                        if i < 1:
                            i += 1
                            await message.edit(embed = pages[i])
                    elif str(reaction) == '⏭':
                        i = 1
                        await message.edit(embed = pages[i])
                    elif str(reaction) == '⏹':
                            break
                    
                    try:
                        reaction, user = await self.bot.wait_for(event='reaction_add', timeout = 30.0, check = check)
                        await message.remove_reaction(reaction, user)
                    except:
                        break

                await message.clear_reactions()
    
    
