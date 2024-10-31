# Recurrent Neural Networks (RNNs)

## Resources

If you want to add more value to this section, we recommend checking out:

* [The Ultimate Guide to Recurrent Neural Networks](http://www.superdatascience.com/the-ultimate-guide-to-recurrent-neural-networks-rnn/)

*These resources will compliment this course, so we hope you enjoy!*
<hr>

## Plan of Attack

* What we will learn in this section:
    * [The idea behind Recurrent Neural Networks](#the-idea-behind-recurrent-neural-networks)
    * [The Vanishing Gradient Problem](#the-vanishing-gradient-problem)
    * [Long Short-Term Memory (LSTM)](#long-short-term-memory)
    * [Practical Intuition](#lstm-practical-intuition)
    <br>
    <br>
    * [**EXTRA:** LSTM Variations](#lstm-variations)
<hr>

## The Idea Behind Recurrent Neural Networks

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
        <td>AutoEncoders</td>
        <td>Used for Recommendation Systems</td>
    </tr>
</table>
<hr>

### Additional Reading

#### *Sunspring (movie, 2016)*

* *Directed By Oscar Sharp*
* *Written By Benjamin*

<img src = "Images/Additional Reading - Sunspring (movie, 2016).png" alt = "Sunspring (movie, 2016)" width="500px">

#### [Sunspring (movie, 2016) - Oscar Sharp and Benjamin](https://arstechnica.com/the-multiverse/2016/06/an-ai-wrote-this-movie-and-its-strangely-moving/)
<hr>

## The Vanishing Gradient Problem

<img src = "Images\The Vanishing Gradient Problem.png" alt = "The Vanishing Gradient Problem" width="80%">

*<code>W<sub>rec</sub></code>* -> *<code>Recurrent Weight</code>*
##### <code>W<sub>rec</sub> ~ small -> Vanishing</code>

##### <code>W<sub>rec</sub> ~ large -> Exploding</code>

**Solutions:**
1. Exploding Gradient
    * Truncated Backpropagation
    * Penalties
    * Gradient Clipping
2. Vanishing Gradient
    * Weight Initialization
    * Echo State Networks
    * Long Short-Term Memory Networks (LSTMs)
<hr>

### Additional Reading

#### *Untersuchungen zu dynamischen neuronalen Netzen*

*By Sepp (Josef) Hochreiter (1991)*

<img src = "Images/Additional Reading - Untersuchungen zu dynamischen neuronalen Netzen.png" alt = "Untersuchungen zu dynamischen neuronalen Netzen" width="500px">

#### [Untersuchungen zu dynamischen neuronalen Netzen - Sepp (Josef) Hochreiter](http://people.idsia.ch/~juergen/SeppHochreiter1991ThesisAdvisorSchmidhuber.pdf)
<hr>

### Additional Reading

#### *Learning Long-Term Dependencies with Gradient Descent is Difficult*

*By Yoshua Bengio et al. (1994)*

<img src = "Images/Additional Reading - Learning Long-Term Dependencies.png" alt = "Learning Long-Term Dependencies with Gradient Descent is Difficult" width="500px">

#### [Learning Long-Term Dependencies with Gradient Descent is Difficult - Yoshua Bengio](https://www.comp.hkbu.edu.hk/~markus/teaching/comp7650/tnn-94-gradient.pdf)
<hr>

### Additional Reading

#### *On The Difficulty of Training Recurrent Neural Networks*

*By Razvan Pascanu et al. (2013)*

<img src = "Images/Additional Reading - On The Difficulty of Training Recurrent Neural Networks.png" alt = "On The Difficulty of Training Recurrent Neural Networks" width="500px">

#### [On The Difficulty of Training Recurrent Neural Networks - Razvan Pascanu](https://proceedings.mlr.press/v28/pascanu13.pdf)
<hr>

## LSTMs

* **Today:**
    * A bit of History
    * LSTM Architecture
    * Example Walkthrough

**Reference:**

#### [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
<hr>

### Additional Reading

#### *Long Short-Term Memory*

*By Sepp Hochreiter & Jurgen Schmidhuber (1997)*

<img src = "Images/Additional Reading - Long Short-Term Memory.png" alt = "Long Short-Term Memory" width="500px">

#### [Long Short-Term Memory - Sepp Hochreiter & Jurgen Schmidhuber](http://www.bioinf.jku.at/publications/older/2604.pdf)
<hr>

### Additional Reading

#### *Understanding LSTM Networks*

*By Christopher Olah (2015)*

<img src = "Images/Additional Reading - Understanding LSTM Networks.png" alt = "Understanding LSTM Networks" width="500px">

#### [Understanding LSTM Networks - Christopher Olah](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
<hr>

## LSTM Practical Intuition

**Reference:**

#### [The Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
<hr>

### Additional Reading

#### *The Unreasonable Effectiveness of Recurrent Neural Networks*

*By Andrej Karpathy (2015)*

<img src = "Images/Additional Reading - The Unreasonable Effectiveness of Recurrent Neural Networks.png" alt = "The Unreasonable Effectiveness of Recurrent Neural Networks" width="500px">

#### [The Unreasonable Effectiveness of Recurrent Neural Networks - Andrej Karpathy](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
<hr>

### Additional Reading

#### *Visualizing and Understanding Recurrent Networks*

*By Andrej Karpathy et al. (2015)*

<img src = "Images/Additional Reading - Visualizing and Understanding Recurrent Networks.png" alt = "Visualizing and Understanding Recurrent Networks" width="500px">

#### [Visualizing and Understanding Recurrent Networks - Andrej Karpathy](https://arxiv.org/pdf/1506.02078.pdf)
<hr>

## LSTM Variations

### Additional Reading

#### *LSTM: A Search Space Odyssey*

*By Klaus Greff et al. (2015)*

<img src = "Images/Additional Reading - LSTM- A Search Space Odyssey.png" alt = "LSTM: A Search Space Odyssey" width="500px">

#### [LSTM: A Search Space Odyssey - Klaus Greff](https://arxiv.org/pdf/1503.04069.pdf)
<hr>
