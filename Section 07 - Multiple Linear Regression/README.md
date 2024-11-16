# Multiple Linear Regression

* *Multiple Linear Regression* is a statistical technique used to model the relationship between multiple variables and a single dependent variable. It is used when we want to predict the value of a dependent variable based on the values of one or more independent variables.

* In simple terms, it is used to find the best-fit line that represents the relationship between the independent variables and the dependent variable. The *best-fit line* is the line that minimizes the sum of the squared errors between the predicted values and the actual values.

* The multiple linear regression model assumes that the relationship between the dependent variable and the independent variables is *linear*. It also assumes that the errors between the predicted values and the actual values are *normally distributed*.

* The multiple linear regression model is widely used in various fields such as finance, economics, and marketing to predict the outcome of a dependent variable based on the values of one or more independent variables. It is also used in machine learning to predict the outcome of a dependent variable based on the values of one or more independent variables.

* In summary, multiple linear regression is a powerful statistical technique used to model the relationship between multiple variables and a single dependent variable. It is widely used in various fields to predict the outcome of a dependent variable based on the values of one or more independent variables.
<hr>

## Dummy Variables

* *Dummy variables* are a type of statistical technique used in data analysis and machine learning. They are binary variables, which take on the values of 0 or 1, and are used to represent categorical variables in a statistical model.

* In a regression analysis, for example, a dummy variable is used to represent whether a particular predictor variable is present or absent in a sample. For example, if we are studying the effect of two different treatments on a response variable, we might use a dummy variable to represent whether the treatment was applied or not.

* In a logistic regression model, for example, a dummy variable is used to represent the presence or absence of a particular predictor variable in a sample. For example, if we are studying the effect of two different treatments on a response variable, we might use a dummy variable to represent whether the treatment was applied or not.

* In summary, dummy variables are used to represent categorical variables in a statistical model, and they are binary variables that take on the values of 0 or 1. They are commonly used in regression and logistic regression models to represent predictor variables that take on a limited number of values.

<table>
    <tr>
        <th>Profit</th>
        <th>R&D Spend</th>
        <th>Admin</th>
        <th>Marketing</th>
        <th>State</th>
    </tr>
    <tr>
        <td>192, 261.83</td>
        <td>165, 349.20</td>
        <td>136, 897.80</td>
        <td>471, 784.10</td>
        <td>New York</td>
    </tr>
    <tr>
        <td>191, 792.06</td>
        <td>162, 597.70</td>
        <td>151, 377.59</td>
        <td>443, 898.53</td>
        <td>California</td>
    </tr>
    <tr>
        <td>191, 050.39</td>
        <td>153, 441.51</td>
        <td>101, 145.55</td>
        <td>407, 934.54</td>
        <td>California</td>
    </tr>
    <tr>
        <td>182, 901.99</td>
        <td>144, 372.41</td>
        <td>118, 671.85</td>
        <td>383, 199.62</td>
        <td>New York</td>
    </tr>
    <tr>
        <td>166, 187.94</td>
        <td>142, 107.34</td>
        <td>91, 391.77</td>
        <td>366, 168.42</td>
        <td>California</td>
    </tr>
</table>
<hr>

## Building a Model

### 5 methods of building models:
1. All-in
2. Backward Elimination
3. Forward Selection
4. Bidirectional Elimination
5. Score Comparison

#### 1. "All-in" - cases:
* Prior knowledge; OR
* You have to; OR
* Preparing for Backward Elimination

#### 2. Backward Elimination
* **Step 1:** Select a significance level to stay in the model (e.g. SL (Significance Level) = 0.05)
* **Step 2:** Fit the full model with all possible predictors
* **Step 3:** Consider the predictor with the <u>highest</u> P-value. If `P > SL`, go to STEP 4, otherwise go to FIN (Finish)
* **Step 4:** Remove the predictor

*NOTE:* The "*" represents important
* **Step 5:** Fit model without this variable*

#### 3. Forward Selection
* **Step 1:** Select a significance level to enter the model (e.g. SL = 0.05)
* **Step 2:** Fit all simple regression models <code>y - x<sub>n</sub></code> Select the one with the lowest P-value
* **Step 3:** Keep this variable and fit all possible models with one extra predictor added to the one(s) you already have
* **Step 4:** Consider the predictor with the <u>lowest</u> P-value. If `P < SL`, go to STEP 3, otherwise go to FIN
* **FIN:** Keep the previous model

#### 4. Bidirectional Elimination
* **Step 1:** Select a significance level to enter and to stay in the model (e.g. SLENTER = 0.05, SLSTAY = 0.05)
* **Step 2:** Perform the next step of Forward Selection (new variables must have `P < SLENTER` to enter)
* **Step 3:** Perform ALL steps of Backward Elimination (old variables must have `P < SLSTAY` to stay)
* **Step 4:** No new variables can enter and no old variables can exit
* **FIN:** Your Model is Ready

#### 5. All Possible Models
* **Step 1:** Select a criterion of goodness of fit (e.g. Akaike criterion)
* **Step 2:** Construct All Possible Regression Models: <code>2<sup>N-1</sup></code> total combinations
* **Step 3:** Select the one with the best criterion
* **FIN:** Your Model is Ready
<hr>

## Download Resources
* <a href="Python/Multiple Linear Regression in Python.ipynb" download>Python Notebook</a>
* <a href="Assumptions of Linear Regression.ipynb" download>Assumptions of Linear Regression</a>
* <a href="R/01. Multiple Linear Regression in R.r" download>R Code</a>
* <a href="R/02. Backward Elimination.r" download>R Code</a>
* <a href="R/03. Automatic Implementation of BE in R.r" download>R Code</a>
* <a href="Python/50_Startups.csv" download>Dataset</a>
<hr>

<a href="../Section 06 - Simple Linear Regression">«Previous</a> | <a href="../Section 08 - Polynomial Regression">Next»</a>
