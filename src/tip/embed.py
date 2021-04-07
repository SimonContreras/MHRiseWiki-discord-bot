from discord.ext import commands
import discord
import datetime


class TipEmbed(discord.Embed):
    """
    Embed that renders help command, listing all commands available for anyone
    ...

    Attributes
    ----------
    dct : dict
        Dictionary with info to show in embed
    footer : Header
        Header with footer info based in command that trigger this embed
    ctx: commands.Context
        Data related to discord server and user that triggers the command
    
    Methods
    -------
    main(self)
        Retrieves embed with message related to available commands

    """
    def __init__(self, ctx: commands.Context, dct: dict):
        self._ctx = ctx
        self._dct = dct

    def list(self):
        """ Retrieve embed with list of tips

        Parameters
        ----------

        Returns
        -------
        Embed
            Embed with commands information
        """
        embed= discord.Embed(title='Lista de Tips', color=discord.Color.blue())
        text = ' '
        for t in self._dct['tips']:
            text += f'''**-**{t['name']} \n'''
        embed.add_field(name=f'''Usa {self._ctx.prefix}tip para ver:''', value=text, inline=False)
       
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text='Mh Rise Wiki')

        return embed
    
    def status_create(self):
        """ Retrieve embed with transaction information

        Parameters
        ----------

        Returns
        -------
        Embed
            Embed with transaction information
        """
        embed = discord.Embed(title='Guardar nuevo Tip')
        if self._dct['status']:
            embed.color = discord.Color.green()
            text = 'El tip fue guardado exitosamente'
            value = f'''El nombre del tip es: **{self._dct['name']}**'''
        else:
            embed.color = discord.Color.red()
            text = 'El tip no pudo ser guardado'
            value = 'Prueba con otro nombre.'
        embed.add_field(name=text, value=value, inline=False)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text='Mh Rise Wiki')

        return embed
    
    def status_delete(self):
        """ Retrieve embed with transaction information

        Parameters
        ----------

        Returns
        -------
        Embed
            Embed with transaction information
        """
        embed = discord.Embed(title='Eliminar Tip')
        if self._dct['status']:
            embed.color = discord.Color.green()
            text = 'El tip fue eliminado exitosamente'
            value = f'''El tip **{self._dct['name']}** fue eliminado.'''
        else:
            embed.color = discord.Color.red()
            text = 'El tip no pudo ser eliminado'
            value = 'Prueba con otro nombre.'
        embed.add_field(name=text, value=value, inline=False)
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text='Mh Rise Wiki')

        return embed