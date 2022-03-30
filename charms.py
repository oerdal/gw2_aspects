import json

armor_json = []

with open('armor.json', 'r') as f:
    armors = json.load(f)

with open('runes.json', 'r') as f:
    runes = json.load(f)

if not(armors and runes):
    print('exiting program')
    exit

charmor = []

for armor in armors:
    rune_id = str(armor['details']['suffix_item_id'])
    rune = runes[rune_id]
    if rune:
        payload = {}
        payload['armor_name'] = armor['name']
        payload['armor_id'] = armor['id']
        payload['armor_type'] = armor['details']['type']
        payload['armor_weight'] = armor['details']['weight_class']
        payload['rune_name'] = rune['name']
        payload['rune_id'] = rune_id
        payload['rune_element'] = rune['element']
        charmor.append(payload)

filename = 'charms.json'
print(f'writing to file {filename}')

with open(filename, 'w') as f:
    json.dump(charmor, f)

print('finished writing to file')