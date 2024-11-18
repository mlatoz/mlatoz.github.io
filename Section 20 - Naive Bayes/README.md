# Bayes' Theorem

`Good`
- Training period is less.
- Better suited for categorical inputs.
- Easy to implement.

`Bad`
- Assumes that all features are independent which is rarely happening in real life.
- Zero frequency.
- Estimations can be wrong in some cases.
<hr>

* Formula:
        
        P(A|B) = P(B|A) * P(A) / P(B)

## Why Naive Bayes Theorem is called "Naive"?
--> Independence Assumption
<hr>

## What happens if we have "More than 2 classes/features"?
--> In the case of more than two classes or features in Naive Bayes classification, the algorithm will still work, but the results may not be as accurate. This is because the Naive Bayes algorithm assumes that the features are independent of each other, which may not be the case when there are more than two features.

One way to address this issue is to use a different classification algorithm that does not assume independence of features, such as a decision tree or a support vector machine.
<hr>

## Download Resources
* <a href="Python/Naive Bayes.ipynb" download>Python Notebook</a>
* <a href="Python/Social_Network_Ads.csv" download>Dataset</a>
* <a href="R/Naive Bayes in R.r" download>Naive Bayes | R Code</a>
<hr>

<a href="../Section 19 - Kernel SVM">«Previous</a> | <a href="../Section 21 - Decision Tree Classification">Next»</a>
