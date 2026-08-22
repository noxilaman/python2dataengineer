import logger
def clean_sales(datacsv):   
    cleanData= []
    for row in datacsv:

        if(row['quantity'] == "" or row['price'] == "" ):
            continue
        
        row['revenue'] = int(row['quantity']) * int(row['price'])
        row['quantity'] = int(row['quantity'])
        row['price'] = int(row['price'])
    
        cleanData.append(row)

    logger.log("Transform Finished")

    return cleanData