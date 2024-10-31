# Random Forest Classification
<hr>

**STEP 1:** Pick at random *K* data points from the Training set.

**STEP 2:** Building the Decision Tree associated to these *K* data points.

**STEP 3:** Choose the number Ntree of trees you want to build and repeat STEPS 1 & 2.

**STEP 4:** For a new data point, make each one of your Ntree trees predict the category to which the data points belongs, and assign the new data point to the category that wins the majority vote.
<hr>