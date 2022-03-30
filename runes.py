import json

runes = {"Charm of Potence": ["Superior Rune of Balthazar","Superior Rune of Durability","Superior Rune of Hoelbrak","Superior Rune of Leadership","Superior Rune of Melandru","Superior Rune of Radiance","Superior Rune of Strength","Superior Rune of Svanir","Superior Rune of the Baelfire","Superior Rune of the Berserker","Superior Rune of the Brawler","Superior Rune of the Cavalier","Superior Rune of the Citadel","Superior Rune of the Defender","Superior Rune of the Dolyak","Superior Rune of the Dragonhunter","Superior Rune of the Earth","Superior Rune of the Fire","Superior Rune of the Firebrand","Superior Rune of the Flame Legion","Superior Rune of the Guardian","Superior Rune of the Herald","Superior Rune of the Ogre","Superior Rune of the Renegade","Superior Rune of the Revenant","Superior Rune of the Scrapper","Superior Rune of the Spellbreaker","Superior Rune of the Sunless","Superior Rune of the Trooper","Superior Rune of the Warrior","Superior Rune of the Wurm","Superior Rune of Tormenting","Superior Rune of Vampirism"],
         "Charm of Brilliance": ["Superior Rune of Altruism","Superior Rune of Divinity","Superior Rune of Dwayna","Superior Rune of Exuberance","Superior Rune of Fireworks","Superior Rune of Grenth","Superior Rune of Lyssa","Superior Rune of Mercy","Superior Rune of Perplexity","Superior Rune of Rata Sum","Superior Rune of Snowfall","Superior Rune of Speed","Superior Rune of Surging","Superior Rune of the Afflicted","Superior Rune of the Air","Superior Rune of the Chronomancer","Superior Rune of the Eagle","Superior Rune of the Elementalist","Superior Rune of the Flock","Superior Rune of the Golemancer","Superior Rune of the Krait","Superior Rune of the Lich","Superior Rune of the Mesmer","Superior Rune of the Mirage","Superior Rune of the Monk","Superior Rune of the Necromancer","Superior Rune of the Privateer","Superior Rune of the Reaper","Superior Rune of the Scholar","Superior Rune of the Scourge","Superior Rune of the Tempest","Superior Rune of the Undead","Superior Rune of the Weaver"],
         "Charm of Skill": ["Superior Rune of Antitoxin","Superior Rune of Evasion","Superior Rune of Infiltration","Superior Rune of Nature's Bounty","Superior Rune of Orr","Superior Rune of Rage","Superior Rune of Resistance","Superior Rune of Sanctuary","Superior Rune of Scavenging","Superior Rune of the Adventurer","Superior Rune of the Aristocracy","Superior Rune of the Centaur","Superior Rune of the Daredevil","Superior Rune of the Deadeye","Superior Rune of the Druid","Superior Rune of the Engineer","Superior Rune of the Forgeman","Superior Rune of the Grove","Superior Rune of the Holosmith","Superior Rune of the Ice","Superior Rune of the Mad King","Superior Rune of the Nightmare","Superior Rune of the Pack","Superior Rune of the Ranger","Superior Rune of the Rebirth","Superior Rune of the Soulbeast","Superior Rune of the Stars","Superior Rune of the Thief","Superior Rune of the Trapper","Superior Rune of the Traveler","Superior Rune of the Water","Superior Rune of the Zephyrite","Superior Rune of Thorns"]}

# for e, rs in runes.items():
#     for r in rs:
#         print((r, e))
all_runes = {r: e for e, rs in runes.items() for r in rs}

rune_json = {}

with open('items.json', 'r') as f:
    items = json.load(f)

for item in items:
    if item['type'] == 'UpgradeComponent' and item['name'] in all_runes:
        rune = item.copy()
        rune['element'] = all_runes[rune['name']]
        rune_json[rune['id']] = rune

filename = 'runes.json'
print(f'writing to file {filename}')

with open(filename, 'w') as f:
    json.dump(rune_json, f)

print('finished writing to file')