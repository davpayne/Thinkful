# Tip calculator
from sys import argv

def calculate_rate(base, percentage):
    return base * percentage
 
def calculate_meal_costs(meal_base, tax_rate, tip_rate):
    """
    Calculates dollar amounts for tax, tip, and total meal cost
    """
    tax_value = calculate_rate(meal_base, tax_rate)
    meal_with_tax = tax_value + meal_base
    tip_value = calculate_rate(meal_with_tax, tip_rate)
    total = meal_with_tax + tip_value
    meal_info = dict(meal_base=meal_base,
                    meal_with_tax=meal_with_tax,
                    tip_value=tip_value,
                    tax_value=tax_value,
                    total = total)
    return meal_info

def main():
    """
    Takes in the cost of the meal, tax rate, and tip rate to produce the meal
    costs. Prompts the user for valid inputs until given appropriate ones.
    """
    try:
        meal_cost = float(argv[1])
        tax_rate = float(argv[2])
        tip_rate = float(argv[3])
    except (ValueError, IndexError):
        while True:
            try:
                print "You must provide a number for all inputs"
                meal_cost = float(raw_input("Meal Cost: $"))
                tax_rate = float(raw_input("Tax rate: "))
                tip_rate = float(raw_input("Tip rate: "))
                break
            except ValueError:
                pass
    
    meal_info = calculate_meal_costs(meal_cost, tax_rate, tip_rate)
    print "The cost of your meal with tax is $%.2f" % meal_info['meal_with_tax']
    print "Tipping at a rate of %d%%, you should leave $%.2f for a tip." % (tip_rate*100, meal_info['tip_value'])
    print "The grand total for your meal is $%.2f." % meal_info['total']
    if tip_rate < .15:
        print "Only tipping %d%% tip? Little Cheap, eh?" % (tip_rate*100)
    
if __name__ == '__main__':
    main()