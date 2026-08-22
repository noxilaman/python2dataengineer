import csv
import logger
def extract_sales(file_path):
    try:
        with open(file_path, newline="") as file:
            reader = csv.DictReader(file)
            datacsv = list(reader) 
            logger.log("Extract Finished")
            return datacsv
    except FileNotFoundError as e:
        print(f"File not found") 
        logger.log("Extract Fail")
