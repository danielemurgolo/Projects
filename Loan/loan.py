import numpy as np
import numpy_financial as npf

loan = 60_000
rate = 0.04
years = 15
per = np.arange(years * 12) + 1

ipmt = -npf.ipmt(rate / 12, per, years * 12, loan)
ppmt = -npf.ppmt(rate / 12, per, years * 12, loan)

print(ipmt)
