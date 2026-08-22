import transform
import extract
import load
import utils
import report


datacsv = extract.extract_sales('data/sales.csv')
if datacsv:
    cleandata = transform.clean_sales(datacsv)
    load.export_sales(cleandata)
    summarydata = utils.summary(cleandata)
    report.summary_report(summarydata)

