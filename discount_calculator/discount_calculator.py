class DiscountCalculator(object):
  def calculate(self, total, discount_amount, discount_type):
    percent_discount = discount_amount/100.
    discount = total * percent_discount
    return discount
