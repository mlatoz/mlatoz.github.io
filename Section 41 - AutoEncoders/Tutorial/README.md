# Auto Encoders

## Auto Encoders

<table>
    <tr>
        <th>Supervised</th>
        <td>Artificial Neural Networks</td>
        <td>Used for Regression & Classification</td>
    </tr>
    <tr>
        <th></th>
        <td>Convolutional Neural Networks</td>
        <td>Used for Computer Vision</td>
    </tr>
    <tr>
        <th></th>
        <td>Recurrent Neural Networks</td>
        <td>Used for Time Series Analysis</td>
    </tr>
</table>
<br>
<table>
    <tr>
        <th>Unsupervised</th>
        <td>Self-Organizing Maps</td>
        <td>Used for Feature Detection</td>
    </tr>
    <tr>
        <th></th>
        <td>Deep Boltzmann Machines</td>
        <td>Used for Recommendation Systems</td>
    </tr>
    <tr>
        <th></th>
        <td><b>AutoEncoders</b></td>
        <td><b>Used for Recommendation Systems</b></td>
    </tr>
</table>
<hr>

**Visual Representation of a Auto Encoder:**

<img src="Images/Auto Encoder.png" alt = "Auto Encoder" width="500px">
<hr>

* As the name suggests an *Auto Encoder* encodes itself.

* It takes some sort of inputs, put some through a hidden layer, and then it gets outputs, but it aims for the outputs to be identical to the inputs.

* Auto Encoders are not a pure type of *Unsupervised Deep Learning Algorithm*.

* They are actually a *Self-Supervised Deep Learning Algorithm*, because they are comparing to something on the end.

* The hidden layer is also called as the *coding layer* or the *bottleneck*.
<hr>

**Uses:**

1. They can be used for feature detection.
2. They can also be used to build powerful recommender systems
3. They are used for encoding, basically.
<hr>

### Additional Reading

#### *Neural Networks Are Impressively Good At Compression*

*By Malte Skarupke (2016)*

<img src = "Images/Additional Reading - Neural Networks.png" alt = "Neural Networks Are Impressively Good At Compression" width="500px">

#### [Neural Networks Are Impressively Good At Compression - Malte Skarupke](https://probablydance.com/2016/04/30/neural-networks-are-impressively-good-at-compression/)
<hr>

## Training an Auto Encoder

### Algorithm:

* **STEP 1:** We start with an array where the lines (*the observations*) correspond to the users and the columns (*the features*) correspond to the movies. Each cell (`u`, `i`) contains the rating (from `1` to `5`, `0` if no rating) of the movie `i` by the user `u`.

* **STEP 2:** The first user goes into the network. The input vector <code>x = (r<sup>1</sup>, r<sup>2</sup>, ..., r<sup>m</sup>)</code> contains all its ratings for all the movies.

* **STEP 3:** The input vector `x` is encoded into a vector `z` of lower dimensions by a mapping function `f` (e.g: *sigmoid function*):
<br>&emsp;&emsp;&emsp;&emsp; <code>z = f(Wx + b)</code><br>where<br>&emsp;&emsp;&emsp;`W` is the *vector of input weights* and `b` the *bias*
<br>
<br>

* **STEP 4:** `z` is then decoded into the output vector `y` of same dimensions as `x`, aiming to replicate the input vector `x`.

* **STEP 5:** The reconstruction error `d(x, y) = ||x-y||` is computed. The goal is to minimize it.

* **STEP 6:** ***Back-Propagation:*** from right to left, the error is back-propagated. The weights are updated according to how much they are responsible for the error. The learning rate decides by how much we update the weights.

* **STEP 7:** Repeat Steps *1* to *6* and update the weights after each observation (*Reinforcement Learning*). Or:<br>&emsp;&emsp;&emsp;&nbsp; Repeat Steps *1* to *6* but update the weights only after a batch of observations (*Batch Learning*).

* **STEP 8:** When the whole training set passed through the **ANN**, that makes an epoch. Redo more epochs.
<hr>

### Additional Reading

#### *Building Autoencoders in Keras*

*By Francois Chollet (2016)*

<img src = "Images/Additional Reading - Building Autoencoders in Keras.png" alt = "Building Autoencoders in Keras" width="500px">

#### [Building Autoencoders in Keras - Francois Chollet](https://blog.keras.io/building-autoencoders-in-keras.html)
<hr>

## Sparse Autoencoders

* A *Sparse Autoencoder* is an autoencoder, where the hidden layer is greater than the input layer. But a *regularization technique* which introduces sparsity has been applied.

&emsp;&emsp;&emsp;<img src = "Images/Autoencoder.png" alt = "Sparse Autoencoder" width="500px">

* A *regularization technique* basically means something that helps prevent over-fitting or stabilizes the algorithm.
<hr>

### Additional Reading

#### *Deep Learning Tutorial - Sparse Autoencoder*

*By Chris McCormick (2014)*

<img src = "Images/Additional Reading - Sparse Autoencoder.png" alt = "Deep Learning Tutorial - Sparse Autoencoder" width="500px">

#### [Deep Learning Tutorial - Sparse Autoencoder - Chris McCormick](http://mccormickml.com/2014/05/30/deep-learning-tutorial-sparse-autoencoder/)
<hr>

### Additional Reading

#### *Deep Learning Tutorial: Sparse Autoencoders*

*By Eric Wilkinson (2014)*

<img src = "Images/Additional Reading - Sparse Autoencoders.png" alt = "Deep Learning Tutorial: Sparse Autoencoders" width="500px">

#### [Deep Learning Tutorial: Sparse Autoencoders - Eric Wilkinson](http://ericlwilkinson.com/blog/2014/11/19/deep-learning-sparse-autoencoders/)
<hr>

### Additional Reading

#### *k-Sparse Autoencoders*

*By Alireza Makhzani et al. (2014)*

<img src = "Images/Additional Reading - k-Sparse Autoencoders.png" alt = "k-Sparse Autoencoders" width="500px">

#### [k-Sparse Autoencoders - Alireza Makhzani](http://arxiv.org/pdf/1312.5663.pdf)
<hr>

## Denoising Autoencoders

* *Denoising Autoencoder* is another regularization technique, which is here to combat the problem of when we have more nodes in the hidden layers than in the input layer.

* Denoising Autoencoder is a *Stochastic Autoencoder*.

* It depends on the random generation or random selection of which values are going to be zeroed out and so it becomes a Stochastic type of Autoencoder.
<hr>

### Additional Reading

#### *Extracting and Composing Robust Features with Denoising Autoencoders*

*By Pascal Vincent et al. (2008)*

<img src = "Images/Additional Reading - Denoising Autoencoders.png" alt = "Extracting and Composing Robust Features with Denoising Autoencoders" width="500px">

#### [Extracting and Composing Robust Features with Denoising Autoencoders - Pascal Vincent](http://www.cs.toronto.edu/~larocheh/publications/icml-2008-denoising-autoencoders.pdf)
<hr>

## Contractive Autoencoders

* *Contractive Autoencoder* is another regularization technique just like sparse autoencoders and denoising autoencoders, which is designed to combat the problem when we have an over-complete hidden layer in the autoencoder.

&emsp;&emsp;&emsp;<img src = "Images/Autoencoder.png" alt = "Sparse Autoencoder" width="500px">

* It leverages the whole training process where information goes through the autoencoder, then we get the outputs and then they are compared with the inputs. *Contractive Autoencoders* add a penalty into this loss-function that has been propagated back through the network, and it specifically doesn't allow the autoencoder to just simply copy these values across.
<hr>

### Additional Reading

#### *Contractive Auto-Encoders: Explicit Invariance During Feature Extraction*

*By Salah Rifai et al. (2011)*

<img src = "Images/Additional Reading - Contractive Auto-Encoders.png" alt = "Contractive Auto-Encoders: Explicit Invariance During Feature Extraction" width="500px">

#### [Contractive Auto-Encoders: Explicit Invariance During Feature Extraction - Salah Rifai](http://machinelearning.wustl.edu/mlpapers/paper_files/ICML2011Rifai_455.pdf)
<hr>

## Stacked Autoencoders

* A *Stacked Autoencoder* is if we add another hidden layer into our autoencoder. So, we have two stages of encoding and one stage of decoding.

<img src = "Images/Stacked Autoencoder.png" alt = "Stacked Autoencoders" width="500px">
<hr>

### Additional Reading

#### *Stacked Denoising Autoencoders: Learning Useful Representations in a Deep Network with a Local Denoising Criterion*

*By Pascal Vincent et al. (2010)*

<img src = "Images/Additional Reading - Stacked Denoising Autoencoders.png" alt = "Stacked Denoising Autoencoders: Learning Useful Representations in a Deep Network with a Local Denoising Criterion" width="500px">

#### [Stacked Denoising Autoencoders - Pascal Vincent](http://www.jmlr.org/papers/volume11/vincent10a/vincent10a.pdf)
<hr>

## Deep Autoencoders

* **NOTE:** *Stacked Autoencoders* are **not the same thing** as *Deep Autoencoders*.

&emsp;&emsp;&emsp;<img src = "Images/Deep Autoencoder.png" alt = "Deep Autoencoders" width="500px">

* These are Restricted Boltzmann Machines (RBMs) that are Stacked. Then they are pre-trained layer by layer. Then they are unrolled. Then they're fine tuned with back propagation. So then you do get directionality in your network and then you have back propagation.

* In essence, a Deep Autoencoder comes from **RBMs**.

* *Stacked Autoencoders* are just **normal autoencoders stacked**. A *Deep Autoencoder* is **RBMs stacked on top of each other** and then certain things are done with them in order to achieve a autoencoding mechanism.
<hr>

### Additional Reading

#### *Reducing the Dimensionality of Data with Neural Networks*

*By Geoffrey Hinton et al. (2006)*

<img src = "Images/Additional Reading - Deep Autoencoders.png" alt = "Reducing the Dimensionality of Data with Neural Networks" width="500px">

#### [Reducing the Dimensionality of Data with Neural Networks - Pascal Vincent](https://www.cs.toronto.edu/~hinton/science.pdf)
<hr>

<a href="../">«Previous</a> | 
