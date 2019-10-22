"""
main.py solve the n-body problem using newton
Copyright (C) 2019 Jorge Antonio Camarena Pliego (camarenapliego@gmail.com)
Keshava Tonathiu Sanchez Barbosa (keshava.t.s.b@gmail.com)
Stephany Dzoara Vargas Mier (stephanydvm@comunidad.unam.mx)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import math
from Body import *
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

i=0
step = 0

def plott(x, y, v, a):
    fig, ax = plt.subplots(3)

    ax[0].set(xlabel = 'time[sec]', ylabel = 'distance[km]', title = 'N-Body')
    ax[0].plot(x, y, label = 'caption')
    ax[0].grid()

    ax[1].set(xlabel = 'time[sec]', ylabel = 'velocity[km/s]')
    ax[1].plot(x, v, label = 'caption')
    ax[1].grid()

    ax[2].set(xlabel = 'time[sec]', ylabel = 'acceleration[km/s^2]')
    ax[2].plot(x, a, label = 'caption')
    ax[2].grid()

    plt.show()

def plot3d(x, y, v, a, A):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    
    for point in y:
        ax.scatter(point[0], point[1], point[2], marker = 'o')

    point = A.getPos()
    ax.scatter(point[0], point[1], point[2], marker = 'o')

    plt.show()

def dynamicPLot3d(system, particles,step):
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection = '3d')

    #global i
    #global step
    #c = ['g', 'r', 'b', 'r']
    trajectories = np.zeros((len(particles),3))
    for j in range(len(particles)):
        trajectories[j] = particles[j].history_channel[step]
        #ax.scatter(y[0], y[1], y[2], marker = 'o', c = c[i])
        #i = (i+1)%4
    #step+=1
    return trajectories

            
