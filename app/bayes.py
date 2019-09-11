from scipy.stats import beta
import matplotlib.pyplot as plt

#non-informative prior
a=1
b=1


x = np.linspace(beta.ppf(0.01, a, b),beta.ppf(0.99, a, b), 100)
>>> ax.plot(x, beta.pdf(x, a, b),
...          'r-', lw=5, alpha=0.6, label='beta pdf')
