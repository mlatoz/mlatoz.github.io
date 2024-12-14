# Principal Component Analysis (PCA)

*Uses:-*

    1. Noise Filtering
    2. Visualization
    3. Feature Extraction
    4. Stock Market Predictions
    5. Gene Data Analysis

*Goals:-*
* Identify patterns in data
* Detect the correlation between variables
* Reduce the dimensions of a d-dimensional dataset by projecting it onto a (`k`) - dimensional subspace (where `k < d`)

*Main Functions of the PCA items:-*
* Standardize the data
* Obtain the Eigen vectors and Eigen values from the covariance matrix or correlation matrix, or perform Singular Vector Decomposition.
* Sort Eigen values in descending order and choose the `k` Eigen vectors that correspond to the `k` largest Eigen values where `k` is the number of dimensions of the new feature subspace (`k <= d`).
* Construct the projection matrix **`W`** from the selected `k` Eigen vectors.
* Transform the original dataset **`X`** via **`W`** to obtain a `k-dimensional` feature subspace **`Y`**

<a href="https://plot.ly/ipython-notebooks/principal-component-analysis/">https://plot.ly/ipython-notebooks/principal-component-analysis/</a>
    
<a href="http://setosa.io/ev/principal-component-analysis/">http://setosa.io/ev/principal-component-analysis/</a>

*PCA is attempting to:-*
* Learn about the relationship between **`X`** and **`Y`** values
* Find list of principal axes
<hr>

## Download Resources
* <a href="Python/Principal Component Analysis (PCA).ipynb" download>Python Notebook</a>
* <a href="Python/Wine.csv" download>Dataset</a>
* <a href="R/Principal Component Analysis (PCA).r" download>Principal Component Analysis (PCA) | R Code</a>
<hr>

<a href="../Section 42 - Part 09 - Dimensionality Reduction">«Previous</a> | <a href="../Section 44 - Linear Discriminant Analysis (LDA)">Next»</a>
