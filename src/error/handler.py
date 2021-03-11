"""
Code copied and modified from:
https://gist.github.com/EvieePy/7822af90858ef65012ea500bcecf1612

Thanks to  @EvieePy
"""
import discord
import traceback
import sys
from discord.ext import commands
from src.orm.queries.header import db_header
from src.error.embed import ErrorEmbed

class CommandErrorHandler(commands.Cog):
    """
    Handler class that catch any exception triggered by a command
    ...

    Attributes
    ----------
    bot: commands.Bot
        Bot instance
    
    Methods
    -------
    on_command_error(self, ctx:commands.Context, error)
        Retrieves None or Message with and embed with error info

    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.description = '''Error Handler commands MH Rise Wiki'''
        self.__dbHeader = db_header


    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        """The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        
        Returns
        -------
        Message or None
            None when the exception ignored, a Message with an embed when error
            is inform to the user.
        """

        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        # This prevents any cogs with an overwritten cog_command_error being handled here.
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.ConversionError, commands.ArgumentParsingError,
                   commands.UnexpectedQuoteError, commands.InvalidEndOfQuotedStringError,
                   commands.ExpectedClosingQuoteError, commands.BadArgument, 
                   commands.CheckFailure, commands.CheckAnyFailure,
                   )

        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
        error = getattr(error, 'original', error)

        # Anything in ignored will return and prevent anything happening.
        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.CommandNotFound):
            message = self.__dbHeader.get_error_msg(str(ctx.guild.id), 'command_not_found')
            embed = ErrorEmbed(message, ctx)
            await ctx.send(embed=embed.main())

        elif isinstance(error, commands.DisabledCommand):
            msg = self.__dbHeader.get_error_msg(str(ctx.guild.id), 'disabled_command')
            msg.translation = msg.translation.format(ctx.command)
            embed = ErrorEmbed(msg, ctx)
            await ctx.send(embed=embed.main())
        
        elif isinstance(error, commands.MissingRequiredArgument):
            msg = self.__dbHeader.get_error_msg(str(ctx.guild.id), 'missing_required_argument')
            msg.translation = msg.translation.format(ctx.invoked_with, ctx.prefix, ctx.command) 
            embed = ErrorEmbed(msg, ctx)
            await ctx.send(embed=embed.main())

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                msg = self.__dbHeader.get_error_msg(str(ctx.guild.id), 'no_private_message') 
                msg.translation = msg.translation.format(ctx.command)
                embed = ErrorEmbed(msg, ctx)
                await ctx.author.send(embed=embed.main())
            except discord.HTTPException:
                pass
        
        elif isinstance(error, commands.PrivateMessageOnly):
            try:
                msg = self.__dbHeader.get_error_msg(str(ctx.guild.id), 'private_message_only') 
                msg.translation = msg.translation.format(ctx.command)
                embed = ErrorEmbed(msg, ctx)
                await ctx.send(embed=embed.main())
            except discord.HTTPException:
                pass

        # For this error example we check to see where it came from...
        elif isinstance(error, commands.BadArgument):
            message = self.__dbHeader.get_error_msg(str(ctx.guild.id), 'bad_argument') 
            embed = ErrorEmbed(message, ctx)
            await ctx.send(embed=embed.main())

        elif isinstance(error, commands.UserInputError):
            message = message = self.__dbHeader.get_error_msg(str(ctx.guild.id), 'user_input_error') 
            embed = ErrorEmbed(message, ctx)
            await ctx.send(embed=embed.main())
        else:
            # All other Errors not returned come here. And we can just print the default TraceBack.
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

   
    