# CNN Intuition

## Plan Of Attack

What we will learn in this section:
* [What are Convolutional Neural Networks?](#what-are-convolutional-neural-networks)
* [**Step 1** - Convolution Operation](#step-1---convolution-operation)
* [**Step 1 (b)** - ReLU (*Rectified Linear Unit*) Layer](#step-1b---relu-rectified-linear-unit-layer)
* [**Step 2** - Pooling](#step-2---max-pooling)
* [**Step 3** - Flattening](#step-3---flattening)
* [**Step 4** - Full Connection](#step-4---full-connection)
* [Summary](#summary)

<br>

* [**EXTRA:** Softmax & Cross-Entropy](#soft-max--cross-entropy)
<hr>

## What are Convolutional Neural Networks?

### How does they work?
<img src="Images/How do CNNs work.png" alt="How do CNNs work?" width="500px" height="200px">

### Example
<img src="Images/CNN Working Example.png" alt="CNN Working Example" width="500px" height="200px">

* **STEP 1:** Convolution
* **STEP 2:** Max Pooling
* **STEP 3:** Flattening
* **STEP 4:** Full Connection
<hr>

### Additional Reading

#### *Gradient-Based Learning Applied to Document Recognition*

*By Yann LeCun et al. (1998)*

<img src = "Images/Additional Reading - Gradient-Based Learning.png" alt = "Gradient-Based Learning Applied to Document Recognition" width="500px">

#### [Gradient-Based Learning Applied to Document Recognition - Yann LeCun](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf)
<hr>

## Step 1 - Convolution Operation

<code>(f * g)(t) =<sup>def</sup> <sub>-∞</sub>∫<sup>∞</sup>f(Ƭ) g(t - Ƭ) dƬ</code>

* A Convolution is basically a combined integration of two functions, and it shows you how one function modifies the other.

### Additional Reading

#### *Introduction to Convolutional Neural Networks*

*By Jianxin Wu (2017)*

<img src = "Images/Additional Reading - Intro to CNNs.png" alt = "Introduction to Convolutional Neural Networks" width="500px">

#### [Introduction to Convolutional Neural Networks - Jianxin Wu](http://cs.nju.edu.cn/wujx/paper/CNN.pdf)
<hr>

## Step 1(B) - ReLU (Rectified Linear Unit) Layer

### Additional Reading

#### *Understanding Convolutional Neural Networks with A Mathematical Model*

*By C. C. Jay Kuo (2016)*

<img src = "Images/Additional Reading - Understanding CNNs with A Mathematical Model.png" alt = "Understanding Convolutional Neural Networks with A Mathematical Model" width="500px">

#### [Understanding Convolutional Neural Networks with A Mathematical Model - C. C. Jay Kuo](https://arxiv.org/pdf/1609.04112.pdf)
<hr>

### Additional Reading

#### *Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification*

*By Kaiming He et al. (2015)*

<img src = "Images/Additional Reading - Delving Deep into Rectifiers.png" alt = "Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification" width="500px">

#### [Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification - Kaiming He](https://arxiv.org/pdf/1502.01852.pdf)
<hr>

## Step 2 - Max Pooling

### Additional Reading

#### *Evaluation of Pooling Operations in Convolutional Architectures for Object Recognition*

*By Dominik Scherer et al. (2010)*

<img src = "Images/Additional Reading - Evaluation of Pooling Operations.png" alt = "Evaluation of Pooling Operations in Convolutional Architectures for Object Recognition" width="500px">

#### [Evaluation of Pooling Operations in Convolutional Architectures for Object Recognition - Dominik Scherer](http://ais.uni-bonn.de/papers/icann2010_maxpool.pdf)
<hr>

## Step 3 - Flattening

## Step 4 - Full Connection

## Summary

### Additional Reading

#### *The 9 Deep Learning Papers You Need To Know About (Understanding CNNs Part 3)*

*By Adit Deshpande (2016)*

<img src = "Images/Additional Reading - The 9 Deep Learning Papers.png" alt = "The 9 Deep Learning Papers You Need To Know About (Understanding CNNs Part 3)" width="500px">

#### [The 9 Deep Learning Papers You Need To Know About (Understanding CNNs Part 3) - Adit Deshpande](https://adeshpande3.github.io/The-9-Deep-Learning-Papers-You-Need-To-Know-About.html)
<hr>

## Soft-Max & Cross-Entropy

* **Soft-Max Function**

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;***<code>f<sub>j</sub>(z) = e<sup>z<sub>j</sub></sup> / ∑<sub>k</sub> e<sup>z<sub>k</sub></sup></code>***

* **Cross-Entropy Function**

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;***<code>L<sub>i</sub> = -log(e<sup>f<sub>y<sub>i</sub></sub></sup> / ∑<sub>j</sub> e<sup>f<sub>j</sub></sup>)</code>***

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;***<code>H(p, q) = -∑<sub>x</sub> p(x)  log q(x)</code>***
<hr>

### Additional Reading

#### *A Friendly Introduction to Cross-Entropy Loss*

*By Rob DiPietro (2016)*

<img src = "Images/Additional Reading - A Friendly Intro to Cross-Entropy Loss.png" alt = "A Friendly Introduction to Cross-Entropy Loss" width="500px">

#### [A Friendly Introduction to Cross-Entropy Loss - Rob DiPietro](https://rdipietro.github.io/friendly-intro-to-cross-entropy-loss)
<hr>

### Additional Reading

#### *How to Implement a Neural Network Intermezzo 2*

*By Peter Roelants (2016)*

<img src = "Images/Additional Reading - Implement a NN Intermezzo 2.png" alt = "How to Implement a Neural Network Intermezzo 2" width="500px">

#### [How to Implement a Neural Network Intermezzo 2 - Peter Roelants](http://peterroelants.github.io/posts/neural_network_implementation_intermezzo02/)
<hr>

<a href="../">«Previous</a> | 
