# Creating Modules
from SalesForModules import calc_shipping, calc_tax
# or
# import SalesForModules

calc_shipping()
calc_tax()

# Compiled Python Flies
import SalesForModules
import sys

print(sys.path)

from ecommerce import SalesForModules
