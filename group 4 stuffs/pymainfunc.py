# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 19:42:55 2021

@author: JH Business
"""
from decimal import Decimal

# link clicked signal to action function - 
# add below line to Class init 
#   self.calc_tax_button.clicked.connect(self.calculate_tax)
# add below function to Class
def calculate_tax(self):
    price = Decimal(self.price_box.text())
    tax = Decimal(self.tax_rate.value())
    total_price = price  + ((tax / 100) * price)
    total_price_string = "The total price with tax is: {:.2f}".format(total_price)
    self.results_output.setText(total_price_string)