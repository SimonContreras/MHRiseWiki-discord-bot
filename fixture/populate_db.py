import os
import sys
sys.path.insert(0,os.getcwd())
from fixture.dummy_data import dummy
from fixture.initial_data import populate_database
from src.orm.models import db

if __name__ == "__main__":
    print('I: -> Creating tables...')
    db.create_tables(check_tables=True)
    print('II: -> Inserting data...')
    populate_database()
    dummy()