# Tip calculator
# Hard-Code
#meal_cost = 20.00
#tax_rate = .15 #15%
#tip_rate = .15
#from sys import argv
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--first", dest="meal_cost", help="the meal cost", type = "float")
parser.add_option("-s", "--second", dest="tax_rate", help="the tax rate", type = "float")
parser.add_option("-t", "--third", dest="tip_rate", help="the tip rate", type = "float", default =".15")

(options, args) = parser.parse_args()
if not(options.meal_cost and options.tax_rate):
	parser.error("You need to supply a value for meal_cost and tax_rate")

def tip_calculator():
    #argv
    #meal_cost = float(argv[1])
    #tax_rate = float(argv[2])
    #tip_rate = float(argv[3])
    #user_inputs
    #meal_cost = float(raw_input("Please enter your pre tax and tip meal cost: "))
    #tax_rate = float(raw_input("Please provide your tax rate as a decimal: "))
    #tip_rate = float(raw_input("Please provide your desired tip rate as a decimal: "))
    print "The base cost of your meal was $%.2f" % options.meal_cost
    tax = options.meal_cost*options.tax_rate
    print "You need to pay $%.2f" % tax
    tip = options.tip_rate*(options.meal_cost+tax)
    print "Tipping at a rate of %d%%, you should leave $%.2f for a tip." % (options.tip_rate*100, tip)
    total = options.meal_cost+tax+tip
    print "The grand total of your meal is $%.2f." % total

tip_calculator()