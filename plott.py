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
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

def plot3d(x, y, v, a):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    
    for point in y:
        ax.scatter(point[0], point[1], point[2], marker = 'o')

    plt.show()