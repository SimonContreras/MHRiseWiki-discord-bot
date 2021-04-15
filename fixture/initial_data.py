from pony.orm import *
from src.orm.models import *


def common_errors_headers():
    '''
    Error messages related to command exceptions
    '''
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()
    
    nonComand = Command(
        name = 'noCommand_esp',
        title = 'Error',
        language = spanish,
        active=True,
        description = 'No command related, only control message'
    )

    ''' Spanish translations '''
    err1_esp = Header(
        id = 1,
        type = 'command_not_found',
        name = 'Error',
        translation = 'Este comando no existe en MH Rise Wiki.',
        command = nonComand  
    )
    err2_esp = Header(
        id = 2,
        type = 'disabled_command',
        name = 'Error',
        translation = 'El comando {command} está desactivado.',
        command = nonComand      
    )
    err3_esp = Header(
        id = 3,
        type = 'missing_required_argument',
        name = 'Error',
        translation = 'Falta el argumento **{params}** para el comando **{prefix}{command}**.',
        command = nonComand        
    )
    err4_esp = Header(
        id = 4,
        type = 'no_private_message',
        name = 'Error',
        translation = 'El comando {command} no puede ser usado en mensaje privado.',
        command = nonComand       
    )
    err5_esp = Header(
        id = 5,
        type = 'private_message_only',
        name = 'Error',
        translation = 'El comando {command} **sólo** puede ser usado en mensaje privado.',
        command = nonComand       
    )
    err6_esp = Header(
        id = 6,
        type = 'bad_argument',
        name = 'Error',
        translation = 'Argumento no válido.',
        command = nonComand       
    )
    err7_esp = Header(
        id = 7,
        type = 'user_input_error',
        name = 'Error',
        translation = 'Argumento no válido.',
        command = nonComand      
    )

    ''' English translation '''
    nonComand_eng = Command(
        name = 'noCommand_eng',
        title = 'Error',
        language = english,
        active=True,
        description = 'No command related, only control message'
    )

    err1_eng = Header(
        id = 8,
        type = 'command_not_found',
        name = 'Error',
        translation = 'Command not found in MH Rise Wiki.',
        command = nonComand_eng      
    )

    err2_eng = Header(
        id = 9,
        type = 'disabled_command',
        name = 'Error',
        translation = 'The command {command} is disabled.',
        command = nonComand_eng   
    )

    err3_eng = Header(
        id = 10,
        type = 'missing_required_argument',
        name = 'Error',
        translation = 'Argument **{params}** not found for command **{prefix}{command}**.',
        command = nonComand_eng   
    )

    err4_eng = Header(
        id = 11,
        type = 'no_private_message',
        name = 'Error',
        translation = "Command {command} can't be use on private messages.",
        command = nonComand_eng    
    )

    err5_eng = Header(
        id = 12,
        type = 'private_message_only',
        name = 'Error',
        translation = 'Command {command} **only** can be use on private messages.',
        command = nonComand_eng    
    )

    err6_eng = Header(
        id = 13,
        type = 'bad_argument',
        name = 'Error',
        translation = 'Invalid argument.',
        command = nonComand_eng      
    )

    err7_esp = Header(
        id = 14,
        type = 'user_input_error',
        name = 'Error',
        translation = 'Invalid argument.',
        command = nonComand_eng      
    )
    commit()

def language_errors_headers():

    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()

    cambiar_idioma = Command(
        language = spanish,
        name = 'cambiarIdioma',
        title = 'Cambiar Idioma',
        scope = 'admin',
        active = True,
        description = 'Cambiar Idioma del bot.'
    )

    change_language = Command(
        language = english,
        name = 'changeLanguage',
        title = 'Change Language',
        scope = 'admin',
        active = True,
        description = 'Change Language of the bot.'
    )

    arg_esp = Argument(
        name = '[sigla-idioma]',
        command = cambiar_idioma
    )

    arg_eng = Argument(
        name = '[language-initials]',
        command = change_language
    )

    msg1_esp = Header(
        id = 15,
        name = 'Notificación',
        type = 'language_not_supported',
        translation = 'Idioma no soportado.',
        command = cambiar_idioma
    )

    msg1_eng = Header(
        id = 16,
        name = 'Notification',
        type = 'language_not_supported',
        translation = 'Language not supported.',
        command = change_language
    )

    msg2_esp = Header(
        id = 17,
        name = 'Notification',
        type = 'language_changed',
        translation = 'Idioma cambiado a {new_lang}.',
        command = cambiar_idioma,   
    )

    msg2_eng = Header(
        id = 18,
        name = 'Notification',
        type = 'language_changed',
        translation = 'Language changed to {new_lang}',
        command = change_language   
    )
    commit()

def insert_help_commands_and_args():
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()

    ayuda = Command(
        language = spanish,
        name = 'ayuda',
        title = 'Comandos disponibles en la Wiki:',
        active = True,
        description = 'Lista comandos disponibles.'
    )

    help = Command(
        language = english,
        name = 'help',
        title = 'Commands available in the Wiki:',
        active = True,
        description = 'List available commands.'
    )

    a_ayuda = Command(
        language = spanish,
        name = 'ayudaAdmin',
        title = 'Comandos de administración:',
        active = True,
        description = 'Lista comandos disponibles.',
        scope='admin'
    )

    a_help = Command(
        language = english,
        name = 'adminHelp',
        title = 'Administration commands:',
        active = True,
        description = 'List available commands.',
        scope='admin'
    )

    arg_esp = Argument(
        name = '\u200b',
        command = ayuda
    )

    arg_eng = Argument(
        name = '\u200b',
        command = help
    )
    a_arg_esp = Argument(
        name = '\u200b',
        command = a_ayuda
    )

    a_arg_eng = Argument(
        name = '\u200b',
        command = a_help
    )

    monstruo = Command(
        language = spanish,
        name = 'monstruo',
        title = 'Información Monstruo',
        active = True,
        description = 'Lista información básica del monstruo.'
    )

    monster = Command(
        language = english,
        name = 'monster',
        title = 'Monster Information',
        active = True,
        description = 'List basic information about the monster.'
    )

    arg_monstruo = Argument(
        name = '[nombre-monstruo]',
        command = monstruo
    )

    arg_monster = Argument(
        name = '[monster-name]',
        command = monster
    )

    hitzone_esp = Command(
        language = spanish,
        name = 'hitzones',
        title = 'Hitzones del monstruo',
        active = True,
        description = 'Lista información numérica detallada del monstruo.'
    )

    hitzone_eng = Command(
        language = english,
        name = 'hitzones',
        title = 'Monster Hitzones',
        active = True,
        description = 'List detailed numeric information about the monster.'
    )

    arg_esp = Argument(
        name = '[nombre-monstruo]',
        command = hitzone_esp
    )

    arg_eng = Argument(
        name = '[monster-name]',
        command = hitzone_eng
    )

    item_esp = Command(
        language = spanish,
        name = 'item',
        title = 'Información del item',
        active = True,
        description = 'Lista información del item.'
    )

    item_eng = Command(
        language = english,
        name = 'item',
        title = 'Item information',
        active = True,
        description = 'List item information.'
    )

    arg_esp = Argument(
        name = '[nombre-item]',
        command = item_esp
    )

    arg_eng = Argument(
        name = '[item-name]',
        command = item_eng
    )

    armadura = Command(
        language = spanish,
        name = 'armadura',
        title = 'Información de armadura',
        description = 'Muestra información en detalle de la parte/set de armadura.'
    )

    armor = Command(
        language = english,
        name = 'armor',
        title = 'Armor information',
        description = 'Show detailed information about armor/set piece.'
    )

    arg_esp = Argument(
        name = '[nombre-armadura]',
        command = armadura
    )

    arg_eng = Argument(
        name = '[armor-name]',
        command = armor
    )

    hab = Command(
        language = spanish,
        name = 'hab',
        active=True,
        title = 'Información de habilidad',
        description = 'Muestra información de la habilidad.'
    )

    skill = Command(
        language = english,
        name = 'skill',
        active=True,
        title = 'Skill Information',

        description = 'Show information about certain skill.'
    )

    arg_esp = Argument(
        name = '[nombre-skill]',
        command = hab
    )

    arg_eng = Argument(
        name = '[skill-name]',
        command = skill
    )

    adorno = Command(
        language = spanish,
        name = 'adorno',
        title = 'Información del adorno',
        description = 'Muestra información del adorno.'
    )

    talisman = Command(
        language = english,
        name = 'talisman',
        title = 'Talisman Information',
        description = 'Show information about certain talisman.'
    )

    arg_esp = Argument(
        name = '[nombre-adorno]',
        command = adorno
    )

    arg_eng = Argument(
        name = '[talisman-name]',
        command = talisman
    )

    zona = Command(
        language = spanish,
        name = 'zona',
        title = 'Información de zona',
        description = 'Muestra información de la zona, mapa, etc.'
    )

    location = Command(
        language = english,
        name = 'location',
        title = 'Location Information',
        description = 'Show information about zone, map, etc.'
    )

    arg_esp = Argument(
        name = '[nombre-zona]',
        command = zona
    )

    arg_eng = Argument(
        name = '[location-name]',
        command = location
    )

    arma = Command(
        language = spanish,
        name = 'arma',
        title = 'Información de arma',
        description = 'Muestra información detallada del arma.'
    )

    weapon = Command(
        language = english,
        name = 'weapon',
        title = 'Weapon Information',
        description = 'Show information about a weapon.'
    )

    arg_esp = Argument(
        name = '[nombre-arma]',
        command = arma
    )

    arg_eng = Argument(
        name = '[weapon-name]',
        command = weapon
    )
    mats = Command(
        language = spanish,
        name = 'mats',
        title = 'Información materiales monstruo',
        active = True,
        description = 'Muestra materiales que da como recompensa un monstruo en un rango específico (alto/bajo).'
    )

    drops = Command(
        language = english,
        name = 'drops',
        title = 'Monster drops information',
        active = True,
        description = 'Show reward materials from a certain monster in a specific rank (high/low).'
    )

    arg_esp = Argument(
        name = '[nombre-monstruo] [rango]',
        command = mats
    )

    arg_eng = Argument(
        name = '[monster-name] [rank]',
        command = drops
    )
    
    commit()

def command_not_found_errors_headers():
    err_esp = Header(
            id = 19,
            type = 'item_not_found',
            name = 'Oops!',
            translation = 'Item no encontrado en la Wiki.',
            command = 11 
        ) 

    err_eng = Header(
            id = 20,
            type = 'item_not_found',
            name = 'Oops!',
            translation = 'Item not found in the Wiki.',
            command = 12
        )
    err_esp2 = Header(
            id = 21,
            type = 'skill_not_found',
            name = 'Oops!',
            translation = 'Habilidad no encontrada en la Wiki.',
            command = 15 
        ) 

    err_eng2 = Header(
            id = 22,
            type = 'skill_not_found',
            name = 'Oops!',
            translation = 'Skill not found in the Wiki.',
            command = 16
        ) 
    err_esp3 = Header(
            id = 23,
            type = 'monster_not_found',
            name = 'Oops!',
            translation = 'Monstruo no encontrado en la Wiki.',
            command = 7
        ) 

    err_eng3 = Header(
            id = 24,
            type = 'monster_not_found',
            name = 'Oops!',
            translation = 'Monster not found in the Wiki.',
            command = 8
        ) 
    err_esp4 = Header(
            id = 25,
            type = 'armor_not_found',
            name = 'Oops!',
            translation = 'Armadura/Parte no encontrada en la Wiki.',
            command = 13
        ) 

    err_eng4 = Header(
            id = 26,
            type = 'armor_not_found',
            name = 'Oops!',
            translation = 'Armor/Set not found in the Wiki.',
            command = 14
        ) 
    err_esp5 = Header(
            id = 27,
            type = 'weapon_not_found',
            name = 'Oops!',
            translation = 'Arma no encontrada en la Wiki.',
            command = 21 
        ) 

    err_eng5 = Header(
            id = 28,
            type = 'weapon_not_found',
            name = 'Oops!',
            translation = 'Weapon not found in the Wiki.',
            command = 22
        )
    err_esp6 = Header(
            id = 29,
            type = 'hitzones_not_found',
            name = 'Oops!',
            translation = 'Hitzones no encontrados en la Wiki.',
            command = 9 
        ) 

    err_eng6 = Header(
            id = 30,
            type = 'hitzones_not_found',
            name = 'Oops!',
            translation = 'Hitzones not found in the Wiki.',
            command = 10
        )
    err_esp7 = Header(
            id = 31,
            type = 'talisman_not_found',
            name = 'Oops!',
            translation = 'Talismán no encontrado en la Wiki.',
            command = 17
        ) 

    err_eng7 = Header(
            id = 32,
            type = 'talisman_not_found',
            name = 'Oops!',
            translation = 'Talisman not found in the Wiki.',
            command = 18
        )
    err_esp8 = Header(
            id = 33,
            type = 'location_not_found',
            name = 'Oops!',
            translation = 'Zona no encontrado en la Wiki.',
            command = 19 
        ) 

    err_eng8 = Header(
            id = 34,
            type = 'location_not_found',
            name = 'Oops!',
            translation = 'Location not found in the Wiki.',
            command = 20
        )
    commit()  

def footers_headers():
    footer_esp = Header(
            id = 35,
            type = 'general_footer',
            name = 'footer_esp',
            translation = 'Escribe {prefix}ayuda para más info en algún comando',
            command = 1
        ) 

    footer_eng = Header(
            id = 36,
            type = 'general_footer',
            name = 'footer_eng',
            translation = 'For more info about commands type {prefix}help',
            command = 2
        ) 
    commit()  

def prefix_commands_and_headers():
    
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()
    
    p_command_esp =  Command(
        name = 'cambiarPrefijo',
        title = 'Cambiar prefijo del bot.',
        language = spanish,
        description = 'Cambia prefijo para el bot.',
        scope='admin'
    )
    p_command_eng =  Command(
        name = 'changePrefix',
        title = 'Change prefix bot.',
        language = english,
        description = 'Change prefix of the bot.',
        scope='admin'
    )
    arg_esp = Argument(
        name = '[nuevo-prefijo]',
        command = p_command_esp
    )
    arg_esp = Argument(
        name = '[New-prefix]',
        command = p_command_eng
    )
    commit()
    p_esp = Header(
        id = 37,
        type = 'prefix_change_succesfully',
        name = 'Notificación',
        translation = 'Prefijo cambiado a {new_prefix}.',
        command = p_command_esp
    )
    p_eng = Header(
        id = 38,
        type = 'prefix_change_succesfully',
        name = 'Notification',
        translation = 'Prefix changed succesfully to {new_prefix}.',
        command = p_command_eng
    )
    p_esp2 = Header(
        id = 39,
        type = 'prefix_cant_be_change',
        name = 'Notificación',
        translation = 'El {prefix} no puede ser utilizado, largo mayor a 3.',
        command = p_command_esp
    )
    p_eng2 = Header(
        id = 40,
        type = 'prefix_cant_be_change',
        name = 'Notification',
        translation = 'Prefix {prefix} can not be used, length greather than 3.',
        command = p_command_eng
    )
    commit()

def monster_command_headers():
    monstruo = Command.select(lambda l: l.name == 'monstruo').first()
    monster = Command.select(lambda l: l.name == 'monster').first()

    specie_esp1 = Header(
        id = 41,
        name='species',
        translation='Especie',
        type='title',
        command=monstruo
    )
    specie_esp2 = Header(
        id = 42,
        name='ailments',
        translation='E.alterados',
        type='title',
        command=monstruo
    )
    specie_esp3 = Header(
        id = 43,
        name='inmune',
        translation='Resiste',
        type='title',
        command=monstruo
    )
    specie_esp4 = Header(
        id = 44,
        name='weakness-3',
        translation='Debilidad :star: :star: :star:',
        type='title',
        command=monstruo
    )
    specie_esp5 = Header(
        id = 45,
        name='weakness-2',
        translation='Debilidad :star: :star: ',
        type='title',
        command=monstruo
    )
    specie_esp6 = Header(
        id = 46,
        name='weakness-1',
        translation='Debilidad :star: ',
        type='title',
        command=monstruo
    )
    specie_esp7 = Header(
        id = 47,
        name='breakable',
        translation='Rompible/Cortable',
        type='title',
        command=monstruo
    )
    specie_esp8 = Header(
        id = 48,
        name='location',
        translation='Locación',
        type='title',
        command=monstruo
    )
    specie_eng1 = Header(
        id = 49,
        name='species',
        translation='Species',
        type='title',
        command=monster
    )
    specie_eng2 = Header(
        id = 50,
        name='ailments',
        translation='Ailments',
        type='title',
        command=monster
    )
    specie_eng3 = Header(
        id = 51,
        name='inmune',
        translation='Inmune',
        type='title',
        command=monster
    )
    specie_eng4 = Header(
        id = 52,
        name='weakness-3',
        translation='Weakness :star: :star: :star:',
        type='title',
        command=monster
    )
    specie_eng5 = Header(
        id = 53,
        name='weakness-2',
        translation='Weakness :star: :star: ',
        type='title',
        command=monster
    )
    specie_eng6 = Header(
        id = 54,
        name='weakness-1',
        translation='Weakness :star: ',
        type='title',
        command=monster
    )
    specie_eng7 = Header(
        id = 55,
        name='breakable',
        translation='Breakable/Severable',
        type='title',
        command=monster
    )
    specie_eng8 = Header(
        id = 56,
        name='location',
        translation='Location',
        type='title',
        command=monster
    )
    specie_eng9 = Header(
        id = 57,
        name='second-state',
        translation='Second State',
        type='title',
        command=monster
    )
    specie_eng10 = Header(
        id = 58,
        name='second-state',
        translation='Segundo Estado',
        type='title',
        command=monstruo
    )
    specie_eng11 = Header(
        id = 59,
        name='weakpoints',
        translation='Puntos débiles',
        type='title',
        command=monstruo
    )
    specie_eng12 = Header(
        id = 60,
        name='weakpoints',
        translation='Weak Points',
        type='title',
        command=monster
    )
    specie_eng13 = Header(
        id = 61,
        name='weakpoints-attacks',
        translation=' > **{}**  \n > Corte {} \n > Impacto {} \n > Disparo {}',
        type='title',
        command=monstruo
    )
    specie_eng14 = Header(
        id = 62,
        name='weakpoints-attacks',
        translation=' > **{}**  \n > Sever {} \n > Impact {} \n > Shot {}',
        type='title',
        command=monster
    )

def item_command_headers():
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()
    c_esp = Command.select(lambda c: (c.language == spanish and c.name == 'item')).first()
    c_eng = Command.select(lambda c: (c.language == english and c.name == 'item')).first()

    h1_esp = Header(
        id = 63,
        name = 'rarity',
        translation = 'Rareza',
        type= 'title',
        command = c_esp,
    )
    h1_eng = Header(
        id = 64,
        name = 'rarity',
        translation = 'Rarity',
        type= 'title',
        command = c_eng,
    )
    h2_esp = Header(
        id = 65,
        name = 'buy',
        translation = 'Comprar',
        type= 'title',
        command = c_esp,
    )
    h2_eng = Header(
        id = 66,
        name = 'buy',
        translation = 'Buy',
        type= 'title',
        command = c_eng,
    )
    h3_esp = Header(
        id = 67,
        name = 'max-carry',
        translation = 'Máx equipable',
        type= 'title',
        command = c_esp,
    )
    h3_eng = Header(
        id = 68,
        name = 'max-carry',
        translation = 'Máx carry',
        type= 'title',
        command = c_eng,
    )
    h4_esp = Header(
        id = 69,
        name = 'combination',
        translation = 'Combinación',
        type= 'title',
        command = c_esp,
    )
    h4_eng = Header(
        id = 70,
        name = 'combination',
        translation = 'Combination',
        type= 'title',
        command = c_eng,
    )

def weapon_command_headers():
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()
    c_esp = Command.select(lambda c: (c.language == spanish and c.name == 'arma')).first()
    c_eng = Command.select(lambda c: (c.language == english and c.name == 'weapon')).first()

    h1_esp = Header(
        id = 71,
        name = 'type',
        translation = 'Tipo',
        type= 'title',
        command = c_esp,
    )
    h1_eng = Header(
        id = 72,
        name = 'type',
        translation = 'Type',
        type= 'title',
        command = c_eng,
    )
    h2_esp = Header(
        id = 73,
        name = 'rarity',
        translation = 'Rareza',
        type= 'title',
        command = c_esp,
    )
    h2_eng = Header(
        id = 74,
        name = 'rarity',
        translation = 'Rarity',
        type= 'title',
        command = c_eng,
    )
    h3_esp = Header(
        id = 75,
        name = 'attack',
        translation = 'Ataque',
        type= 'title',
        command = c_esp,
    )
    h3_eng = Header(
        id = 76,
        name = 'attack',
        translation = 'Attack',
        type= 'title',
        command = c_eng,
    )
    h4_esp = Header(
        id = 77,
        name = 'real-attack',
        translation = 'Ataque Real',
        type= 'title',
        command = c_esp,
    )
    h4_eng = Header(
        id = 78,
        name = 'real-attack',
        translation = 'Real Attack',
        type= 'title',
        command = c_eng,
    )
    h5_esp = Header(
        id = 79,
        name = 'damage-type',
        translation = 'Tipo de daño',
        type= 'title',
        command = c_esp,
    )
    h5_eng = Header(
        id = 80,
        name = 'damage-type',
        translation = 'Damage type',
        type= 'title',
        command = c_eng,
    )
    h6_esp = Header(
        id = 81,
        name = 'affinity',
        translation = 'Afinidad',
        type= 'title',
        command = c_esp,
    )
    h6_eng = Header(
        id = 82,
        name = 'affinity',
        translation = 'Affinity',
        type= 'title',
        command = c_eng,
    )
    h7_esp = Header(
        id = 83,
        name = 'defense',
        translation = 'Defensa',
        type= 'title',
        command = c_esp,
    )
    h7_eng = Header(
        id = 84,
        name = 'defense',
        translation = 'Defense',
        type= 'title',
        command = c_eng,
    )
    h8_esp = Header(
        id = 85,
        name = 'elderseal',
        translation = 'Sello de ancianos',
        type= 'title',
        command = c_esp,
    )
    h8_eng = Header(
        id = 86,
        name = 'elderseal',
        translation = 'Elderseal',
        type= 'title',
        command = c_eng,
    )
    h9_esp = Header(
        id = 87,
        name = 'special-ammo',
        translation = 'Munición especial',
        type= 'title',
        command = c_esp,
    )
    h9_eng = Header(
        id = 88,
        name = 'special-ammo',
        translation = 'Special Ammo',
        type= 'title',
        command = c_eng,
    )
    h10_esp = Header(
        id = 89,
        name = 'deviation',
        translation = 'Desviación',
        type= 'title',
        command = c_esp,
    )
    h10_eng = Header(
        id = 90,
        name = 'deviation',
        translation = 'Deviation',
        type= 'title',
        command = c_eng,
    )
    h11_esp = Header(
        id = 91,
        name = 'slots',
        translation = 'Espacios',
        type= 'title',
        command = c_esp,
    )
    h11_eng = Header(
        id = 92,
        name = 'slots',
        translation = 'Slots',
        type= 'title',
        command = c_eng,
    )
    h12_esp = Header(
        id = 93,
        name = 'craft-materials',
        translation = 'Mat.Crafteo',
        type= 'title',
        command = c_esp,
    )
    h12_eng = Header(
        id = 94,
        name = 'craft-materials',
        translation = 'Crafting Mats',
        type= 'title',
        command = c_eng,
    )
    h12_esp = Header(
        id = 95,
        name = 'upgrade-materials',
        translation = 'Mat.Mejora',
        type= 'title',
        command = c_esp,
    )
    h12_eng = Header(
        id = 96,
        name = 'upgrade-materials',
        translation = 'Upgrade Mats',
        type= 'title',
        command = c_eng,
    )
    h13_esp = Header(
        id = 97,
        name = 'shelling-type',
        translation = 'Tipo de disparo',
        type= 'title',
        command = c_esp,
    )
    h13_eng = Header(
        id = 98,
        name = 'shelling-type',
        translation = 'Shelling type',
        type= 'title',
        command = c_eng,
    )
    h14_esp = Header(
        id = 99,
        name = 'element-ailment',
        translation = 'Elem/E.Alterado',
        type= 'title',
        command = c_esp,
    )
    h14_eng = Header(
        id = 100,
        name = 'element-ailment',
        translation = 'Element/Ailment',
        type= 'title',
        command = c_eng,
    )
    h15_esp = Header(
        id = 101,
        name = 'coating',
        translation = 'Revestimientos',
        type= 'title',
        command = c_esp,
    )
    h15_eng = Header(
        id = 102,
        name = 'coating',
        translation = 'Coatings',
        type= 'title',
        command = c_eng,
    )
    h16_esp = Header(
        id = 103,
        name = 'sharpness',
        translation = 'Filo',
        type= 'title',
        command = c_esp,
    )
    h16_eng = Header(
        id = 104,
        name = 'sharpness',
        translation = 'Sharpness',
        type= 'title',
        command = c_eng,
    )
    h17_esp = Header(
        id = 105,
        name = 'next-upgrade',
        translation = 'Siguiente Mejora',
        type= 'title',
        command = c_esp,
    )
    h17_eng = Header(
        id = 106,
        name = 'next-upgrade',
        translation = 'next Upgrade',
        type= 'title',
        command = c_eng,
    )
    h18_esp = Header(
        id = 107,
        name = 'ammo-type',
        translation = 'Tipo de munición',
        type= 'title',
        command = c_esp,
    )
    h18_eng = Header(
        id = 108,
        name = 'ammo-type',
        translation = 'Ammo Type',
        type= 'title',
        command = c_eng,
    )
    h19_esp = Header(
        id = 109,
        name = 'next-weapon',
        translation = 'Siguiente Mejora',
        type= 'title',
        command = c_esp,
    )
    h19_eng = Header(
        id = 110,
        name = 'next-weapon',
        translation = 'Next Upgrade',
        type= 'title',
        command = c_eng,
    )
    h20_esp = Header(
        id = 111,
        name = 'previous-weapon',
        translation = 'Mejora Anterior',
        type= 'title',
        command = c_esp,
    )
    h20_eng = Header(
        id = 112,
        name = 'previous-weapon',
        translation = 'Previous Upgrade',
        type= 'title',
        command = c_eng,
    )
    h21_esp = Header(
        id = 113,
        name = 'capacity',
        translation = 'Capacidad',
        type= 'title',
        command = c_esp,
    )
    h21_eng = Header(
        id = 114,
        name = 'capacity',
        translation = 'Capacity',
        type= 'title',
        command = c_eng,
    )
    h22_esp = Header(
        id = 115,
        name = 'rapid-fire',
        translation = 'Fuego Rápido',
        type= 'title',
        command = c_esp,
    )
    h22_eng = Header(
        id = 116,
        name = 'rapid-fire',
        translation = 'Rapid Fire',
        type= 'title',
        command = c_eng,
    )
    h23_esp = Header(
        id = 117,
        name = 'recoil',
        translation = 'Retroceso',
        type= 'title',
        command = c_esp,
    )
    h23_eng = Header(
        id = 118,
        name = 'recoil',
        translation = 'Retroceso',
        type= 'title',
        command = c_eng,
    )
    h24_esp = Header(
        id = 119,
        name = 'reload',
        translation = 'Recarga',
        type= 'title',
        command = c_esp,
    )
    h24_eng = Header(
        id = 120,
        name = 'reload',
        translation = 'Reload',
        type= 'title',
        command = c_eng,
    )

def skill_command_headers():
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()
    c_esp = Command.select(lambda c: (c.language == spanish and c.name == 'hab')).first()
    c_eng = Command.select(lambda c: (c.language == english and c.name == 'skill')).first()

    h1_esp = Header(
        id = 121,
        name = 'level',
        translation = 'Nivel',
        type= 'title',
        command = c_esp,
    )
    h1_eng = Header(
        id = 122,
        name = 'level',
        translation = 'Level',
        type= 'title',
        command = c_eng,
    )
    h2_esp = Header(
        id = 123,
        name = 'talisman',
        translation = 'Talismán',
        type= 'title',
        command = c_esp,
    )
    h2_eng = Header(
        id = 124,
        name = 'talisman',
        translation = 'Talisman',
        type= 'title',
        command = c_eng,
    )
    h3_esp = Header(
        id = 125,
        name = 'jewels',
        translation = 'Joyas',
        type= 'title',
        command = c_esp,
    )
    h3_eng = Header(
        id = 126,
        name = 'jewels',
        translation = 'Jewels',
        type= 'title',
        command = c_eng,
    )

def armor_command_headers():
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()
    c_esp = Command.select(lambda c: (c.language == spanish and c.name == 'armadura')).first()
    c_eng = Command.select(lambda c: (c.language == english and c.name == 'armor')).first()

    h1_esp = Header(
        id = 127,
        name = 'armorset',
        translation = 'Bonus de set',
        type= 'title',
        command = c_esp,
    )
    h1_eng = Header(
        id = 128,
        name = 'armorset',
        translation = 'Armor set bonus',
        type= 'title',
        command = c_eng,
    )
    h2_esp = Header(
        id = 129,
        name = 'resistances',
        translation = 'Resistencias',
        type= 'title',
        command = c_esp,
    )
    h2_eng = Header(
        id = 130,
        name = 'resistances',
        translation = 'Resistances',
        type= 'title',
        command = c_eng,
    )
    h3_esp = Header(
        id = 131,
        name = 'defenses',
        translation = 'Defensas :shield:',
        type= 'title',
        command = c_esp,
    )
    h3_eng = Header(
        id = 132,
        name = 'defenses',
        translation = 'Defenses :shield:',
        type= 'title',
        command = c_eng,
    )
    h4_esp = Header(
        id = 133,
        name = 'pieces',
        translation = 'Partes',
        type= 'title',
        command = c_esp,
    )
    h4_eng = Header(
        id = 134,
        name = 'pieces',
        translation = 'Pieces',
        type= 'title',
        command = c_eng,
    )
    h5_esp = Header(
        id = 135,
        name = 'slots',
        translation = 'Espacios adornos',
        type= 'title',
        command = c_esp,
    )
    h5_eng = Header(
        id = 136,
        name = 'slots',
        translation = 'Slots',
        type= 'title',
        command = c_eng,
    )
    h6_esp = Header(
        id = 137,
        name = 'skills',
        translation = 'Habilidades',
        type= 'title',
        command = c_esp,
    )
    h6_eng = Header(
        id = 138,
        name = 'skills',
        translation = 'Skills',
        type= 'title',
        command = c_eng,
    )
    h7_esp = Header(
        id = 139,
        name = 'craft-mats',
        translation = 'Materiales de crafteo',
        type= 'title',
        command = c_esp,
    )
    h7_eng = Header(
        id = 140,
        name = 'craft-mats',
        translation = 'Crafting Materials',
        type= 'title',
        command = c_eng,
    )

def more_item_headers():
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()
    c_esp = Command.select(lambda c: (c.language == spanish and c.name == 'item')).first()
    c_eng = Command.select(lambda c: (c.language == english and c.name == 'item')).first()

    h2_esp = Header(
        id = 141,
        name = 'sell',
        translation = 'Vender',
        type= 'title',
        command = c_esp,
    )
    h2_eng = Header(
        id = 142,
        name = 'sell',
        translation = 'Sell',
        type= 'title',
        command = c_eng,
    )
    h3_esp = Header(
        id = 143,
        name = 'category',
        translation = 'Categoría',
        type= 'title',
        command = c_esp,
    )
    h3_eng = Header(
        id = 144,
        name = 'category',
        translation = 'Category',
        type= 'title',
        command = c_eng,
    )
    h4_esp = Header(
        id = 145,
        name = 'location',
        translation = 'Obtenible en',
        type= 'title',
        command = c_esp,
    )
    h4_eng = Header(
        id = 146,
        name = 'location',
        translation = 'Obtainable in',
        type= 'title',
        command = c_eng,
    )
    h5_esp = Header(
        id = 147,
        name = 'rank',
        translation = 'rango',
        type= 'title',
        command = c_esp,
    )
    h5_eng = Header(
        id = 148,
        name = 'rank',
        translation = 'rank',
        type= 'title',
        command = c_eng,
    )
    h6_esp = Header(
        id = 149,
        name = 'zones',
        translation = 'zonas',
        type= 'title',
        command = c_esp,
    )
    h6_eng = Header(
        id = 150,
        name = 'zones',
        translation = 'zones',
        type= 'title',
        command = c_eng,
    )
    h7_esp = Header(
        id = 151,
        name = 'map-information',
        translation = 'Información mapa',
        type= 'title',
        command = c_esp,
    )
    h7_eng = Header(
        id = 152,
        name = 'map-information',
        translation = 'Map information',
        type= 'title',
        command = c_eng,
    )

def more_monster_headers():
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()
    c_esp = Command.select(lambda c: (c.language == spanish and c.name == 'monstruo')).first()
    c_eng = Command.select(lambda c: (c.language == english and c.name == 'monster')).first()

    h1_esp = Header(
        id = 153,
        name = 'traps',
        translation = 'Trampas',
        type= 'title',
        command = c_esp,
    )
    h1_eng = Header(
        id = 154,
        name = 'traps',
        translation = 'Traps',
        type= 'title',
        command = c_eng,
    )
    h2_esp = Header(
        id = 155,
        name = 'danger-level',
        translation = 'Nivel de peligro',
        type= 'title',
        command = c_esp,
    )
    h2_eng = Header(
        id = 156,
        name = 'danger-level',
        translation = 'Danger level',
        type= 'title',
        command = c_eng,
    )
    h3_esp = Header(
        id = 157,
        name = 'plagues',
        translation = 'Plagas',
        type= 'title',
        command = c_esp,
    )
    h3_eng = Header(
        id = 158,
        name = 'plagues',
        translation = 'Plagues',
        type= 'title',
        command = c_eng,
    )

def more_skill_headers():
    spanish = Language.select(lambda l: l.initials == 'esp').first()
    english = Language.select(lambda l: l.initials == 'eng').first()
    c_esp = Command.select(lambda c: (c.language == spanish and c.name == 'hab')).first()
    c_eng = Command.select(lambda c: (c.language == english and c.name == 'skill')).first()

    h1_esp = Header(
        id = 159,
        name = 'deco',
        translation = 'Decoración/Joya',
        type= 'title',
        command = c_esp,
    )
    h1_eng = Header(
        id = 160,
        name = 'deco',
        translation = 'Decoration/Jewel',
        type= 'title',
        command = c_eng,
    )
    h2_esp = Header(
        id = 161,
        name = 'rarity',
        translation = 'Rareza',
        type= 'title',
        command = c_esp,
    )
    h2_eng = Header(
        id = 162,
        name = 'rarity',
        translation = 'Rarity',
        type= 'title',
        command = c_eng,
    )
    h3_esp = Header(
        id = 163,
        name = 'slots',
        translation = 'Espacios',
        type= 'title',
        command = c_esp,
    )
    h3_eng = Header(
        id = 164,
        name = 'slots',
        translation = 'Slots',
        type= 'title',
        command = c_eng,
    )
    h4_esp = Header(
        id = 165,
        name = 'skill_lvl',
        translation = 'Nivel de habilidad',
        type= 'title',
        command = c_esp,
    )
    h4_eng = Header(
        id = 166,
        name = 'skill_lvl',
        translation = 'Skill Level',
        type= 'title',
        command = c_eng,
    )
    h5_esp = Header(
        id = 167,
        name = 'unlock',
        translation = 'Desbloqueable al cazar/llegar a',
        type= 'title',
        command = c_esp,
    )
    h5_eng = Header(
        id = 168,
        name = 'unlock',
        translation = 'Unlocked at hunt/reach:',
        type= 'title',
        command = c_eng,
    )
    h6_esp = Header(
        id = 169,
        name = 'mats',
        translation = 'Materiales',
        type= 'title',
        command = c_esp,
    )
    h6_eng = Header(
        id = 170,
        name = 'mats',
        translation = 'Materials',
        type= 'title',
        command = c_eng,
    )