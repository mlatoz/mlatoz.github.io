# Linear Regression

<code>Good</code>

- Simple to implement and efficient to train.
- Overfitting can be reduced by regularization.
- Performs well when the dataset is linearly separable.

<code>Bad</code>

- Assumes that the data is independent which is rare in real life.
- Prone to noise and overfitting.
- Sensitive to outliers.
<hr>

# Simple Linear Regression
* *Simple Linear Regression* is a statistical technique used to model the relationship between two continuous variables: a dependent variable (also known as the *response* or *outcome variable*) and an independent variable (also known as the *predictor* or *explanatory variable*).

* It aims to find the best-fitting straight line through the data points to predict the values of the dependent variable based on the values of the independent variable.

* The equation for a simple linear regression model is typically represented as:

<code>y = β<sub>0</sub> + β<sub>1</sub> * x + ε</code>

<pre>
  Where:
  
    - y is the dependent variable (the variable we want to predict).
  
    - x is the independent variable (the variable used to make predictions).
  
    - β<sub>0</sub> is the intercept, representing the value of y when x is zero.
  
    - β<sub>1</sub> is the slope of the regression line, indicating how much y changes for each unit change in x.
  
    - ε represents the error term, which accounts for the variability of y that is not explained by the regression line.
</pre>

* The goal of simple linear regression is to estimate the values of `β`<sub>`0`</sub> and `β`<sub>`1`</sub> that minimize the sum of squared differences between the predicted values (`β`<sub>`0`</sub> `+ β`<sub>`1`</sub> `* x`) and the actual observed values of the dependent variable. This is usually done using a method called the *least squares approach*.

* Once the regression coefficients (`β`<sub>`0`</sub> and `β`<sub>`1`</sub>) are estimated, the fitted regression line can be used to make predictions for new values of the independent variable.

* *Simple linear regression* is a fundamental and widely used technique in statistics and machine learning for understanding and modeling the relationship between two variables, especially when the relationship appears to be linear. However, when dealing with more complex relationships, multiple linear regression or other advanced regression techniques may be more appropriate.
<hr>

# Ordinary Least Squares
* *Ordinary Least Squares (OLS)* is a method used in simple linear regression to estimate the parameters of a linear relationship between two variables. In simple linear regression, we have a dependent variable (`Y`) and an independent variable (`X`), and we want to find the best-fitting line that represents the linear relationship between them. The equation of the line is given by:

<code>Y = β<sub>0</sub> + β<sub>1</sub> * X</code>

<pre>
  Where:
  
    - Y is the dependent variable (the one we want to predict or explain).
  
    - X is the independent variable (the predictor or explanatory variable).
  
    - β<sub>0</sub> is the intercept (the value of Y when X is 0).
  
    - β<sub>1</sub> is the slope (the change in Y for a one-unit change in X).
</pre>

* The goal of the *OLS* method is to find the values of <code>β<sub>0</sub></code> and <code>β<sub>1</sub></code> that minimize the sum of squared differences between the observed values of `Y` (<code>Y<sub>i</sub></code>) and the predicted values (<code>Ŷ<sub>i</sub></code>) from the linear equation for all data points (`i`) in the dataset.

* Mathematically, the *OLS* estimates of <code>β<sub>0</sub></code> and <code>β<sub>1</sub></code> are obtained as follows:

<code>β<sub>1</sub> = Σ((X<sub>i</sub> - X̄)(Y<sub>i</sub> - Ȳ)) / Σ((X<sub>i</sub> - X̄)<sup>2</sup>)</code>

<code>β<sub>0</sub> = Ȳ - β<sub>1</sub> * X̄</code>

<pre>
  Where:
  
    - Σ represents the sum of.
  
    - X<sub>i</sub> is the value of the independent variable for the i<sup>th</sup> data point.
  
    - Y<sub>i</sub> is the value of the dependent variable for the i<sup>th</sup> data point.
  
    - X̄ is the mean of all X values.
  
    - Ȳ is the mean of all Y values.
</pre>

* The *OLS* method is called "least squares" because it minimizes the sum of the squared vertical distances between the observed data points and the regression line. The line obtained through *OLS* is the "best-fitting" line because it minimizes the total squared error between the observed values and the predicted values.

* Once you have estimated the values of <code>β<sub>0</sub></code> and <code>β<sub>1</sub></code> using *OLS*, you can use the linear equation (<code>Y = β<sub>0</sub> + β<sub>1</sub> * X</code>) to predict the value of the dependent variable `Y` for any given value of the independent variable `X`. Additionally, you can assess the goodness of fit of the regression model and make inferences about the relationship between the two variables using statistical tests and measures such as R-squared, t-tests, etc.
<hr>
