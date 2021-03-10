from discord import Guild
from discord.ext import commands
from src.prefix.embed import PrefixEmbed
from src.orm.queries.guild import db_guild
from src.orm.queries.header import db_header


class PrefixCog(commands.Cog):
    """
    Commands and events related to Prefix
    ...

    Attributes
    ----------
    bot : commands.Bot
        Discord.ext class that implements Bot class

    Methods
    -------
    on_guild_join(ctx, guild)
        add default prefix to db for the new guild joined
    on_guild_remove(ctx, guild)
        remove guild from db when guild remove bot
    change_prefix(ctx, prefix)
        change command prefix for a especific guild

    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.name = 'Prefix Cog'
        self.description = '''Prefix management commands MH Rise Wiki '''
        self.__dbGuild = db_guild
        self.__dbHeader = db_header


    @commands.Cog.listener()
    async def on_guild_join(self, guild: Guild):
        """Add new guild id to db with default prefix '?'

        Parameters
        ----------
        guild: Guild
            Guild object 

        Returns
        -------
        bool
            Status of new row in db for new guild
        """
        if self.__dbGuild.create(str(guild.id)):
            return True
        return False
    
    @commands.Cog.listener()
    async def on_guild_remove(self, guild: Guild):
        """Remove guild from db

        Parameters
        ----------
        guild: Guild
            Guild object 

        Returns
        -------
        bool
            Status of remove row in db
        """
        if self.__dbGuild.delete(str(guild.id)):
            return True
        return False
    
    @commands.command(name='cambiarPrefijo', aliases=['changePrefix'])
    @commands.has_permissions(administrator=True)
    async def change_prefix(self, ctx: commands.Context, prefix: str):
        """Add new guild to db with default prefix '?'

        Parameters
        ----------
       ctx: commands.Context
            Info related to discord server that triggers command
        prefix: str
            new prefix to update, max length 3
        
        Returns
        -------
        Message
            Embed with info related to prefix change
        """
        if len(prefix) > 3:
            header = self.__dbHeader.get_error_msg(str(ctx.guild.id), 'prefix_cant_be_change')
            embed = PrefixEmbed(header, prefix)
            await ctx.send(embed=embed.main())
        
        else:
            new_prefix = self.__dbGuild.update_prefix(str(ctx.guild.id), prefix)          
            header = self.__dbHeader.get_error_msg(str(ctx.guild.id), 'prefix_change_succesfully')
            embed = PrefixEmbed(header, new_prefix)
            await ctx.send(embed=embed.main())




    
