# Apriori
<hr>

## Apriori - Support

* **Movie Recommendation:**&emsp;&emsp;<code>support(***M***) = (# user watchlists containing ***M***) / (# user watchlists)</code>

* **Market Basket Optimisation:**&emsp;&emsp;<code>support(***I***) = (# transactions containing ***I***) / (# transactions)</code>
<hr>

## Apriori - Confidence

* **Movie Recommendation:**&emsp;&emsp;<code>confidence(***M<sub>1</sub> → M<sub>2</sub>***) = (# user watchlists containing ***M<sub>1</sub>*** and ***M<sub>2</sub>***) / (# user watchlists containing ***M<sub>1</sub>***)</code>

* **Market Basket Optimisation:**&emsp;&emsp;<code>confidence(***I<sub>1</sub> → I<sub>2</sub>***) = (# transactions containing ***I<sub>1</sub>*** and ***I<sub>2</sub>***) / (# transactions containing ***I<sub>1</sub>***)</code>

**NOTE:-** *confidence* is defined as the number of people who have seen movies *M<sub>1</sub>* and *M<sub>2</sub>* divided by the number of people who have seen movie *M<sub>1</sub>*.
<hr>

## Apriori - Lift

* **Movie Recommendation:**&emsp;&emsp;<code>lift(***M<sub>1</sub> → M<sub>2</sub>***) = confidence(***M<sub>1</sub> → M<sub>2</sub>***) / support(***M<sub>2</sub>***)</code>

* **Market Basket Optimisation:**&emsp;&emsp;<code>lift(***I<sub>1</sub> → I<sub>2</sub>***) = confidence(***I<sub>1</sub> → I<sub>2</sub>***) / support(***I<sub>2</sub>***)</code>
<hr>

## Apriori - Algorithm

* **STEP 1:** Set a minimum *support* and *confidence*

* **STEP 2:** Take all the subsets in transactions having *higher support* than *minimum support*

* **STEP 3:** Take all the rules of these subsets having *higher confidence* than *minimum confidence*

* **STEP 4:** Sort the rules by decreasing *lift*
<hr>