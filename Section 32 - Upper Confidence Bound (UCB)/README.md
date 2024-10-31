# Upper Confidence Bound (UCB)
<hr>

## The Multi-Armed Bandit Problem - Summary

* We have *d* arms. For example, arms are ads that we display to users each time they connect to a web page.

* Each time a user connects to this web page, that makes a round.

* At each round *n*, we choose one ad to display to the user.

* At each round *n*, ad *i* gives reward *r<sub>i</sub>(n) ∈ {0, 1}: r<sub>i</sub>(n) = 1* **if the user clicked on the ad *i***, *0* **if the user didn't**.

* Our goal is to maximize the total reward we get over many rounds.
<hr>

## Upper Confidence Bound Algorithm

**Step 1:** At each round *n*, we consider two numbers for each ad *i*:
    * *N<sub>i</sub>(n)* - the number of times the ad *i* was selected up to round *n*,
    * *R<sub>i</sub>(n)* - the sum of rewards the ad *i* up to round *n*.

**Step 2:** From these two numbers we compute:
- the average reward of ad *i* up to round *n*<br>
    <code><span style="text-decoration: overline">r</span><sub>i</sub>(n) = R<sub>i</sub>(n) / N<sub>i</sub>(n)</code>

- the confidence interval <code>[<span style="text-decoration: overline">r</span><sub>i</sub>(n) - Δ<sub>i</sub>(n), <span style="text-decoration: overline">r</span><sub>i</sub>(n) + Δ<sub>i</sub>(n)]</code> at round *n* with
    <code>Δ<sub>i</sub>(n) = &#8730;(3 / 2) * (log(n) / N<sub>i</sub>(n))</code>

**Step 3:** We select the ad *i* that has the maximum UCB *<code><span style="text-decoration: overline">r</span><sub>i</sub>(n) + Δ<sub>i</sub>(n)</code>.*
<hr>