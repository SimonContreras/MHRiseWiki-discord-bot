from pony import orm
from src.orm.models import Header, Guild, Command
from src.orm.serializer import HeaderSerializer

class dbHeader():

    def __init__(self):
        self = self
    
    def normalize_command(self, guild_id:str, command:str):
        c = orm.select(c for c in Command for g in Guild \
             if ((guild_id == g.id) and (c.language == g.language) \
                 and c.name == command)).first()
        translation = {
            'item': 'item',
            'monstruo': 'monster',
            'arma': 'weapon',
            'ayuda': 'help',
            'hab': 'skill',
            'item': 'item',
            'monster': 'monstruo',
            'weapon': 'arma',
            'help': 'ayuda',
            'skill': 'hab',
            'armor': 'armadura',
        }
        if (c is not None) and (c.name == command):
            return command
        return translation[command]

    @orm.db_session
    def get_error_msg(self, guild_id: str, error: str):
        query = orm.select(h for c in Command for g in Guild for h in Header \
             if ((guild_id == g.id) and (c.language == g.language) \
                         and (h.command.id == c.id) and (h.type == error)))
        message = query.first()
        return message
    
    @orm.db_session
    def get_help_info(self, guild_id: str):
        query = orm.select(c for c in Command for g in Guild \
             if ((c.name != 'noCommand_eng') and (c.name != 'noCommand_esp') \
                and (g.id == guild_id) and (c.language == g.language)))
        return list(query)

    @orm.db_session
    def entity_not_found(self, guild_id: str, error: str):
        query = orm.select(h for c in Command for g in Guild for h in Header \
             if ((guild_id == g.id) and (c.language == g.language) \
                         and (h.command.id == c.id) and (h.type == error)))
        return query.first().to_dict()

    @orm.db_session
    def get_footer(self, guild_id:str, type:str):
        query = orm.select(h for c in Command for g in Guild for h in Header \
             if ((guild_id == g.id) and (c.language == g.language) \
                         and (h.command.id == c.id) and (h.type == type)))
        return query.first()

    @orm.db_session
    def get_headers(self, guild_id:str, command:str):
        n_command = self.normalize_command(guild_id, command)
        query = orm.select(h for c in Command for g in Guild for h in Header \
             if ((guild_id == g.id) and (c.language == g.language) and (c.name == n_command) \
                 and (h.command.id == c.id) and (h.type == 'title')))
        return HeaderSerializer.serialize(list(query))
    

db_header = dbHeader()
        