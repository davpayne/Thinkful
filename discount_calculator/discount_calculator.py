class DiscountCalculator(object):
	def calculate(self, total, discount_amount, discount_type):
	    if discount_type == 'percent':
	      if discount_amount > 100:
	      	raise ValueError("Percentage discount cannot exceed 100%")
	      percentage_discount = discount_amount / 100.
	      discount = total * percentage_discount
	    elif discount_type == 'absolute':
	      if discount_amount > total:
	      	raise ValueError("Discount cannot exceed order total.")
	      discount = discount_amount
	    else:
	      raise ValueError("Invalid discount type: Options are 'percent' and 'absolute'.")
	    return discount
