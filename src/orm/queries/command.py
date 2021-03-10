from pony import orm
from src.orm.models import Guild, Command, Argument
from src.orm.serializer import HelpSerializer


class dbCommand():

    def __init__(self):
        self = self
    
    def __normalize_command(self, guild_id:str, command:str):
        c = orm.select(c for c in Command for g in Guild \
             if ((guild_id == g.id) and (c.language == g.language) \
                 and c.name == command)).first()
        translation = {
            'ayuda': 'help',
            'help': 'ayuda',
            'ayudaAdmin': 'adminHelp',
            'adminHelp': 'ayudaAdmin'
        }
        if (c is not None) and (c.name == command):
            return command
        return translation[command]

    ''' scope can be: 'admin' or 'anyone' '''
    @orm.db_session
    def get_commands(self, guild_id: str, command: str, scope: str):
        norm_command = self.__normalize_command(guild_id, command)
        query_header = orm.select( c for c in Command for g in Guild \
             if (g.id == guild_id) and (c.name == norm_command) and (c.scope == scope) and (c.language == g.language))
        query_commands = orm.select((c, a) for c in Command for g in Guild for a in Argument\
             if (a.command.id == c.id and c.name != norm_command) and (g.id == guild_id and c.language == g.language and c.scope == scope))
        return  HelpSerializer(list(query_commands), query_header.first()).serialize()
    
    @orm.db_session
    def get_admin_commands(self, guild_id: str, command: str, scope: str):
        norm_command = self.__normalize_command(guild_id, command)
        query_header = orm.select( c for c in Command for g in Guild \
             if (g.id == guild_id) and (c.name == norm_command) and (c.scope == scope) and (c.language == g.language))
        query_commands = orm.select((c, a) for c in Command for g in Guild for a in Argument\
             if (a.command.id == c.id and c.name != norm_command) and (g.id == guild_id and c.language == g.language and c.scope == scope))
        return  HelpSerializer(list(query_commands), query_header.first()).serialize()


db_command = dbCommand()
    

        