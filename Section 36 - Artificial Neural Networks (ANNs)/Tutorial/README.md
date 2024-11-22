# ANN Intuition

## Plan Of Attack
What we will learn in this section:
* [The Neuron](#the-neuron)
* [The Activation Function](#the-activation-function)
* How do Neural Networks work? (*example*)
* [How do Neural Networks learn?](#how-do-neural-networks-learn)
* [Gradient Descent](#gradient-descent)
* [Stochastic Gradient Descent](#stochastic-gradient-descent)
* [Backpropagation](#backpropagation)
* [ANN Algorithm Steps](#training-the-ann-with-stochastic-gradient-descent)
<hr>

## The Neuron

* A neuron is a specialized cell that can transmit and receive *electrical* and *chemical* signals in the nervous system.

* Neurons have three main parts: *a cell body*, *dendrites*, and *an axon*.

* Neurons communicate with each other through *synapses*, which are junctions where *neurotransmitters* are released.

<br>
<img src="Images/The Neuron.png" alt="The Neuron" width="500px">
<br>
<img src="Images/The Neuron 2.png" alt="The Neuron" width="500px">
<hr>

### Additional Reading


#### *Efficient BackProp*
*By Yann LeCun et al. (1998)*

<img src = "Images/Additional Reading - Efficient BackProp.png" alt = "Efficient BackProp" width="500px">

<h4><a href="Additional Reading/Efficient Back Propagation.pdf" download>Efficient BackProp - Yann LeCun</a></h4>
<hr>

## The Activation Function
* An activation function is a function that calculates the *output* of a node in an artificial neural network, based on its *inputs* and the *weights* on individual inputs.

* Activation functions are essential for neural networks to *learn complex patterns* in data, as they introduce *non-linearity* and enable the network to approximate any function.

* There are four types of Activation Functions.

* The first one is **Threshold Function**

<img src = "Images/Threshold Function.png" alt = "Threshold Function" width = "500px" height = "300px">

* The second one is **Sigmoid Function**

<img src = "Images/Sigmoid Function.png" alt = "Sigmoid Function" width = "500px" height = "300px">

where<br>&emsp; `x = Sum of weights`

* The third one is **Rectifier Function**

<img src = "Images/Rectifier Function.png" alt = "Rectifier Function" width = "500px" height = "300px">

* The fourth and last one is **Hyperbolic Tangent (tanh) Function**

<img src = "Images/Hyperbolic Tangent Function.png" alt = "Hyperbolic Tangent Function" width = "500px" height = "300px">
<hr>

### Additional Reading

#### *Deep Sparse Rectifier Neural Networks*

*By Xavier Glorot et al. (2011)*

<img src = "Images/Addtional Reading - Deep Sparse Rectifier Neural Networks.png" alt = "Deep Sparse Rectifier Neural Networks" width="500px">

<h4><a href="Additional Reading/Deep Sparse Rectifier Neural Networks.pdf" download>Deep Sparse Rectifier Neural Networks - Xavier Glorot</a></h4>
<hr>

## How do Neural Networks Learn?

* They *receive input data* and *pass it through one or more layers* of neurons, each with a *non-linear* activation function.

* They *produce output data* and *compare* it with the *expected* or *desired output*, using a *loss function* to measure the *error* or *discrepancy*.

* They adjust the *weights* and *biases* of the connections between neurons, using a learning algorithm such as *gradient descent* and a technique called *backpropagation*, to *minimize the loss function* and *reduce the error*.

* They repeat this process for many iterations or epochs, until the network converges to a satisfactory level of performance.

* **The Cost Function:**

    &emsp;&emsp;<code>c = ∑ 1/2 (y^ - y)<sup>2</sup></code>

&emsp;&emsp;&emsp;where<br>&emsp;&emsp;&emsp;&emsp;&emsp;`y^ = y-cap`
<hr>

### Additional Reading

#### *A List of Cost Functions used in Neural Networks, Alongside Applications*

*CrossValidated (2015)*

<img src = "Images/Additional Reading - A List of Cost Functions.png" alt = "A List of Cost Functions used in Neural Networks" width="500px">

#### [A List of Cost Functions used in Neural Networks, Alongside Applications - CrossValidated](http://stats.stackexchange.com/questions/154879/a-list-of-cost-functions-used-in-neural-networks-alongside-applications)
<hr>

## Gradient Descent
* *Gradient Descent* is an optimization algorithm that tries to find the *minimum value* of a function by *iteratively moving in the direction* of the *steepest descent*, which is the *opposite* of the *gradient* of the function.

* *Gradient Descent* is the simplest optimization algorithm which computes gradients of loss function with respect to model weights and updates them by using the following formula:

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<code>w<sub>t</sub> = w<sub>t-1</sub> - a . dw<sub>t</sub></code>

where<br>&emsp;&emsp;`w = Weight Vector`<br>&emsp;&emsp;`dw = Gradient of w`<br>&emsp;&emsp;`a = Learning Rate`<br>&emsp;&emsp;`t = Iteration Number`
<hr>

## Stochastic Gradient Descent
* *Stochastic Gradient Descent* is an iterative optimization algorithm commonly used in machine learning to find the optimal parameters (weights and biases) of a model that minimize a given loss function.

* It's a varient of gradient descent that approximates the true gradient of the loss function by randomly selecting a single data point (or a small batch of data points) at each iteration, rather than using the entire dataset.

* The update rule for SGD is as follows:

      w(t+1) = w(t) - η * ∇J(w(t), x(i), y(i))

where<br>&emsp;&emsp;`w(t)` represents the model parameters (weights and biases)<br>&emsp;&emsp;at iteration `t`.<br><br>&emsp;&emsp;`η` is the learning rate (a hyperparameter that controls the step size).<br><br>&emsp;&emsp;`∇J(w(t), x(i), y(i))` is the gradient of the loss function `J`,<br>&emsp;&emsp;evaluated at the current parameters `w(t)` using a randomly selected<br>&emsp;&emsp;data point `(x(i), y(i))`.
<hr>

### Additional Reading

#### *A Neural Network in 11 Lines of Python (Part 1)*

*Andrew Trask (2015)*

<img src = "Images/Additional Reading - A NN in 11 Lines of Python.png" alt = "A Neural Network in 11 Lines of Python" width="500px">

#### [A Neural Network in 11 Lines of Python - Andrew Trask](https://iamtrask.github.io/2015/07/12/basic-python-network/)
<hr>

### Additional Reading

#### *A Neural Network in 13 Lines of Python (Part 2 - Gradient Descent)*

*Andrew Trask (2015)*

<img src = "Images/Additional Reading - A NN in 13 Lines of Python.png" alt = "A Neural Network in 13 Lines of Python" width="500px">

#### [A Neural Network in 13 Lines of Python - Andrew Trask](https://iamtrask.github.io/2015/07/27/python-network-part2/)
<hr>

## Backpropagation
* *Backpropagation*, short for "backward propagation of errors", is a fundamental algorithm in machine learning used for training artificial neural networks.

* It calculates the gradient of the loss function with respect to the network's weights, enabling the use of optimization algorithms like SGD to update the weights and minimize the loss.
<hr>

### Additional Reading

#### *Neural Networks and Deep Learning*

*Michael Nielson (2015)*

<img src = "Images/Additional Reading - Neural Networks and Deep Learning.png" alt = "A Neural Network in 13 Lines of Python" width="500px">

#### [Neural Networks and Deep Learning - Michael Nielson](http://neuralnetworksanddeeplearning.com/chap2.html)
<hr>

## Training the ANN with Stochastic Gradient Descent

* **STEP 1:** Randomly initialize the weights to small numbers close to `0` (**but not `0`**)

* **STEP 2:** Input the first observation of your dataset in the input layer, each feature in one input node.

* **STEP 3:** *Forward-Propagation:* from left to right, the neurons are activated in a way that the impact of each neuron's activation is limited by the weights. Propagate the activations until getting the predicted result `y`.

* **STEP 4:** Compare the predicted result to the actual result. Measure the generated error.

* **STEP 5:** *Backward-Propagation:* from right to left, the error is back-propagated. Update the weights according to how much they are responsible for the error. The learning rate decides by how much we update the weights.

* **STEP 6:** Repeat Steps `1` to `5` and update the weights after each observation (*Reinforcement Learning*). Or:<br>
              Repeat Steps `1` to `5` but update the weights only after a batch of observations (*Batch Learning*).

* **STEP 7:** When the whole training set passed through the ANN, that makes an epoch. Redo more epochs.
<hr>

<a href="../Section 36 - Artificial Neural Networks (ANNs)">«Previous</a> | 
