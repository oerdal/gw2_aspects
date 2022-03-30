import json

CHARMS = ['Charm of Brilliance', 'Charm of Potence', 'Charm of Skill']

def match_data():
    armor_json = []

    with open('dw_items.json', 'r') as f:
        dw_items = json.load(f)

    with open('charms.json', 'r') as f:
        charms = json.load(f)

    if not(dw_items and charms):
        print('exiting program')
        exit

    aspects = []

    dw_charms = {c['name']: c for c in dw_items.values() if c['name'] in CHARMS}

    for item in charms:
        # attach armor cost
        a_id = str(item['armor_id'])
        if a_id in dw_items:
            aspect = item.copy()
            for k, v in dw_items[a_id].items():
                aspect[f'armor_{k}'] = v
        
            # attach charm value
            dw_charm = dw_charms[item['rune_element']].items()
            for k, v in dw_charm:
                aspect[f'charm_{k}'] = v

            aspects.append(aspect)

    filename = 'aspects.json'
    print(f'writing to file {filename}')

    with open(filename, 'w') as f:
        json.dump(aspects, f)

    print('finished writing to file')


def main():
    match_data()


if __name__ == '__main__':
    main()