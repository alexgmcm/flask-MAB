from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np




def plot_distributions(cat_dict):

    #non-informative prior
    a=1
    b=1


    x = np.linspace(0,1, 1000)
    colors = ['r','b','k','g']
    for cat,color in zip(cat_dict.values(),colors):
        plt.plot(x, beta.pdf(x, a + cat.score, b + cat.fails),color, lw=3, alpha=1, label=cat.name)

    plt.title(r'Distributions of $\theta$')
    plt.ylabel(r'$P(\theta|x)$')
    plt.xlabel(r'$\theta$')
    plt.legend()

    plt.savefig("./app/static/betaplot.png")
    plt.close()
