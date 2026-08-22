def calculate_total_revenue(data):
    total_revenue = 0
    for row in data:
        total_revenue += row['quantity']*row['price']
    return total_revenue

def test_total_revenue():
    data = [
        {"quantity": 10, "price": 20},
        {"quantity": 5, "price": 100},
    ]

    assert calculate_total_revenue(data) == 700

test_total_revenue()