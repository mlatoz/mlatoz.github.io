# R-Squared Intuition

## R Squared

* SS<sub>res</sub> = SUM(y<sub>i</sub> - y^<sub>i</sub>)<sup>2</sup>

* SS<sub>tot</sub> = SUM(y<sub>i</sub> - y<sub>avg</sub>)<sup>2</sup>

* R<sup>2</sup> = 1 - SS<sub>res</sub>/SS<sub>tot</sub><br><code>R<sup>2</sup></code> - Goodness of fit (greater is better)

* **NOTE:-**

    If the value of R is:-
    
        1.0 = Perfect fit (suspicious)
        ~0.9 = Very good
        <0.7 = Not great model
        <0.4 = Terrible
        <0 = Model makes no sense for this data
<hr>

# Adjusted R-Squared Intuition
## Adjusted R Squared

* Note:- <code>R<sup>2</sup></code> - Goodness of fit (greater is better)

**Problem:**

&emsp;<code>y^ = b<sub>0</sub> + b<sub>1</sub>X<sub>1</sub> + b<sub>2</sub>X<sub>2</sub></code>

*<code>SS<sub>tot</sub></code>* doesn't change

*<code>SS<sub>res</sub></code>* will decrease or stay the same (This is because of *Ordinary Least Squares*: <code>SS<sub>res</sub></code>-> Min)

**Solution:**

&emsp;<code>Adj R<sup>2</sup> = 1 - (1 - R<sup>2</sup>) * (n - 1)/(n - k - 1)</code>

`k` - number of independent variables<br>
`n` - sample size
<hr>

<a href="../Section 11 - Random Forest Regression">«Previous</a> | <a href="../Section 13 - Regression Model Selection in Python">Next»</a>
