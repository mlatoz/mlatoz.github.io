# Kernel SVM

## Mapping to a Higher Dimension

* Mapping to a Higher Dimensional Space can be highly compute-intensive. So, it may require a lot of computation, a lot of processing power, and, you know, the larger your data set, the more of a problem this can cause.
<hr>

## The Kernel Trick

* **The Gaussian RBF Kernel:-**

    <b><code>K(x-bar, l<sup>i</sup>-bar) = e<sup>-(||x-bar - l<sup>i</sup>-bar||<sup>2</sup> / 2σ<sup>2</sup>)</sup></code></b>

        where,
            K = A Kernel that is a function applied to two vectors.
            x-bar = Point in a dataset
            l = Landmark
            i = No. of landmarks
<hr>

## Types of Kernel Functions

* **Gaussian RBF Kernel:** <code>K(x-bar, l<sup>i</sup>-bar) = e<sup>-(||x-bar - l<sup>i</sup>-bar||<sup>2</sup> / 2σ<sup>2</sup>)</sup></code>

* **Sigmoid Kernel:** <code>K(X, Y) = tanh(γ.X<sup>T</sup>Y + r)</code>

* **Polynomial Kernel:** <code>K(X, Y) = (γ.X<sup>T</sup>Y + r)<sup>d</sup></code>, *γ > 0*
<hr>

## Non-Linear Kernel SVR (Advanced)

### Heads-up about Non-Linear SVR

* Section on SVR:
    * SVR Intuition

* Section on SVM:
    * SVM Intuition

* Section on Kernel SVM:
    * Kernel SVM Intuition
    * Mapping to a higher dimension
    * The Kernel Trick
    * Types of Kernel Functions
    * Non-Linear Kernel SVR
<hr>

## Download Resources
* <a href="Python/Kernel SVM.ipynb" download>Python Notebook</a>
* <a href="Python/Social_Network_Ads.csv" download>Dataset</a>
* <a href="R/Kernel SVM in R.r" download>Kernel SVM | R Code</a>
<hr>

<a href="../Section 18 - Support Vector Machine (SVM)">«Previous</a> | <a href="../Section 20 - Naive Bayes">Next»</a>
