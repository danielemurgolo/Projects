import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

loan = 60_000
rate = 0.04
years = 15
per = np.arange(years * 12) + 1

ipmt = -npf.ipmt(rate / 12, per, years * 12, loan)
ppmt = -npf.ppmt(rate / 12, per, years * 12, loan)

plt.plot(per, ipmt, label="interests")
plt.plot(per, ppmt, label="principal")
plt.plot(per, np.cumsum(ipmt), label="cumulative interests")
plt.plot(per, np.cumsum(ppmt), label="cumulative principal")

plt.legend()
plt.show()

principal = loan - np.cumsum(ppmt)

plt.plot(per, principal, label="principal")
plt.plot(per, np.cumsum(ppmt), label="cumulative principal")
plt.legend()
plt.show()
