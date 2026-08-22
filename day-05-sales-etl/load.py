import csv
import logger
from datetime import datetime

def export_sales(data):
    headers = ['date','product', 'quantity', 'price','revenue']
    now = datetime.now()
    date_str = now.strftime("%d%m%y")
    filename = f"output/clean_sales_{date_str}.csv"

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        # สร้าง DictWriter object โดยต้องส่งหัวคอลัมน์ไปด้วย
        writer = csv.DictWriter(file, fieldnames=headers) 
        writer.writeheader()
        writer.writerows(data) 

    logger.log("Load Finished")
