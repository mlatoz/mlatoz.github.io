# K-Means Clustering

`Good`
- Simple to implement.
- Scales to large datasets.
- Guarantees convergence.
- Easily adapts to new examples.
- Generalizes to clusters of different shapes and sizes.

`Bad`
- Sensitive to the outliers.
- Choosing the `k` values manually is tough.
- Dependent on initial values.
- Scalability decreases when dimension increases.
<hr>

## What is Clustering? (Supervised vs Unsupervised Learning)

* Clustering can be defined as *grouping an <u>unlabelled</u> data*
<hr>

## The Elbow Method

* Within Cluster Sum of Squares (WCSS):

    &emsp;<b><code>WCSS = &sum;(<sub>P<sub>i</sub> in Cluster 1</sub>) distance(P<sub>i</sub>, C<sub>1</sub>)<sup>2</sup> + &sum;(<sub>P<sub>i</sub> in Cluster 2</sub>) distance(P<sub>i</sub>, C<sub>2</sub>)<sup>2</sup> + ...</code></b>
<hr>

## K-Means++

* **K-Means++ Initialization Algorithm:**
        Step 1: Choose first centroid at random among data points
        Step 2: For each of the remaining data points compute the distance (D) to the <u>nearest</u> out of already selected centroids
        Step 3: Choose next centroid among remaining data points using <u>weighted</u> random selection - weighted by D<sup>2</sup>
        Step 4: Repeat *Steps 2* and *3* until all *k* centroids have been selected
        Step 5: Proceed with standard k-means clustering
<hr>