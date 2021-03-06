import json
import random

from util import fmt_price, get_mat_value


ECTO_RATE = 1.27
ECTO_ID = '19721'
CHARM_RATE = 0.09

with open('aspects.json', 'r') as f:
    items = json.load(f)

with open('dw_items.json', 'r') as f:
    dw = json.load(f)
    ecto = dw[ECTO_ID]

ECTO_PRICE = ecto['sell_price']


def salvage_profit(armor, price_data, instant_buy=False):
    # armor_is_coat T if coat, F otherwise
    armor_is_coat = armor['armor_type'] == 'Coat'
    armor_weight = armor['armor_weight']

    crafting_mat_value = get_mat_value(armor_weight, armor_is_coat, price_data)
    crafting_mat_value += ECTO_PRICE*ECTO_RATE
    
    armor_cost = armor['armor_sell_price'] if instant_buy else armor['armor_buy_price']
    cost_per_charm = (crafting_mat_value - armor_cost) * (1/CHARM_RATE)

    # cost of the charm through salvaging + cost of buying charm
    profit = cost_per_charm + armor['charm_buy_price']

    return profit


def simulate_salvage(armor, price_data, instant_buy=False):
    # armor_is_coat T if coat, F otherwise
    armor_is_coat = armor['armor_type'] == 'Coat'
    armor_weight = armor['armor_weight']

    # get the estimated number of drops
    crafting_mat_value = get_mat_value(armor_weight, armor_is_coat, price_data)
    crafting_mat_value += ECTO_PRICE*ECTO_RATE
    charm_salvaged = random.choices([True, False], weights=[9, 91], k=1)[0]

    armor_cost = armor['armor_sell_price'] if instant_buy else armor['armor_buy_price']

    return (charm_salvaged, fmt_price(crafting_mat_value), fmt_price(armor_cost))


to_salvage = {}

for item in items:
    p = salvage_profit(item, dw, instant_buy=False)
    if p > 0:
        fp = fmt_price(p)
        print(f"{item['armor_name']}: {fp}")
        to_salvage[item['armor_id']] = { 'name' : item['armor_name'], 'charm' : item['rune_element'], 'profit' : fp }

filename = 'salvaging.json'
print(f'writing to file {filename}')

with open(filename, 'w') as f:
    json.dump(to_salvage, f)

print('finished writing to file')