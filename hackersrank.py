meal_cost = 100
tip_percent = 15
tax_percent = 8

def TotalCost():
    meal_cost = 100
    tip_percent = 15
    tax_percent = 8
    tip = tip_percent/100 * meal_cost
    tax = tax_percent/100 * meal_cost
    Total_cost = meal_cost + tip + tax
    result = round(Total_cost)
    print(result)
