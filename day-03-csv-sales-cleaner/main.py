import csv

numofrows = 0
validdata = 0
totalRevenue = 0
cleanData= []
invalidData= []
allproduct = {}
with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    
    
    for row in reader:
        numofrows += 1

        if(row['quantity'] == "" or row['price'] == "" ):
            invalidData.append(row)
            continue
        
        validdata += 1

        row['revenue'] = int(row['quantity']) * int(row['price'])

        if row['product'] not in allproduct:
            allproduct[row['product']]  = 0

        allproduct[row['product']] +=  row['revenue']

        cleanData.append(row)

        totalRevenue += int(row['quantity']) * int(row['price'])


sorted_a = {key: value for key, value in sorted(allproduct.items(), key=lambda item: item[1], reverse=True)}

for key, value in sorted_a.items():
        print(f"{key}")
        print(f"Revenue :  {value:,.0f}")
        print("")
        break


print(f"Total Records : {numofrows}")
print(f"Valid Records : {validdata}")
print(f"Invalid Records : {numofrows - validdata}")
print("Total Revenue")
print(f"{totalRevenue:,.0f}")


    
sorted_data = sorted(cleanData, key=lambda x: x['revenue'], reverse=True)

headers = ['product', 'quantity', 'price','revenue']

with open('output/clean_sales.csv', mode='w', newline='', encoding='utf-8') as file:
    # สร้าง DictWriter object โดยต้องส่งหัวคอลัมน์ไปด้วย
    writer = csv.DictWriter(file, fieldnames=headers) 
    writer.writeheader()
    writer.writerows(sorted_data) 

inheaders = ['product', 'quantity', 'price']

with open('output/invalid_sales.csv', mode='w', newline='', encoding='utf-8') as file:
    # สร้าง DictWriter object โดยต้องส่งหัวคอลัมน์ไปด้วย
    writer = csv.DictWriter(file, fieldnames=inheaders) 
    writer.writeheader()
    writer.writerows(invalidData) 
        



