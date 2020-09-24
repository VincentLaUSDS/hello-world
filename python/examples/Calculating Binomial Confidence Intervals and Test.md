Benchmarking Results of Python against R

R:
```
> x = 15
> n=20
> binom.test(x=x, n=n,p=0.5, alternative='two.sided', conf.level=0.95)

	Exact binomial test

data:  x and n
number of successes = 15, number of trials = 20, p-value = 0.04139
alternative hypothesis: true probability of success is not equal to 0.5
95 percent confidence interval:
 0.5089541 0.9134285
sample estimates:
probability of success 
                  0.75 
```

Python
```
from scipy.stats import binom_test
from statsmodels.stats.proportion import proportion_confint

x = 15
n = 20
>>> binom_test(x=x, n=n, p=0.5)
0.04138946533203125

# Beta is Copper-Pearson Interval which is what R uses by default
proportion_confint(count=x, nobs=n, method='beta')
(0.5089541282920425, 0.9134285308985655)
```

Error Bars in Matplotlib: https://stackoverflow.com/questions/44603615/plot-95-confidence-interval-errorbar-python-pandas-dataframes

https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.errorbar.html
