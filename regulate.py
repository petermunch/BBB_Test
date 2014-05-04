__author__ = 'munchp'
'''
Regulation of the temperatures
'''

import time
from main import cookerSettings, recipeSettings
# Variables
check_temp = False
pit_temp = 110.56
grill_temp = 100.34
hysterese = 5

while check_temp:
    if grill_temp < recipeSettings.grill_target - hysterese:
        open_vent = True
    elif grill_temp > recipeSettings.grill_target + hysterese:
       close_vent = True
