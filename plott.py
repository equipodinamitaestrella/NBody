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

def plott(x, y, v):
    fig, ax = plt.subplots(2)
    ax[0].set(xlabel = 'time[sec]', ylabel = 'distance[km]', title = 'N-Body')
    ax[0].plot(x, y, label = 'caption')
    ax[0].grid()

    ax[1].set(xlabel = 'time[sec]', ylabel = 'velocity[km/s]', title = 'N-Body')
    ax[1].plot(x, v, label = 'caption')
    ax[1].grid()

    plt.show()