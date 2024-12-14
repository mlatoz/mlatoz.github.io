# Boltzmann Machine

## Boltzmann Machine

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
        <td><b>Deep Boltzmann Machines</b></td>
        <td><b>Used for Recommendation Systems</b></td>
    </tr>
    <tr>
        <th></th>
        <td>AutoEncoders</td>
        <td>Used for Recommendation Systems</td>
    </tr>
</table>
<hr>

## Energy-Based Model (EBM)

### Boltzmann Distribution:

<code>p<sub>i</sub> = e<sup>-ε<sub>i</sub>/kT</sup> / <sub>j = 1</sub>∑<sup>M</sup> e<sup>-ε<sub>j</sub>/kT</sup></code>

where:-

    pi = Probability of a certain state of a system (Here i)
    εi = Energy of that system
    k = Constant
    T = Temperature

    "pi" is inversely proportional to "εi"

### Energy Function for a Restricted Boltzmann Machine:-

<code>E(v, h) = -<sub>i</sub>∑ a<sub>i</sub>v<sub>i</sub> - <sub>j</sub>∑ b<sub>j</sub>h<sub>j</sub> - <sub>i</sub>∑<sub>j</sub>∑ v<sub>i</sub> w<sub>i,j</sub> h<sub>j</sub></code>

### Probability of being in a certain state:-
<code>P(v, h) = 1/Z e<sup>-E(v, h)</sup></code>

where

    Z = Sum of all the values of the possible states
<hr>

### Additional Reading

#### *A Tutorial on Energy-Based Learning*

*By Yann LeCun et al. (2006)*

<img src = "Images/Additional Reading - A Tutorial on Energy-Based Learning.png" alt = "A Tutorial on Energy-Based Learning" width="500px">

#### [A Tutorial on Energy-Based Learning - Yann LeCun](http://yann.lecun.com/exdb/publis/pdf/lecun-06.pdf)
<hr>

### Additional Reading

#### *Mr. Nobody (film)*

*By Jaco Van Dormael (2009)*

<img src = "Images/Additional Reading - Mr. Nobody (film).png" alt = "Mr. Nobody (film)" width="500px">

#### [Mr. Nobody (film) - Jaco Van Dormael](http://www.imdb.com/title/tt0485947/)
<hr>

### Reference:- [Boltzmann Distribution](https://en.wikipedia.org/wiki/Boltzmann_distribution)
<hr>

## Contrastive Divergence

* It allows Restricted Boltzmann Machines to learn.

<img src = "Images/Contrastive Divergence.png" alt = "Mr. Nobody (film)" width="800px">

<code>∂logp(<b>v</b><sup>0</sup>) / ∂<sub>w<sub>ij</sub></sub> = < v<sub>i</sub><sup>0</sup> h<sub>j</sub><sup>0</sup> > - < v<sub>i</sub><sup>∞</sup> h<sub>j</sub><sup>∞</sup> ></code>

where

    It is a Gradient Formula.
<hr>

### Additional Reading

#### *A fast learning algorithm for deep belief nets*

*By Geoffrey Hinton et al. (2006)*

<img src = "Images/Additional Reading - A fast learning algo for DBNs.png" alt = "A fast learning algorithm for deep belief nets" width="500px">

#### [A fast learning algorithm for deep belief nets - Geoffrey Hinton](https://www.cs.toronto.edu/~hinton/absps/fastnc.pdf)
<hr>

### Additional Reading

#### *Notes on Contrastive Divergence*

*By Oliver Woodford (2012)*

<img src = "Images/Additional Reading - Notes on Contrastive Divergence.png" alt = "Notes on Contrastive Divergence" width="500px">

#### [Notes on Contrastive Divergence - Oliver Woodford](http://www.robots.ox.ac.uk/~ojw/files/NotesOnCD.pdf)
<hr>

## Deep Belief Networks

### Additional Reading

#### *Greedy Layer - Wise Training of Deep Networks*

*By Yoshua Bengio et al. (2006)*

<img src = "Images/Additional Reading - Greedy Layer.png" alt = "Greedy Layer - Wise Training of Deep Networks" width="500px">

#### [Greedy Layer-Wise Training of Deep Networks - Yoshua Bengio](http://www.iro.umontreal.ca/~lisa/pointeurs/BengioNips2006All.pdf)
<hr>

### Additional Reading

#### *The wake-sleep algorithm for unsupervised neural networks*

*By Geoffrey Hinton et al. (1995)*

<img src = "Images/Additional Reading - The wake-sleep algorithm.png" alt = "The wake-sleep algorithm for unsupervised neural networks" width="500px">

#### [The wake-sleep algorithm for unsupervised neural networks - Geoffrey Hinton](http://www.gatsby.ucl.ac.uk/~dayan/papers/hdfn95.pdf)
<hr>

## Deep Boltzmann Machines

* **NOTE:** *Deep Belief Networks* are **not the same** as *Deep Boltzmann Machines*.

* DBMs can extract features that are more sophisticated, more complex and therefore they could be used for more complex tasks.
<hr>

### Additional Reading

#### *Deep Boltzmann Machines*

*By Ruslan Salakhutdinov et al. (2009)*

<img src = "Images/Additional Reading - Deep Boltzmann Machines.png" alt = "Deep Boltzmann Machines" width="500px">

#### [Deep Boltzmann Machines - Ruslan Salakhutdinov](http://www.utstat.toronto.edu/~rsalakhu/papers/dbm.pdf)
<hr>

<a href="../">«Previous</a> | 
