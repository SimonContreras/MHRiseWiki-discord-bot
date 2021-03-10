from pony import orm
from src.orm.models import Guild, Language


class dbGuild():

    def __init__(self):
        self = self
                

    @orm.db_session
    def get_prefix(self, guild_id: str):
        guild = orm.select(l for l in Guild if l.id == guild_id).first()
        return guild.prefix
    
    @orm.db_session
    def update_prefix(self, guild_id: str, new_prefix: str):
        guild = orm.select(l for l in Guild if l.id == guild_id).first()
        guild.prefix = new_prefix
        orm.commit()
        return new_prefix
    
    @orm.db_session
    def create(self, guild_id: str):
        try:
            guild = Guild(
                id = guild_id,
                language = 1 #default language Spanish
            )
            orm.commit()
        except Exception as e:
            return False
        return True
    
    @orm.db_session
    def delete(self, guild_id: str):
        try:
            guild = Guild[guild_id].delete()
            orm.commit()
        except Exception as e:
            return False
        return True
    
    @orm.db_session
    def update_language(self, guild_id: str, new_lang: str):
        new_l = orm.select(l for l in Language if l.initials == new_lang).first()
        guild = orm.select(l for l in Guild if l.id == guild_id).first()
        guild.language = new_l
        orm.commit()
        return new_lang
    
    @orm.db_session
    def get_language(self, guild_id: str):
        lang = orm.select(l for g in Guild  for l in Language if (g.id == guild_id)).first()
        return lang.initials


db_guild = dbGuild()