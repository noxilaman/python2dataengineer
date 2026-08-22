import json

def inventorybelow(rate,jsondata):
    for row in jsondata:
        if(row['stock'] < rate):
            print(row['product'])

def groupbycat(jsondata):
    groupbycat = {}
    for row in jsondata:
        tmp = {}
        if row['category'] not in groupbycat:
            tmp['Products'] = 1
            tmp['Stock'] = row['stock']
            tmp['Value'] = row['stock']*row['price']
            groupbycat[row['category']]  = tmp
        else:
            tmp = groupbycat[row['category']]
            tmp['Products'] += 1
            tmp['Stock'] += row['stock']
            tmp['Value'] += row['stock']*row['price']
            groupbycat[row['category']]  = tmp
        
    for key, value in groupbycat.items():
        print(key)
        print(f"Products : {value['Products']}")
        print(f"Stock : {value['Stock']}")
        print(f"Value : {value['Value']}")

def update_inventory_value(filename,jsondata):

    for row in jsondata:
        row['inventory_value'] = row['stock']*row['price']    

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        json.dump(jsondata, file)

    return jsondata


