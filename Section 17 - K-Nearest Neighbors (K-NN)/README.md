# K-Nearest Neighbors (K-NN)

`Good`
- Can make predictions without training.
- Time Complexity is `O(n)`.
- Can be used for both classification and regression.

`Bad`
- Does not work well with large dataset.
- Sensitive to noisy data, missing values and outliers.
- Need feature scaling.
- Choose the correct `K` value.
<hr>

## How did KNN categorize a data point for two groupings?

**Step 1**: Choose the number *K* of neighbors

**Step 2**: Take the *K* nearest neighbors of the new data point, according to the *Euclidean distance*

&emsp;<span style="color: gray">Euclidean Distance = √(x<sub>2</sub> - x<sub>1</sub>)<sup>2</sup> + (y<sub>2</sub> - y<sub>1</sub>)<sup>2</sup></span>

**Step 3**: Among these *K* neighbors, count the number of data points in each category

**Step 4**: Assign the new data point to the category where you counted the most neighbors

<span style="color: skyblue">**Your Model is Ready**</span>
<hr>