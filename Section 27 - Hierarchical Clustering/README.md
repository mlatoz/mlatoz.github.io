# Hierarchical Clustering
<hr>

## HC Intuition: Understanding HC

### Agglomerative HC

* **STEP 1:** Make each data point a single-point cluster **→** That forms *N* clusters

* **STEP 2:** Take the two closest data points and make them one cluster **→** That forms *N-1* clusters

* **STEP 3:** Take the two closest clusters and make them one cluster **→** That forms *N-2* clusters

* **STEP 4:** Repeat **STEP 3** until there is only one cluster

* <table><tr><th>FIN</th></tr></table>
<hr>

### Euclidean Distance

<img src="Images/image.png" alt="Euclidean Distance" width="500px" height="500px">

<code>Euclidean Distance between P<sub>1</sub> and P<sub>2</sub> = &#x221A;[(x<sub>2</sub>-x<sub>1</sub>)<sup>2</sup> + (y<sub>2</sub>-y<sub>1</sub>)<sup>2</sup>]</code>
<hr>

### Distance Between Clusters

<img src="Images/image-1.png" alt="Distance Between Clusters" width="500px" height="500px">

**Distance Between Two Clusters:**

* Option 1: Closest Points

* Option 2: Furthest Points

* Option 3: Average Distance

* Option 4: Distance Between Centroids
<hr>