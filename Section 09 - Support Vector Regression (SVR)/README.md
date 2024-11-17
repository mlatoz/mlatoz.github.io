# Support Vector Regression

* Support Vector Regression (SVR) is a supervised learning algorithm used for regression tasks. It is based on the Support Vector Machines (SVM) algorithm, which was originally developed for classification problems. SVR aims to find a hyperplane that best fits the data while minimizing the error.

* Here are some key points about Support Vector Regression:
    1. <b><i>Regression task:</i></b> SVR is used for solving regression problems, where the goal is to predict a continuous output variable based on input features.

    2. <b><i>Margin and support vectors:</i></b> In SVR, the hyperplane is determined by the support vectors, which are the data points closest to the hyperplane. The margin is the region between the positive and negative hyperplanes. The objective of SVR is to maximize the margin while keeping the deviations (errors) of the data points within a certain tolerance.

    3. <b><i>Loss function:</i></b> SVR introduces a loss function to measure the error of predictions. The commonly used loss function is the epsilon-insensitive loss function. It penalizes predictions that fall outside an epsilon-insensitive tube around the true target value. Data points inside the tube are ignored during model training.

    4. <b><i>Regularization:</i></b> Like in SVM, SVR also uses regularization parameters (C parameter in SVR) to control the trade-off between maximizing the margin and minimizing the errors. A smaller value of C will enforce a larger margin but might allow more errors outside the tube, while a larger C will prioritize minimizing errors over maximizing the margin.

    5. <b><i>Kernel trick:</i></b> SVR, like SVM, can make use of the kernel trick. It allows SVR to implicitly transform the original feature space into a higher-dimensional space, making it capable of capturing complex non-linear relationships between features and the target variable. Common kernel functions include the linear, polynomial, radial basis function (RBF), and sigmoid kernels.

    6. <b><i>Choice of kernel:</i></b> The choice of the kernel function and its hyperparameters plays a crucial role in the performance of the SVR model. Selecting the appropriate kernel and tuning its parameters is often a part of the model selection process.

    7. <b><i>Scalability:</i></b> SVR can become computationally expensive for large datasets since it requires solving a quadratic optimization problem. For larger datasets, using linear kernels or other approximations can be considered to improve scalability.

    8. <b><i>Outliers:</i></b> SVR is sensitive to outliers in the training data, as outliers can significantly affect the position and orientation of the hyperplane. Robust preprocessing techniques and outlier removal methods can be employed to mitigate their impact.

    9. <b><i>Evaluation:</i></b> Common evaluation metrics for SVR models include Mean Squared Error (MSE), Mean Absolute Error (MAE), R-squared (R2), and others, depending on the specific problem and requirements.

* SVR is a powerful regression algorithm, especially when dealing with non-linear relationships and situations where the number of features is greater than the number of samples. However, it requires careful hyperparameter tuning and handling of data preprocessing to achieve optimal results.
<hr>

## Download Resources
* <a href="SVR Additional Reading.txt">SVR Additional Reading</a>
* <a href="Support Vector Regression Book.txt">SVR Recommended Book</a>
* <a href="Python/SVR in Python.ipynb" download>Python Notebook</a>
* <a href="R/SVR in R.r" download>Support Vector Regression | R Code</a>
* <a href="Python/Position_Salaries.csv" download>Dataset</a>
<hr>

<a href="../Section 08 - Polynomial Regression">«Previous</a> | <a href="../Section 10 - Decision Tree Regression">Next»</a>
