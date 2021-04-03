import os
import sys
sys.path.insert(0,os.getcwd())
from fixture.initial_data import *
from fixture.csv_loaders import *
from src.orm.models import db

@db_session
def populate_database():
    print('III: 1/13 -> Inserting Available languages.')
    load_languages('./fixture/csv/languages.csv')
    load_guild()
    print('III: 2/13 -> Inserting languages headers/titles.')
    language_errors_headers()
    print('III: 3/13 -> Inserting Default guild.')
    print('III: 4/13 -> Inserting common headers/titles.')
    common_errors_headers()
    print('III: 5/13 -> Inserting help command arguments headers/titles.')
    insert_help_commands_and_args()
    print('III: 6/13 -> Inserting not found headers/titles.')
    command_not_found_errors_headers()
    print('III: 7/13 -> Inserting footer headers/titles.')
    footers_headers()
    print('III: 8/13 -> Inserting prefix command headers/titles.')
    prefix_commands_and_headers()
    print('III: 9/13 -> Inserting monster command headers/titles.')
    monster_command_headers()
    print('III: 10/13 -> Inserting item command headers/titles.')
    item_command_headers()
    print('III: 11/13 -> Inserting weapon command headers/titles')
    weapon_command_headers()
    print('III: 12/13 -> Inserting skill headers/titles.')
    skill_command_headers()
    print('III: 13/13 -> Inserting armor command headers/titles.')
    load_locations('./fixture/csv/locations.csv')
    load_monster_stats('./fixture/csv/monsters-stats.csv')
    load_monster_esp_text('./fixture/csv/monsters-esp-text.csv')
    load_monsters_habitats('./fixture/csv/monsters-habitats.csv')
    print('III: Initial data done!!')
    armor_command_headers()

if __name__ == "__main__":
    print('I: -> Creating tables...')
    db.create_tables(check_tables=True)
    print('II: -> Inserting data...')
    populate_database()
    