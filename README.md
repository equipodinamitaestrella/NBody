
# N-Body Problem
## Introduction

The basic ideas of N-Body problem were published in 1687 by Sir Isaac Newton in his Principia. The limitations to his work was given later by Henry Poincaré, who described the non-integrability principle as applicable to problems of three and more bodies.

Classically, it refers to the problem of predicting the motion of N celestial bodies that interact gravitationally. Nowadays, other problems, such as those from molecular dynamics, are also often referred to as N-Body problems. For N=1 and N=2 the equations can be solved analytically. N=2 was completely solved by Johann Bernoulli. The case N=3 provides one of the richest of all unsolved dynamical problems because solutions only exists in special cases. In general, numerical methods must be used to simulate such systems.

Many physical phenomena directly or indirectly (when solving a discrete version of a continuous problem) involve, or can be simulated with particle systems, where each particle interacts with all other particles according to the laws of physics. Examples include the gravitational interaction among the stars in a galaxy or the Coulomb forces exerted by the atoms in a molecule. The challenge of efficiently carrying out the related calculations is generally known as the N-body problem.

Mathematically, the N-body problem can be formulated as:<br>
<img src="http://latex.codecogs.com/svg.latex?U(x_{0}) = \sum_{i}F(x_{0},x_{i})" border="0"/> (1)<br>

Where U(**X<sub>0</sub>**) is a physical quantity at x<sub>0</sub> which can be obtained by summing the pairwise
interactions F(**x<sub>0</sub>**,**x<sub>i</sub>**) over the particles of the system. For instance, assume a system of
N particles, located at x<sub>i</sub> and having a mass of _m<sub>i</sub>_. The gravitational force exerted on a
particle **x** having a mass _m_ is then expressed as:<br>

<img src="http://latex.codecogs.com/svg.latex?F(x) = \sum_{i=1}^{N} Gmm_{i}\frac{x-x_{i}}{\left | x-x_{i} \right |^{3}}" border="0"/>  (2)<br>
where G is the gravitational constant.


## Bibliography

Title: N-body problem
Authors: Bhatnagar, K. B. & Saha, L. M.
Journal: Astronomical Society of India, Bulletin (ISSN 0304-9523), vol. 21, no. 1, p. 1-25
Bibliographic Code: 1993BASI...21....1B
Link: http://articles.adsabs.harvard.edu//full/1993BASI...21....1B/0000001.000.html

http://www.astrosen.unam.mx/~aguilar/MySite/Outreach_files/Nbody1_eng.pdf<br>
https://www.ceremade.dauphine.fr/~fejoz/Articles/Fejoz_2014_nbp.pdf<br>
http://cosweb1.fau.edu/~jmirelesjames/introductionNotes.pdf<br>
https://gereshes.com/2018/05/07/what-is-the-n-body-problem/<br>
https://arxiv.org/abs/astro-ph/0503600<br>
https://www.cs.usask.ca/~spiteri/CMPT851/notes/nBody.pdf<br>
http://www.cs.hut.fi/~ctl/NBody.pdf<br>
