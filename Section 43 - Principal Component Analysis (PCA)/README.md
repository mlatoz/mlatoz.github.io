# Principal Component Analysis (PCA)
<hr>

*Uses:-*
* Noise Filtering
* Visualization
* Feature Extraction
* Stock Market Predictions
* Gene Data Analysis

*Goals:-*
* Identify patterns in data
* Detect the correlation between variables
* Reduce the dimensions of a d-dimensional dataset by projecting it onto a (*k*) - dimensional subspace (where *k < d*)

*Main Functions of the PCA items:-*
* Standardize the data
* Obtain the Eigen vectors and Eigen values from the covariance matrix or correlation matrix, or perform Singular Vector Decomposition.
* Sort Eigen values in descending order and choose the *k* Eigen vectors that correspond to the *k* largest Eigen values where *k* is the number of dimensions of the new feature subspace (*k <= d).
* Construct the projection matrix **W** from the selected *k* Eigen vectors.
* Transform the original dataset **X** via **W** to obtain a *k-dimensional* feature subspace **Y**

    https://plot.ly/ipython-notebooks/principal-component-analysis/
    
    http://setosa.io/ev/principal-component-analysis/

*PCA is attempting to:-*
* Learn about the relationship between **X** and **Y** values
* Find list of principal axes
<hr>