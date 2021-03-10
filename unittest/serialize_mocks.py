armor_dct = {
                'name': 'alatreon beta',
                'rarity': 10, 
                'set-bonus': {'description': 'TODO', 'name': 'TODO'},
                'pieces': [
                        {
                        'crafting-mats': [{'name': 'hierba', 'quantity': 4}], 
                        'max-def': 500, 
                        'min-def': 200, 
                        'name': 'cabeza alatreon', 
                        'rarity': 10, 
                        'resistances': {'dragon': 5, 'fire': 10, 'ice': 20, 'thunder': -5, 'water': -10}, 
                        'skills': [{'level': 2, 'name': 'bonus punto debil'}], 
                        'slots': {'1': 1, '2': 1, '3': 2}, 
                        'type': 'head'},
                    {
                    'crafting-mats': [{'name': 'hierba', 'quantity': 4}], 
                    'max-def': 500, 
                    'min-def': 200, 
                    'name': 'cabeza alatreon', 
                    'rarity': 10, 
                    'resistances': {'dragon': 5, 'fire': 10, 'ice': 20, 'thunder': -5, 'water': -10}, 
                    'skills': [{'level': 2, 'name': 'bonus punto debil'}], 
                    'slots': {'1': 1, '2': 1, '3': 2}, 
                    'type': 'head'},
                    {
                    'crafting-mats': [{'name': 'hierba', 'quantity': 4}], 
                    'max-def': 500, 
                    'min-def': 200, 
                    'name': 'cabeza alatreon', 
                    'rarity': 10, 
                    'resistances': {'dragon': 5, 'fire': 10, 'ice': 20, 'thunder': -5, 'water': -10}, 
                    'skills': [{'level': 2, 'name': 'bonus punto debil'}], 
                    'slots': {'1': 1, '2': 1, '3': 2}, 
                    'type': 'head'},
                    {
                    'crafting-mats': [{'name': 'hierba', 'quantity': 4}], 
                    'max-def': 500, 
                    'min-def': 200, 
                    'name': 'cabeza alatreon', 
                    'rarity': 10, 
                    'resistances': {'dragon': 5, 'fire': 10, 'ice': 20, 'thunder': -5, 'water': -10}, 
                    'skills': [{'level': 2, 'name': 'bonus punto debil'}], 
                    'slots': {'1': 1, '2': 1, '3': 2}, 
                    'type': 'head'},
                    {
                    'crafting-mats': [{'name': 'hierba', 'quantity': 4}], 
                    'max-def': 500, 
                    'min-def': 200, 
                    'name': 'cabeza alatreon', 
                    'rarity': 10, 
                    'resistances': {'dragon': 5, 'fire': 10, 'ice': 20, 'thunder': -5, 'water': -10}, 
                    'skills': [{'level': 2, 'name': 'bonus punto debil'}], 
                    'slots': {'1': 1, '2': 1, '3': 2}, 
                    'type': 'head'}
                ]}

armor_headers = {
            'armorset':'Bonus de set',
            'resistances':'Resistencias',
            'defenses':'Defensas :shield:',
            'pieces':'Partes',
            'slots':'Espacios adornos',
            'skills':'Habilidades',
            'craft-mats':'Materiales de crafteo'
        }

not_found_dct = {
                'command': 13,
                'id': 25, 
                'name': 'Oops!', 
                'translation': 'Armadura/Parte no en...n la Wiki.', 
                'type': 'armor_not_found'
                }

item_dct = {
            'craftable': 1, 
            'description': 'descripcion item 3 en esp', 
            'max': 7684, 
            'name': 'pocion', 
            'price': 30, 
            'product': 6, 
            'rarity': 1, 
            'recipe': {
                'items': [{'name': 'hierba', 'quantity': 4}, {'name': 'seta-azul', 'quantity': 1}], 
                'product': 6
                }
            }

item_headers = {
        'combination': 'Combinación', 
        'max-carry': 'Máx equipable', 
        'price': 'Valor', 'rarity': 'Rareza'
        }

help_dct = {
            'title': 'test title',
            'commands': [
                {
                    'name': 'test_command_1',
                    'params': '[test-param_1]',
                    'description': 'description test 1'
                },
                 {
                    'name': 'test_command_2',
                    'params': '[test-param_2]',
                    'description': 'description test 2'
                }
            ]

        }

monster_dct = {
                'name': 'alatreon',
                'species': 'Dragon Anciano',
                'description': 'Un símbolo de...',
                'img-url': 'alatreon.png',
                'ailments': ['fuego', 'trueno', 'hielo', 'dragon', 'nitro', 'efluvio'],
                'inmune': ['fuego', 'aturdir'],
                'weakness-3': ['trueno', 'dragon'],
                'weakness-2': ['hielo', 'veneno', 'parálisis'],
                'weakness-1': ['agua', 'sueño', 'nitro'],
                'has-alt-weakness': True,
                'alt-state-description': 'modo furia',
                'alt-inmune': ['fuego'],
                'alt-weakness-3': ['trueno', 'parálisis'],
                'alt-weakness-2': ['agua', 'hielo', 'sueño', 'aturdir'],
                'alt-weakness-1': ['dragon', 'veneno', 'nitro'],
                'locations': ['BosquePrimigenio', 'Isla Ingle'],
                'breakable': ['cuerno', 'cola'],
                'weak-points': [
                    {'blunt': 10, 'dragon': 40, 'fire': 20, 'ice': 40, 'part': 'cabeza', 
                    'ranged': 20, 'sever': 20, 'stunt': 5, 'thunder': 40, 'water': 30},
                    {'blunt': 10, 'dragon': 40, 'fire': 20, 'ice': 40, 'part': 'cabeza', 
                    'ranged': 20, 'sever': 20, 'stunt': 5, 'thunder': 40, 'water': 30},
                    {'blunt': 10, 'dragon': 40, 'fire': 20, 'ice': 40, 'part': 'cabeza', 
                    'ranged': 20, 'sever': 20, 'stunt': 5, 'thunder': 40, 'water': 30}],
                'alt-weak-points': [
                    {'blunt': 10, 'dragon': 40, 'fire': 20, 'ice': 40, 'part': 'cabeza', 
                    'ranged': 20, 'sever': 0, 'stunt': 5, 'thunder': 40, 'water': 30},
                    {'blunt': 10, 'dragon': 40, 'fire': 20, 'ice': 40, 'part': 'cabeza', 
                    'ranged': 20, 'sever': 0, 'stunt': 5, 'thunder': 40, 'water': 30},
                    {'blunt': 10, 'dragon': 40, 'fire': 20, 'ice': 40, 'part': 'cabeza', 
                    'ranged': 20, 'sever': 0, 'stunt': 5, 'thunder': 40, 'water': 30},
                    ]
            }

monster_headers = {
            'species': 'Especie',
            'ailments': 'E.alterado/Plagas',
            'inmune': 'Resiste',
            'weakness-3': 'Debilidad :star: :star: :star:',
            'weakness-2': 'Debilidad :star: :star:',
            'weakness-1': 'Debilidad :star:',
            'breakable': 'Rompible/Cortable',
            'location': 'Locación',
            'second-state': 'Segundo Estado',
            'weakpoints': 'Puntos débiles',
            'weakpoints-attacks': '> **{}**  \n > Corte {} \n > Impacto {} \n > Disparo {}',
        }

skill_dct = {
                'name': 'bonus punto debil',
                'description': 'Aumenta la afinidad de ataques que aprove....',
                'talisman': 'Talisman Provecho',
                'levels': [
                            {'description': 'Los ataques en punto...s heridas.', 'level': '1'}, 
                            {'description': 'Los ataques en punto...s heridas.', 'level': '2'},
                            {'description': 'Los ataques en punto...s heridas.', 'level': '3'}
                        ],
                'jewels': [
                            {'level': '1', 'name': 'Joya ablandadora 1'}, 
                            {'level': '2', 'name': 'Joya ablandadora 2'}
                        ]  
            }

skill_headers = {'jewels': 'Joyas', 'level': 'Nivel', 'talisman': 'Talismán'}

weapon_dct = {
                'name': 'cross 2',
                'type': 'light-bowgun',
                'rarity': 11,
                'attack': 331,
                'real-attack': 202,
                'damage-type': 'shot',
                'affinity': 15,
                'defense': 100,
                'elderseal': 'low',
                'shelling': 'long',
                'shelling-lvl': 5,
                'special-ammo': 'wyvernblast',
                'deviation': 'high',
                'elements': [{'attack': 230, 'name': 'fire'}, {'attack': 340, 'name': 'water'}],
                'slots': {'1': 1, '2': 1, '3': 1},
                'coatings': [
                                {'name': 'blast', 'quantity': 20}, {'name': 'close', 'quantity': 10}, 
                                {'name': 'paralysis', 'quantity': 30}, {'name': 'poison', 'quantity': 20}, 
                                {'name': 'power', 'quantity': 20}, {'name': 'sleep', 'quantity': 20}
                            ],
                'sharpness': 'blue',
                'sharpness-max': False,
                'create-items': [],
                'upgrade-items': [
                        {'name': 'seta-azul', 'quantity': 5}, 
                        {'name': 'pocion', 'quantity': 2}],
                'ammos': {
                            'weapon': 2,
                            'deviation': 'high',
                            'special_ammo': 'wyvernblast',
                            'normal1_clip': 20,
                            'normal1_rapid': True,
                            'normal1_recoil': 1,
                            'normal1_reload': 'slow',
                            'normal2_clip': 10,
                            'normal2_rapid': False,
                            'normal2_recoil': 1,
                            'normal2_reload': 'slow',
                            'normal3_clip': 0,
                            'normal3_rapid': False,
                            'normal3_recoil': 0,
                            'normal3_reload': '-',
                            'pierce1_clip': 0,
                            'pierce1_rapid': False,
                            'pierce1_recoil': 0,
                            'pierce1_reload': '-',
                            'pierce2_clip': 0,
                            'pierce2_rapid': False,
                            'pierce2_recoil': 0,
                            'pierce2_reload': '-',
                            'pierce3_clip': 0,
                            'pierce3_rapid': False,
                            'pierce3_recoil': 0,
                            'pierce3_reload': '-',
                            'spread1_clip': 0,
                            'spread1_rapid': False,
                            'spread1_recoil': 0,
                            'spread1_reload': '-',
                            'spread2_clip': 0,
                            'spread2_rapid': False,
                            'spread2_recoil': 0,
                            'spread2_reload': '-',
                            'spread3_clip': 0,
                            'spread3_rapid': False,
                            'spread3_recoil': 0,
                            'spread3_reload': '-',
                            'sticky1_clip': 0,
                            'sticky1_rapid': False,
                            'sticky1_recoil': 0,
                            'sticky1_reload': '-',
                            'sticky2_clip': 0,
                            'sticky2_rapid': False,
                            'sticky2_recoil': 0,
                            'sticky2_reload': '-',
                            'sticky3_clip': 0,
                            'sticky3_rapid': False,
                            'sticky3_recoil': 0,
                            'sticky3_reload': '-',
                            'cluster1_clip': 0,
                            'cluster1_rapid': False,
                            'cluster1_recoil': 0,
                            'cluster1_reload': '-',
                            'cluster2_clip': 0,
                            'cluster2_rapid': False,
                            'cluster2_recoil': 0,
                            'cluster2_reload': '-',
                            'cluster3_clip': 0,
                            'cluster3_rapid': False,
                            'cluster3_recoil': 0,
                            'cluster3_reload': '-',
                            'recover1_clip': 0,
                            'recover1_rapid': False,
                            'recover1_recoil': 0,
                            'recover1_reload': '-',
                            'recover2_clip': 0,
                            'recover2_rapid': False,
                            'recover2_recoil': 0,
                            'recover2_reload': '-',
                            'poison1_clip': 0,
                            'poison1_rapid': False,
                            'poison1_recoil': 0,
                            'poison1_reload': '-',
                            'poison2_clip': 0,
                            'poison2_rapid': False,
                            'poison2_recoil': 0,
                            'poison2_reload': '-',
                            'paralysis1_clip': 0,
                            'paralysis1_rapid': False,
                            'paralysis1_recoil': 0,
                            'paralysis1_reload': '-',
                            'paralysis2_clip': 0,
                            'paralysis2_rapid': False,
                            'paralysis2_recoil': 0,
                            'paralysis2_reload': '-',
                            'sleep1_clip': 0,
                            'sleep1_rapid': False,
                            'sleep1_recoil': 0,
                            'sleep1_reload': '-',
                            'sleep2_clip': 0,
                            'sleep2_rapid': False,
                            'sleep2_recoil': 0,
                            'sleep2_reload': '-',
                            'exhaust1_clip': 0,
                            'exhaust1_rapid': False,
                            'exhaust1_recoil': 0,
                            'exhaust1_reload': '-',
                            'exhaust2_clip': 0,
                            'exhaust2_rapid': False,
                            'exhaust2_recoil': 0,
                            'exhaust2_reload': '-',
                            'flaming_clip': 0,
                            'flaming_rapid': False,
                            'flaming_recoil': 0,
                            'flaming_reload': '-',
                            'water_clip': 0,
                            'water_rapid': False,
                            'water_recoil': 0,
                            'water_reload': '-',
                            'freeze_clip': 0,
                            'freeze_rapid': False,
                            'freeze_recoil': 0,
                            'freeze_reload': '-',
                            'thunder_clip': 0,
                            'thunder_rapid': False,
                            'thunder_recoil': 0,
                            'thunder_reload': '-',
                            'dragon_clip': 0,
                            'dragon_rapid': False,
                            'dragon_recoil': 0,
                            'dragon_reload': '-',
                            'slicing_clip': 0,
                            'slicing_rapid': False,
                            'slicing_recoil': 0,
                            'slicing_reload': '-',
                            'wyvern_clip': 5,
                            'wyvern_rapid': False,
                            'wyvern_recoil': 0,
                            'wyvern_reload': 'slow',
                            'demon_clip': 0,
                            'demon_rapid': False,
                            'demon_recoil': 0,
                            'demon_reload': '-',
                            'armor_clip': 0,
                            'armor_rapid': False,
                            'armor_recoil': 0,
                            'armor_reload': '-',
                            'tranq_clip': 10,
                            'tranq_rapid': False,
                            'tranq_recoil': 1,
                            'tranq_reload': 'normal'
                            },
            'previous-weapon': 'cross 1',
            'next-weapon': 'cross 3'
        }

weapon_headers = {
            'type': 'Tipo',
            'rarity': 'Rareza',
            'attack': 'Ataque',
            'real-attack': 'Ataque Real',
            'damage-type': 'Tipo de daño',
            'affinity': 'Afinidad',
            'defense': 'Defensa',
            'elderseal': 'Sello de ancianos',
            'special-ammo': 'Munición especial',
            'deviation': 'Desviación',
            'slots': 'Espacios',
            'craft-materials': 'Mat.Crafteo',
            'upgrade-materials': 'Mat.Mejora',
            'shelling-type': 'Tipo de disparo',
            'element-ailment': 'Elem/E.Alterado',
            'coating': 'Revestimientos',
            'sharpness': 'Filo',
            'next-upgrade': 'Siguiente Mejora',
            'ammo-type': 'Tipo de munición',
            'next-weapon': 'Siguiente Mejora',
            'previous-weapon': 'Mejora Anterior',
            'capacity': 'Capacidad',
            'rapid-fire': 'Fuego Rápido',
            'recoil': 'Retroceso',
            'reload': 'Recarga',
    }