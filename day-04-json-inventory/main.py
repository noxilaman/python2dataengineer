import json
import transformer
import reader
import report

totalinventory = 0
numofproduct = 0
inventory = reader.readdata("data/inventory.json")

for row in inventory:

    print(f"{row['product']} : {row['stock']*row['price']}")
    numofproduct += 1
    totalinventory += row['stock']*row['price']

print(totalinventory) 

transformer.inventorybelow(50,inventory)
transformer.groupbycat(inventory)
newdata = transformer.update_inventory_value('data/inventory.json',inventory)
report.new_inventory_summary('output/inventory_report.json',newdata,numofproduct,totalinventory)

sorted_data = sorted(newdata, key=lambda x: x['inventory_value'], reverse=True)

print(sorted_data[0]) 

