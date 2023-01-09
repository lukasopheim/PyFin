# this program implements the black-scholes pricing formula

import numpy as np
from scipy.stats import norm
#params

#interestRate
r = 0.09
#underlying
s = 382.75
#strikePrice
K = 383
#time in days unitl the expiration date over 365 since time is in years
T = 7/365
#volatility
sigma = 0.1722

def blackScholes(r, s, K, T, sigma, type="C"):
    "Calculate the BS option price for a call or put"
    d1 = (np.log(s/K)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1-sigma*np.sqrt(T)
    try:
        if type == "C":
            price = s*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "p":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - s*norm.cdf(-d1, 0, 1)
        return price
    except:
        print("please confirm all option parameters above")


print("Option Price is:", round(blackScholes(r, s, K, T, sigma, type="C"), 2) )






