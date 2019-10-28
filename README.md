# Jupiter's Moons and the N-Body Problem

## Summary
Jupiter is the fifth planet from the Sun and by far the largest. Jupiter is more than twice as massive as all the other planets combined (the mass of Jupiter is 318 times that of Earth). Jupiter has around 70-80 known moons, many of which haven't been named yet. Due to it's size, Jupiter has lots of gravity, thus its moons have huge gravitational interactions through their rotation and traslation movements.

This project pretends to simulate the trajectory of Jupiter's four largest moons, also known as _the Galilean moons_, as well as their interactions, so we can make observations and reach some conclusions. The model we will draw on was created using the _N-Body problem_. In the next sections you will find a concise explanation of what the N-Body problem is, and how it helped us to solve our problem.

## Introduction
Probably the most significent contribution that Galileo Galilei made to science was the discovery of the four satellites around Jupiter that are now named in his honor. Galileo first observed the moons of Jupiter on January 7, 1610 through a homemade telescope. He originally thought he saw three stars near Jupiter, strung out in a line through the planet. The next evening, these stars seemed to have moved the wrong way, which caught his attention. Galileo continued to observe the stars and Jupiter for the next week. On January 11, a fourth star (which would later turn out to be Ganymede) appeared. After a week, Galileo had observed that the four stars never left the vicinity of Jupiter and appeared to be carried along with the planet, and that they changed their position with respect to each other and Jupiter. Finally, Galileo determined that what he was observing were not stars, but planetary bodies that were in orbit around Jupiter. This discovery provided evidence in support of the Copernican system and showed that everything did not revolve around the Earth.<br>
Galileo published his observations in Sidereus Nuncius in March 1610. The following pictures show his notes to the eight first days of observation:<br>

![(1) January 7th 1610](pictures/pictures/january7th.png) (1)<br>
_January 7th 1610_<br>
![(2) January 8th 1610](pictures/pictures/january8th.png) (2)<br>
_January 8th 1610_<br>
![(3) January 10th 1610](pictures/pictures/january10th.png) (3)<br>
_January 10th 1610_<br>
![(4) January 11th 1610](pictures/pictures/january11th.png) (4)<br>
_January 11th 1610. "[...]This was at length seen clear as day in many subsequent<br>
observations, and also that there are not only three, but four wandering stars making<br> 
their revolutions about Jupiter." Galileo Galilei._<br>
![(5) January 12th 1610](pictures/pictures/january12th.png) (5)<br>
_January 12th 1610_<br>
![(6) January 13th 1610](pictures/pictures/january13th.png) (6)<br>
_January 13th 1610_<br>
![(7) January 15th 1610](pictures/pictures/january15th.png) (7)<br>
_January 15th 1610. "[...] for the first time four little stars were seen by me in<br>
this formation with respect to Jupiter. Three were on the west and one on the east."<br>
Galileo Galilei._<br>
![(8) January 16th 1610](pictures/pictures/january16th.png) (8)<br>
_January 16th 1610_<br>

Those eight first days of observations are very significant to us since it will be the basement to build up our conclusions at the end of this work.

### But, how is this related to the N-Body Problem?

The basic ideas of N-Body problem were published in 1687 by Sir Isaac Newton in his Principia. The limitations to his work was given later by Henry Poincaré, who described the non-integrability principle as applicable to problems of three and more bodies.

Classically, it refers to the problem of predicting the motion of N celestial bodies that interact gravitationally. Nowadays, other problems, such as those from molecular dynamics, are also often referred to as N-Body problems. For N=1 and N=2 the equations can be solved analytically. N=2 was completely solved by Johann Bernoulli. The case N=3 provides one of the richest of all unsolved dynamical problems because solutions only exists in special cases. In general, numerical methods must be used to simulate such systems.

Many physical phenomena directly or indirectly (when solving a discrete version of a continuous problem) involve, or can be simulated with particle systems, where each particle interacts with all other particles according to the laws of physics. Examples include the gravitational interaction among the stars in a galaxy or the Coulomb forces exerted by the atoms in a molecule and _the interaction between planets that orbit in a solar system_, which can be similarly applied to a planet and how its moons orbit around it. The challenge of efficiently carrying out the related calculations is generally known as the N-body problem.

Mathematically, the N-body problem can be formulated as:<br>
<img src="http://latex.codecogs.com/svg.latex?U(x_{0}) = \sum_{i}F(x_{0},x_{i})" border="0"/> (1)<br>

Where U(**X<sub>0</sub>**) is a physical quantity at x<sub>0</sub> which can be obtained by summing the pairwise
interactions F(**x<sub>0</sub>**,**x<sub>i</sub>**) over the particles of the system. For instance, assume a system of
N particles, located at x<sub>i</sub> and having a mass of _m<sub>i</sub>_. The gravitational force exerted on a
particle **x** having a mass _m_ is then expressed as:<br>

<img src="http://latex.codecogs.com/svg.latex?F(x) = \sum_{i=1}^{N} Gmm_{i}\frac{x-x_{i}}{\left | x-x_{i} \right |^{3}}" border="0"/>  (2)<br>
where G is the gravitational constant.

Therefore, we will take advantage of this N-Body Problem model to predict Jupiter's moons positions through the time, so we can make a simulation of their orbits around this planet by setting up some initial conditions and plotting our results.

## Objectives
1) Understand the _N-Body problem_.
2) Analyze the behavior of the orbits of Jupiter's moons through plotting the simulation of a model based on the N-Body problem.
3) Compare our results and observations to Galileo's contribution back in 1610.

## Methodology
For the reproducibility of our results, please consider the following: <br>
* Our code is based on the code we developed in _Modeling and simulation_ class at ENES UNIDAD MORELIA, UNAM. Its main file is included in this repository as _main.py_. 
* To make things easier to handle, we also created different files for the plotting function (named _plott.py_) and the definition of the classes we will be using (named _Body.py_).
* The main file of _Jupiter's Moons and the N-Body Problem_ is named _main_jupyter.py_ .
* **To make calculations a little bit easier and to reduce computation costs, moons were taken as if they orbit in the same plane and were initialized aligned in their correspondant orbits.**

### Initial conditions
1) **Jupyter** <br> 
&nbsp;&nbsp;&nbsp; position = [0, 0, 0] m <br>
&nbsp;&nbsp;&nbsp; velocity = [0, 0, 0] m/s <br>
&nbsp;&nbsp;&nbsp; mass = 1.898e27 kg <br>
2) **Io** <br>
&nbsp;&nbsp;&nbsp; position = [0, 422000000, 0] m <br>
&nbsp;&nbsp;&nbsp; velocity = [17334, 0, 0] m/s <br>
&nbsp;&nbsp;&nbsp; mass = 8.94e22 kg <br>
3) **Europa** <br>
&nbsp;&nbsp;&nbsp; position = [0, 671000000, 0] m <br>
&nbsp;&nbsp;&nbsp; velocity = [13740, 0, 0] m/s <br>
&nbsp;&nbsp;&nbsp; mass = 4.80e22 kg <br>
4) **Ganymede** <br>
&nbsp;&nbsp;&nbsp; position = [0, 1070000000, 0] m <br>
&nbsp;&nbsp;&nbsp; velocity = [10880, 0, 0] m/s <br> 
&nbsp;&nbsp;&nbsp; mass = 1.48e23 kg <br>

5) **Callisto** <br>
position = [0, 1883000000, 0] m <br>
velocity = [8204, 0, 0] m/s <br>
mass = 1.08e23 kg <br>

6) **dt** <br>
dt = 1 s <br>

7) **Simulation time** <br>
lenTime = 3600 * 24 * 8 s <br>

### Execution
After you have downloaded this repository, run this project by executing the following on your command line:

bash testing.sh

## Results
With the aforementioned initial conditions, our  final simulation came out as follows: <br>
[![Watch on Youtube: https://youtu.be/1iNjpaS8yX8](https://img.youtube.com/vi/1iNjpaS8yX8/0.jpg)](https://www.youtube.com/watch?v=1iNjpaS8yX8) <br>
_Click the image!_

## Conclusions
We simulated eight days of Io's, Europa's, Ganymede's and Callisto's orbits, and out of this, we can conclude the following: <br>
1) First of all, we chose eight days of simulation because Galileo discovered those four moons in that period of time, so we were curious about how much he could have observed in such little days that made him find them out. What he pointed out the most the whole time, was the changing in the stars' positions and sizes, and the way they were moving, which we can actually observe through our simulation.
2) Three out of four of the largest moons of Jupiter can go around it in less than eight days, which means their traslation movement is relatively fast despite Jupiter's size. At first it looked a little bit strange that Galileo could observe such big changes in the _stars'_ positions in lapses of few hours, but now we could prove that it is indeed possible and Galileo was right.
3) Unfortunately we cannot claim we did an exact representation of what Galileo saw since we do not know if the moons were aligned the exact same way we initialized them back in January 7th 1610 (probably not), so we cannot tell many details on how things actually occurred. Still, it would be interesting to try to do an actuall simulation of _those_ 40 days in 1610.
4) Through the animation we could observe how objects closer to the center of gravity of a system tend to have higher orbital speeds. This happens because the speed and acceleration of a satellite are only dependent upon the radius of orbit and the mass of the central body that the satellite is orbiting.

## Bibliography

[1] Title: N-body problem
Authors: Bhatnagar, K. B. & Saha, L. M.<br>
Journal: Astronomical Society of India, Bulletin (ISSN 0304-9523), vol. 21, no. 1, p. 1-25 <br>
Bibliographic Code: 1993BASI...21....1B <br>
Link: http://articles.adsabs.harvard.edu//full/1993BASI...21....1B/0000001.000.html <br>

[2] Luis A. Aguilar. (--). The N-Body Problem. 09/20/2019, from UNAM Link: http://www.astrosen.unam.mx/~aguilar/MySite/Outreach_files/Nbody1_eng.pdf 

[3] Jacques F´ejoz. (--). The N-body problem. 09/20/2019, from Universit´e Paris-Dauphine & Observatoire de Paris Link: https://www.ceremade.dauphine.fr/~fejoz/Articles/Fejoz_2014_nbp.pdf

[4] J.D. Mireles James. (2007). Celestial Mechanics Notes Set 1: Introduction to the N-Body Problem. 09/20/2019, Link: http://cosweb1.fau.edu/~jmirelesjames/introductionNotes.pdf

[5] --. (2018). WHAT IS THE N-BODY PROBLEM?. 09/20/2019, Link: https://gereshes.com/2018/05/07/what-is-the-n-body-problem/

[6] Douglas C. Heggie. (2005). The Classical Gravitational N-Body Problem. 09/20/2019, from Cornell University Link: https://arxiv.org/abs/astro-ph/0503600

[7] Tancred Lindholm,. (1999). N-body algorithms. 09/20/2019, Web page: http://www.cs.hut.fi/~ctl/NBody.pdf

[8] The Nine Planets. (--). Jupiter. 10/22/2019,  Web page: https://nineplanets.org/jupiter/

[9] Calvin J. Hamilton. (2009). The Discovery of the Galilean Satellites. 10/22/2019, Web page: http://solarviews.com/eng/galdisc.htm

[10] Albert Van Helden. (1989). English Translation Galileo Galilei Sidereus Nuncius Venice, 1610. 10/22/2019, from The University of Chicago Link: http://people.reed.edu/~wieting/mathematics537/SideriusNuncius.pdf
