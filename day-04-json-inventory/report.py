import json

def new_inventory_summary(filename,jsondata,numproduct,suminventory):
    data = {}
    tmp = {}
    tmp['total_products'] = numproduct
    tmp['total_inventory_value'] = suminventory
    data['summary'] = tmp
    data['products'] = jsondata

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        json.dump(data, file)