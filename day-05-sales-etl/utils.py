def summary(data):
    summarydata = {}
    summarydata['total_record'] = 0
    summarydata['total_revenue'] = 0
    
    for row in data:
        summarydata['total_record'] += 1
        summarydata['total_revenue'] += row['revenue']

    summarydata['average_revenue'] = summarydata['total_revenue']/summarydata['total_record']

    return summarydata
