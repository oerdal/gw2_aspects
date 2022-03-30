from itertools import zip_longest

def batch_ids(endpoint, ids, batch_size=100):
    args = [iter(ids)] * batch_size
    id_batches = zip_longest(*args, fillvalue=None)
    batched_endpoints = []
    for batch in id_batches:
        batched_endpoint = f'{endpoint}?ids={",".join([str(item_id) for item_id in batch if item_id])}'
        batched_endpoints.append(batched_endpoint)
    return batched_endpoints


def fmt_price(price):
    out = '-' if price < 0 else ''
    price = round(abs(price))
    c = price % 100
    price //= 100
    s = price % 100
    price //= 100
    g = price
    out += f'{g}g {s}s {c}c'
    return out


MAT_DATA = {'Heavy' : {'Quantity' : [1.35, 2.45], 'Drop_ID': '19700'},
            'Medium' : {'Quantity' : [3.1, 2.1], 'Drop_ID': '19729'},
            'Light' : {'Quantity' : [3.1, 2.1], 'Drop_ID': '19748'}}
'''
Get the expected crafting material value of a salvage at post-tax market price
based on the given armor weight and whether or not it's a coat.
@weight string      - one of ['Light', Medium', 'Heavy']
@is_coat boolean    - true if the armor is a coat, false otherwise
@price_data         - json of datawars pricing information to use for mat value
@instant_sell       - true if mats will be instant sold, false otherwise
                    - false by default
'''
def get_mat_value(weight, is_coat, price_data, instant_sell=False):
    mat_quantity = MAT_DATA[weight]['Quantity'][is_coat]
    mat_id = MAT_DATA[weight]['Drop_ID']
    mat_pricing = price_data[mat_id]
    mat_value = mat_quantity * mat_pricing['buy_price'] if instant_sell else mat_quantity * mat_pricing['sell_price']
    return mat_value


##
# Heavy Coat = 2.45 Ore
# Heavy other Armor = 1.35 Ore
# Medium Coat = 3.1 Leather sections
# Medium other Armor = 2.1 Leather sections
# Light Coat = 3.1 Cloth scraps
# Light other Armor = 2.1 Cloth scraps




