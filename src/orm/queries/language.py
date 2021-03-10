from pony import orm
from src.orm.models import Language


class dbLanguage():

    def __init__(self):
        self = self
                

    @orm.db_session
    def get_languages(self):
        languages = list(orm.select(l.initials for l in Language))
        return languages
    

db_language = dbLanguage()