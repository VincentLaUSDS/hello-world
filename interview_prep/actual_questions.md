# SQL

## Next Insurance (2019-11-26)
Say you have a table where each row is employee, salary, and department. How would you construct a query to find top earning employee id for each department? High level (actual sql was not required)

```
Basically the idea would be to use a window function to rank each employee by department ordered by salary.
Can then filter to where the rank is above X number
```

# ML

## Next Insurance (2019-11-26)
Say you have bivariate data, y and X. I tell you that the way the data is distributed, the true model fits a piecewise linear function where there is a threshold, T below which there is one line to fit, above which there is another line to fit. How do you find the optimal value of T?

```
In this case, assume we use OLS to fit. This minimizes the sum of least squares. First, we define a new dummy variable D and fit the following model

y = b0 + b1D + b2X + b3X*D

this model characterizes the piecewise linear function. I think this is equivalent to 

y = b0 + b1X + e where x < T
y = a0 + a1X + e where x >= T
?

In any case, you can calculate the MSE for both. Then to find the optimal value of D, we can iterate through the domain of X and test each point. This is O(n) since we need to test all cases between each value of x to split the dataset.

However, note that on runtime this runs at mn^2, or in this case n^2 since m = 2.

We can get more efficient by using a binary search. So binary search can be used whenever the dataset is ordered. Specifically, the intuition behind binary search is that it can be used whenever we can throw away one half of the search space every time.

So in this case, given that we have the assumption that the true distribution is a piecewise linear function, we can compute the midpoint and fit the model.

Then we can compute the midpoint to the left and to the right. Because we know that the true distribution is a piecewise linear function we know two things
1. One side has to be better than the other. It's not possible for both sides to be worse or both sides to be better (I think)
2. Once we pick one side, it's not possible for the other side to be better. That is, no subset of the worse side can yield better results than picking the other side. The performance is monotonically improving

Thus, the solution is that we compute midpoint, calculate MSE. Then compute MSE of left side, and right side and pick the one that is better. Continue doing this until you've searched the space. This should run in o(nlog n). log(n) because of the search, n because of the cost to compute OLS weights. 
```

# Programming

## Komodo Health (2019-11-19)

Write a program to find the square root of a number
