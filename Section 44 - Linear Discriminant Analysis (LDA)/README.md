# Linear Discriminant Analysis (LDA)
<hr>

*Uses:-*
* Used as a *dimensionality reduction* technique

* Used in the pre-processing step for pattern classification

* Has the goal to project a dataset onto a lower-dimensional space

Sounds similar to PCA right?
* LDA differs because in addition to finding the component axises with LDA we are interested in the axes that maximize the separation between multiple classes.

Breaking it down further:-
* The goal of LDA is to project a feature space (a dataset n-dimensional samples) onto a small subspace *k* (where *k <= n-1*) while maintaining the class-discriminatory information.

* Both PCA and LDA are linear transformation techniques used for dimensional reduction. PCA is described as unsupervised by LDA is **supervised** because of the relation to the dependent variable.
<hr>

## PCA vs LDA

<img src="PCA vs LDA.png" alt="PCA vs LDA" width="75%">

[2014 Python LDA Article](https://sebastianraschka.com/Articles/2014_python_lda.html)
<hr>

## Five Main Steps for LDA:-

1. Compute the ***d***-dimensional mean vectors for the different classes from the dataset.

2. Compute the scatter matrices (in-between-classes and within-class scatter matrix).

3. Compute the eigen vectors (***e<sub>1</sub>, e<sub>2</sub>, ..., e<sub>d</sub>***) and corresponding eigen values (***ƛ<sub>1</sub>, ƛ<sub>2</sub>, ..., ƛ<sub>d</sub>***) for the scatter matrices.

4. Sort the eigen vectors by decreasing eigen values and choose ***k*** eigen vectors with the largest eigen values to form a ***d * k*** dimensional matrix ***W*** (where every column represents an eigen vector).

5. Use this ***d * k*** eigen vector matrix to transform the samples onto the new subspace. This can be summarized by the matrix multiplication: ***Y = X * W*** (where ***X*** is a ***n * d***-dimensional matrix representing the ***n*** samples, and ***y*** are the transformed ***n * k***-dimensional samples in the new subspace).

[2014 Python LDA Article](https://sebastianraschka.com/Articles/2014_python_lda.html)
<hr>