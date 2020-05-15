# SQL

## Next Insurance (2019-11-26)
Say you have a table where each row is employee, salary, and department. How would you construct a query to find top earning employee id for each department? High level (actual sql was not required)

```
Basically the idea would be to use a window function to rank each employee by department ordered by salary.
Can then filter to where the rank is above X number
```

# ML and Statistical Modeling

## Komodo Health (2019-11-19; Onsite)
Let's say you have claims data with patient_id, and a bunch of demographic, diagnosis, procedure, and medication information about the patient. How would you go about predicting whether the patient has a certain disease or not?

```
EDA
1. Check for duplicates
2. Check for missing data
3. Check for class imbalance
4. Check correlations between features

Feature Engineering
1. One-hot encode or label encode categorical variables

Modeling
1. Logistic Regression or Random Forest are usually good places to start. Tradeoffs are Logistic Regression is easier to implement and interpret. Tree based models tend to do better to account for nonlinearities
2. Can try hypertuning but usually that's after you try other low hanging fruit

Model Evaluation
1. Accuracy is usually not a good measure in cases of class imbalance

```

## Next Insurance (2019-11-26; Technical Phone Screen)
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

## Next Insurance (2019-12-11; Onsite)
Let's say you have three tables

1. `Policy`: `id`, `class`, `payroll`, `premium`
2. `Claims`: `id`, `dollar_amount`
3. `Features`: `Yelp Reviews`, `Credit Score`, etc.

Let's say we wanted to add the additional features in the `Features` table in to better predict claim amounts to price better. In this case, lets say we want to price as close to the expected dollar amount as much as possible. How would we do this?

First Answer:
```
We can think of this as a regression problem where we are basically just trying to predict claim amount.
```

Second Question: How do you know if your regression model worked well? How do you know if it's "good enough" to use in our pricing models?

Second Answer:
```
You can look at MSE
```

Third Question: But how do you know what MSE is good? Is 1000 good, is 50,000 MSE bad or good?
```
You can calculate a baseline MSE amount using existing actual premium to claim data
``` 

Fourth Question: What might you do if you're not getting a good MSE? How would you think about aggregating results to predict at a group level?

```
Not sure if I had a good answer to this in the interview; see https://towardsdatascience.com/how-to-measure-the-goodness-of-a-regression-model-60c7f87614ce perhaps?
```

Fifth Question: Why might the model be miscalibrated? What can you do about calibration issues?

```
Didn't have a good answer to this during the interview; Googling around seems to yield some useful links
```

## Next Insurance (2019-12-11; Onsite)
Lets say you have one table with the following columns: `class`, `payroll`, `revenue`, `number_employees`. Let's say that there are concerns that certain companies are falsfiying data to get better premiums. How might you check for input data validity?

```
I framed this as an outlier detection problem. Basically the idea is that you have to establish some prior on what you would expect and then compare the actual data to your priors. Things that deviate significantly are likely to be false. 

You could try clustering here; you would need some way to deal with categorical variables. One-Hot encoding can yield sparsity issues. 

A guide on Outlier Detection: https://towardsdatascience.com/a-brief-overview-of-outlier-detection-techniques-1e0b2c19e561
https://towardsdatascience.com/how-to-use-machine-learning-for-anomaly-detection-and-condition-monitoring-6742f82900d7

both of these seem to point to similar solutions
```

## Stanford RegLab (2019-10-14)
With Regression Discontinuity Design, how do you test if there is actually a discontinuity at the threshold? How do you test the bandwidth to use around the threshold?

This is a good practitioner's guide to RDD: https://www.mdrc.org/sites/default/files/regression_discontinuity_full.pdf. Briefly
1. On testing the discontinuity, you can use McCrary's Test
2. There is an approach to use Cross Validation to test the bandwidth around the threshold.

## Metis (2020-05-15)
Let's say you are deciding between two models, kNN regression vs logistic regression. Let's say you trained and they achieved the exact same performance (on train, validation, and test). Which do you choose in production

1. I would still go with Logistic regression because of concerns of overfitting with kNN
2. Also if magically they really were somehow magically the same, still go with Logistic because at test/scoring time, kNN needs to keep track of all training data and then calculate distance between test data to train data to make prediction. This is computationally intensive and slow. Logistic Regression you just need the weights.

## General Prep
How do you test for overfitting?

1. https://stats.stackexchange.com/questions/333199/random-forest-has-almost-perfect-training-auc-compared-to-other-models

# Programming

## Komodo Health (2019-11-19)

Write a program to find the square root of a number

# Behavioral Questions

## General Questions
1. Why are you interested in this company? (Asked in almost every interview. You should definitely have a good answer to this)
2. Tell me about a time you dealt with conflict with a coworker or a manager. How did you resolve it?

## Prealize Health (2019-12-19)

1. Based on what you know so far, what do you think is Prealize's moat (differentiator compared to competitors)
2. Talk about your resume experience. How would you explain it to a technical person? How would you explain it to a non-technical person?
