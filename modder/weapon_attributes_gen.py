import json

materials = ('steel',)

weapons = \
    {
        'messer_sword': {'parent': 'bettercombat:cutlass'},
        'sabre': {'parent': 'bettercombat:cutlass'},
        'falchion': {'parent': 'bettercombat:cutlass'},
        'scimitar': {'parent': 'bettercombat:cutlass',
                     'attributes':
                         {
                             'two_handed': True,
                         }
                     },
        'german_greatsword':
            {
                'parent': 'bettercombat:claymore',
                'attributes':
                    {
                        'attack_range': 2.9,
                    }
            },
        'executioners_sword':
            {
                'parent': 'bettercombat:claymore',
                'attributes':
                    {
                        'attack_range': 2.8,
                    }
            },
        'longsword':
            {
                'parent': 'bettercombat:claymore',
                'attributes':
                    {
                        'attack_range': 2.6,
                    }
            },
        'arming_sword_type_xiii': {'parent': 'bettercombat:sword'},
        'arming_sword_type_xiv': {'parent': 'bettercombat:sword'},
        'arming_sword_type_xv': {'parent': 'bettercombat:sword'},
        'rapier': {'parent': 'bettercombat:rapier'},
        'sidesword':
            {
                'parent': 'bettercombat:rapier',
                'attributes':
                    {
                        'attack_range': 2.6,
                    }
            },
        'dagger': {'parent': 'bettercombat:dagger'},
        'sickle': {'parent': 'bettercombat:sickle'},
        'battleaxe': {'parent': 'bettercombat:axe'},
        'partisan':
            {
                'parent': 'bettercombat:spear',
                'attributes':
                    {
                        'attack_range': 3.5
                    }
            },
        'boar_spear':
            {
                'parent': 'bettercombat:spear',
                'attributes':
                    {
                        'attack_range': 3.4
                    }
            },
        'glaive': {'parent': 'bettercombat:glaive'},
        'voulge': {'parent': 'bettercombat:glaive'},
        'goedendag':
            {
                'parent': 'bettercombat:spear',
                'attributes':
                    {
                        'attack_range': 3.3,
                    }
            },
        'lance':
            {
                'parent': 'bettercombat:lance',
                'attributes':
                    {
                        'attack_range': 4.0,
                    }
            },
        'scythe': {'parent': 'bettercombat:scythe'},
        'billhook':
            {
                'parent': 'bettercombat:halberd',
                'attributes':
                    {
                        'attack_range': 3.3,
                    }
            },
        'french_halberd': {'parent': 'bettercombat:halberd'},
        'english_poleaxe': {'parent': 'bettercombat:halberd'},
        'fauchard': {'parent': 'bettercombat:halberd'},
        'italian_poleaxe': {'parent': 'bettercombat:halberd'},
        'swiss_halberd':
            {
                'parent': 'bettercombat:halberd',
                'attributes':
                    {
                        'attack_range': 3.4,
                    }
            },
        'francisca_axe': {'parent': 'bettercombat:axe'},
        'war_axe': {'parent': 'bettercombat:axe'},
        'war_hammer': {'parent': 'bettercombat:double_axe'},
        'bollock_dagger': {'parent': 'bettercombat:dagger'},
        'rondel_dagger': {'parent': 'bettercombat:dagger'},
        'broadaxe':
            {
                'parent': 'bettercombat:halberd',
                'attributes':
                    {
                        'attack_range': 3.2,
                    }
            },
        'daneaxe':
            {
                'parent': 'bettercombat:halberd',
                'attributes':
                    {
                        'attack_range': 3.3,
                    }
            },
        'gallowglass_axe':
            {
                'parent': 'bettercombat:halberd',
                'attributes':
                    {
                        'attack_range': 3.3,
                    }
            },
        'cutlass': {'parent': 'bettercombat:cutlass'},
        'feder': {'parent': 'bettercombat:claymore'},
        'grand_falchion': {'parent': 'bettercombat:claymore'},
        'long_seax': {'parent': 'bettercombat:claymore'},
        'training_sword': {'parent': 'bettercombat:claymore'},
        'short_spear':
            {
                'parent': 'bettercombat:spear',
                'attributes':
                    {
                        'attack_range': 3.4
                    }
            },
        'welsh_guisarme': {'parent': 'bettercombat:glaive'},
        'rich_saxon_sword': {'parent': 'bettercombat:sword'},
        'saxon_sword': {'parent': 'bettercombat:sword'},
        'short_seax': {'parent': 'bettercombat:sword'},
    }

result_dir = 'new_files'


def main():
    for material in materials:
        for weapon_name, data in weapons.items():
            with open(result_dir + '/' + material + '_' + weapon_name + '.json', 'w') as f:
                json.dump(data, f, indent=4)


if __name__ == '__main__':
    main()
