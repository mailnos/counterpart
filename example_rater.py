"""

title: counterpart case study

author: liam watson

date: 07/16/2023

version: 1

"""

 

from operator import concat

import pandas as pd

import numpy as np

from scipy.interpolate import interp1d

 

def rater(json_input):

 

    asset_size = [ 1, 1000000, 2500000, 5000000, 10000000, 15000000, 20000000, 25000000, 50000000, 75000000, 100000000, 250000000]

    base_rate = [ 1065, 1819, 3966, 3619, 4291, 4905, 5120, 5499, 6279, 6966, 7156, 8380]

 

    limit = [ 0, 1000, 2500, 5000, 7500, 10000, 15000, 20000, 25000, 35000, 50000, 75000, 100000, 125000,

    150000, 175000, 200000, 225000, 250000, 275000, 300000, 325000, 350000, 375000, 400000, 425000, 450000,

    475000, 500000, 525000, 550000, 575000, 600000, 625000, 650000, 675000, 700000, 725000, 750000, 775000,

    800000, 825000, 850000, 875000, 900000, 925000, 950000, 975000, 1000000, 2000000, 2500000, 3000000, 4000000, 5000000 ]

 

    factor = [ -0.76, -0.6, -0.51, -0.406, -0.303, -0.231, -0.128, -0.064, 0, 0.105, 0.175, 0.277, 0.35, 0.406,

    0.452, 0.491, 0.525, 0.555, 0.581, 0.605, 0.627, 0.648, 0.666, 0.684, 0.7, 0.715, 0.73, 0.743, 0.756, 0.807,

    0.819, 0.831, 0.842, 0.853, 0.864, 0.874, 0.883, 0.893, 0.902, 0.91, 0.919, 0.927, 0.935, 0.943, 0.95, 0.957,

    0.964, 0.971, 1, 1.415,  1.526, 1.637, 1.82, 1.986]

 

    industry_dict = {"Hazard Group 1": 1, "Hazard Group 2": 1.25, "Hazard Group 3": 1.5}

 

    #error handling    

    if  json_input["Asset Size"] < 1:

        return "Please Enter Asset Size > $1"

    elif json_input["Asset Size"] >  250000000:

        return "Please reach out to actuary for large account pricing"

 

    if  json_input["Limit"] < 1:

        return "Please Enter Limit > $1"

    elif json_input["Limit"] >  5000000:

        return "Please reach out to actuary for large account pricing"

 

    if  json_input["Retention"] < 0:

        return  "Please Enter Limit > $1"

    elif json_input["Retention"] >  5000000:

        return  "Please reach out to actuary for high excess account pricing"

 

    base_function = interp1d(asset_size, base_rate, kind = "linear", bounds_error= False, fill_value= 0)

    lim_function = interp1d(limit, factor, kind = "linear", bounds_error= False, fill_value= 0)

 

    rate_f = base_function(json_input["Asset Size"])

    limit_f = lim_function(json_input["Limit"])

    retention_f = lim_function(json_input["Retention"])

    industry_f = industry_dict[json_input["Industry"]]

 

    result = round(rate_f * (limit_f - retention_f) * industry_f * 1.7,0)

 

    if  json_input["Asset Size"] < json_input["Limit"] :

        result = "The price is: "+ str(result) + ", however please note that your limit is greater than your asset size"

 

    return result

 
