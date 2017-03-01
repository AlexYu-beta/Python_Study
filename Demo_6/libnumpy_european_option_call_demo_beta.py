from numpy import *
"""
an simple example of Monto Carlo valuation of European call option in Black-Scholes-Merton Model
"""
S0 = 100        #initial stock index level
K = 105         #strike price of the European call option
T = 1.0         #time to maturity
r = 0.05        #<CONSTANT>riskless short rate
sigma = 0.2     #<CONSTANT>volatility
I = 100000      #number of random numbers from the standard normal distribution
z = random.standard_normal(I)           #generate the pseudo-random variant from the standard normal distribution
ST = S0 * exp((r - 0.5 * sigma ** 2) * T + sigma *sqrt(T) * z)      #Black-Scholes-Merton formula
HT = maximum(ST - K,0)
C0 = exp(-r * T) * sum(HT) / I          #Monte Carlo Estimator
print "value of the European Call Option %5.3f" % C0