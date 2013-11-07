# Tip calculator
# Hard-Code
#meal_cost = 20.00
#tax_rate = .15 #15%
#tip_rate = .15

def tip_calculator():
    meal_cost = float(raw_input("Please enter your pre tax and tip meal cost: "))
    tax_rate = float(raw_input("Please provide your tax rate as a decimal: "))
    tip_rate = float(raw_input("Please provide your desired tip rate as a decimal: "))
    print "The base cost of your meal was $%.2f" % meal_cost
    tax = meal_cost*tax_rate
    print "You need to pay $%.2f" % tax
    tip = tip_rate*(meal_cost+tax)
    print "Tipping at a rate of %d%%, you should leave $%.2f for a tip." % (tip_rate*100, tip)
    total = meal_cost+tax+tip
    print "The grand total of your meal is $%.2f." % total

tip_calculator()