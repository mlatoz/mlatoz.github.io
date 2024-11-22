# Thompson Sampling

## Bayesian Inference

* Ad *i* gets rewards **y** from Bernoulli distribution <code>*p(**y**|θ<sub>i</sub>) ~ ß(θ<sub>i</sub>)*</code>

* *θ<sub>i</sub>* is unknown but we set its uncertainty by assuming it has a uniform distribution <code>*p(θ<sub>i</sub>)* ~ *u*([0, 1])</code>, which is the prior distribution.

* **Bayes Rule:** We approach *θ<sub>i</sub>* by the posterior distribution
<img src="Posterior Distribution.png" width="1000px">

* We get <code>*p(θ<sub>i</sub>|**y**) ~ ß(number of successes + 1, number of failures + 1)*</code>

* At each round *n* we take a random draw *θ<sub>i</sub>(n)* from this posterior distribution *`p(θ<sub>i</sub>|**y**)`*, for each ad *i*.

* At each round *n* we select the ad *i* that has the highest *θ<sub>i</sub>(n)*.
<hr>

## Thompson Sampling Algorithm

**Step 1:** At each round *n*, we consider two numbers for each ad *i*:
* *N<sup>1</sup><sub>i</sub>(n)* - the number of times the ad *i* got reward *1* up to round *n*.
* *N<sup>0</sup><sub>i</sub>(n)* - the number of times the ad *i* got reward *0* up to round *n*.

**Step 2:** For each ad *i*, we take a random draw from the distribution below:

&emsp;&emsp;&emsp;&emsp;&emsp;<code>θ<sub>i</sub>(n) = ß(N<sup>1</sup><sub>i</sub>(n) + 1, N<sup>0</sup><sub>i</sub>(n) + 1)</code>

**Step 3:** We select the ad that has the highest *θ<sub>i</sub>(n)*.
<hr>

## UCB Algorithm v/s Thompson Sampling Algorithm

<table>
    <tr>
        <th>Upper Confidence Bound</th>
        <th>Thompson Sampling</th>
    </tr>
    <tr>
        <td><img src="UCB.png" alt="UCB" width="500px"></td>
        <td><img src="Thompson Sampling.png" alt="Thompson Sampling" width="500px" height="250px"></td>
    </tr>
    <tr>
        <td>Deterministic</td>
        <td>Probabilistic</td>
    </tr>
    <tr>
        <td>Requires update at every round</td>
        <td>Can accommodate delayed feedback</td>
    </tr>
    <tr>
        <td>Less empirical evidence than Thompson Sampling</td>
        <td>Better empirical evidence than UCB</td>
    </tr>
</table>
<hr>

## Download Resources
* <a href="Python/Thompson Sampling.ipynb" download>Python Notebook</a>
* <a href="Python/Ads_CTR_Optimisation.csv" download>Dataset</a>
* <a href="R/Thompson Sampling.r" download>Thompson Sampling | R Code</a>
<hr>

<a href="../Section 32 - Upper Confidence Bound (UCB)">«Previous</a> | <a href="../Section 34 - Part 07 - Natural Language Processing (NLP)">Next»</a>
