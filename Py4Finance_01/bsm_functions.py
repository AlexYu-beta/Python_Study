"""
this python file includes some basic functions of Black-Scholes-Merton formulas
"""
def bsm_call_value(S0,K,T,r,sigma):
    '''
    Valuation of European call option in BSM model
    :param S0: initial stock level
    :param K: strike price
    :param T: maturity date
    :param r: constant risk-free short rate
    :param sigma: volatility factor in diffusion term
    :return: the call value
    '''

    from math import log,sqrt,exp
    from scipy import stats

    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = (log(S0 / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    value = (S0 * stats.norm.cdf(d1,0.0,1.0)) - K * exp(-r * T) * stats.norm.cdf(d2,0.0,1.0)
    return value

def bsm_vega(S0,K,T,r,sigma):
    '''
    calculating Vega of European option in BSM model
    :param S0: initial stock level
    :param K: strike price
    :param T: maturity date
    :param r: constant risk-free short rate
    :param sigma: volatility factor in diffusion term
    :return: Vega
    '''

    from math import log,sqrt
    from scipy import stats

    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    vega = S0 * stats.norm.cdf(d1,0.0,1.0) * sqrt(T)
    return vega

def bsm_call_imp_vol(S0,K,T,r,C0,sigma_est, it=100):
    '''
    implied volatility of European call option in BSM model
    :param S0: initial stock level
    :param K: strike price
    :param T: maturity date
    :param r: constant risk-free short rate
    :param C0:
    :param sigma_est: estimate of impl. volatility
    :param it: number of iterations
    :return:
    '''

    for i in range(it):
        sigma_est -= ((bsm_call_value(S0,K,T,r,sigma_est)-C0)/bsm_vega(S0,K,T,r,sigma_est))
    return sigma_est
