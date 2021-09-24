# SQL

## Next Insurance (2019-11-26)
Say you have a table where each row is employee, salary, and department. How would you construct a query to find top earning employee id for each department? High level (actual sql was not required)

```
Basically the idea would be to use a window function to rank each employee by department ordered by salary.
Can then filter to where the rank is above X number
```

# ML and Statistical Modeling

## Recidiviz (2019; Onsite)
Note, forgot to record the interview questions at the time so backfilling

1. The main question I remember was around how to deal with bias 

Basically the answer is that you can't just account for the variables (e.g. racial) in a standard regression. This is because including the variables in there, you can't account for all the unobservables. If you remove the variables, correlated variables will just pick it up (e.g. Zip Code).

There was a "general framework" in a linear regression approach where you combine two regressions, one that uses the variables, one that doesn't, but I'm forgetting.

Machine Learning wise, the idea is to basically add "fairness" to the cost function: https://towardsdatascience.com/understanding-and-reducing-bias-in-machine-learning-6565e23900ac, which generally makes sense. I'm forgetting my original answer but this seems good enough. 

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

## Metis (2020-05-15)
Explain an example of supervised learning vs unsupervised learning as if I was someone new to data science.

## Metis (2020-05-15)
Explain what regularization is

## Metis (2020-05-15)
How would you tune the lambda parameter for regularization?

## Blue Owl (2020-06-01)
1. Are you familiar with GLM models (GLM models are very popular in P&C)
2. Are you familiar with building custom transformers in sci-kit-learn? Are you comfortable with building end-to-end pipelines using customer transformers and grid search?

## General Prep
How do you test for overfitting?

1. https://stats.stackexchange.com/questions/333199/random-forest-has-almost-perfect-training-auc-compared-to-other-models

# Programming

## Komodo Health (2019-11-19)

Write a program to find the square root of a number

## Level (2020-08-21)

Question: Write a program to predict temperature (using only base Python no libraries)

I basically started with just naively predict the average for all cases. More nuanced is you can predict the average based on just the hour. See the [Temperature Prediction](./notebooks/temperature-prediction.ipynb) notebook for more details.

Question: what if you had access to all libraries (pandas, numpy, scikitlearn, etc.) How would you model this now?

You would want to take into account seasons. So set up a spline OLS regression where the splines are defined by season and then do an OLS fit. 

# Behavioral Questions

## General Questions
1. Why are you interested in this company? (Asked in almost every interview. You should definitely have a good answer to this)
2. Tell me about a time you dealt with conflict with a coworker or a manager. How did you resolve it?

## Prealize Health (2019-12-19)

1. Based on what you know so far, what do you think is Prealize's moat (differentiator compared to competitors)
2. Talk about your resume experience. How would you explain it to a technical person? How would you explain it to a non-technical person?

## Bestow Life (2020-06-25)
Conversation with Jonathan (cofounder)

1. Given your experience working with PhDs vs non-PhDs, people with business experience vs research modeling, infrastructure vs data science vs business, how do you think about the effective makeup of the team (e.g. where do you want your team to excel at) and where do you fit?
2. In terms of infrastructure work (I said that's where I'm weakest), do you feel comfortable interfacing with them. How do you reason about tradeoffs even if you are not an expert?
3. What is your experience as a technical lead, how is it relevant to management, where do you feel like you have not yet interfaced the most?
    1. I said project level, full stack. Where I haven't yet interfaced the most directly is hiring specifically (that was likely a mistake, I should have said people management I think because they are looking for someone to directly hire and build out a team. --> but then go into that by saying although I haven't technically been a people manager, in many ways as tech lead I had similar responsibilities). 
4. Where do you see yourself in the future? What do you want to be?

Conversation with Dan (Head Actuary)

1. Given limited experience, how do you think about modeling and how do you know it works?
    1. My answer, which seemed to resonate quite well with him, was well in general you can look for proxies, you can do pilots, but honestly mortality predictions would not be my first bet. I would look first into growth, maybe some fraud detection with the web analytics. You can try some of the mortality stuff and prototype it first, but not commit fully to it yet. We tried reserves and hospitalizations and IBNR at Clover and it was really hard. 
2. Tell me about your background, do you like your current job, why are you interested in Bestow?
3. For the [Sentinel Effect](https://sentineleffect.wordpress.com/about/) productivity and outcomes can be improved through process of observation, should we use computer vision for Face ID to categorize patients?
    1. My answer, we could, i do have computer vision background, but honestly probably not. The whole point of Bestow is to make the process super easy. We're now adding this step of downloading an app taking a picture, it adds additional steps. At that point, why not just put a doctor on the other side and make it a telemedicine visit, but that's the thing we're trying to avoid.
    
## CMS (2020-10-21)
1. Can you think of an example, where you’re working on a problem and you want to use one data technique but you have a disagreement with a coworker who wants to use a different data technique/different tool to solve a problem and how would you resolve?
    1. My answer was rambling. I used the In Home Primary Care Example, I could have been more succinct by saying:
        1. We had an in-home primary care initiative. Clinical folks, executives just wanted to go for it, and just measure pre-post which has a lot of problems
        2. Spent a lot of time convincing them that this is not valid because of bias
        3. Resolved this by setting up an RCT
        4. When setting up the RCT, we didn't have that many lives, so we didn't have a lot of power, this necessitated longer windows, but we didn't have time for longer windows, business reasons/investors, etc.
        5. They wanted to peak early -- which we know is not good because there's so much variance
        6. Dissolved the control group but resolved by setting up Propensity Score Matching
        7. So in each case there's a tension between careful analysis potentially taking up more time/resources vs understanding the true efficacy to guide business decisions and that's how I went about resolving by advocating for analysis but also being realistic and compromising on business decisions. 
