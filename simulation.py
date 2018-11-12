#!/usr/bin/env python

from matplotlib import pyplot as plt

import numpy
mttf = 300*60
mttr = 1*60
u = 1/mttr
lamb = 1/mttf
dt = .1
c1 = .8
c2 = .9

#N = 1000000
N = 1000000


markovMatrix = [
    [1 - 2*lamb*dt,                 u*lamb*dt,  u*lamb*dt],
    [lamb*dt*(c1+c2), 1 - 2*lamb*dt - u*lamb*dt,          0],
    [lamb*dt*(2 - c1 - c2),                 2*lamb*dt, (1 - u)*lamb*dt]
]


p = [numpy.matrix([[1], [0], [0]])]
m = numpy.matrix(markovMatrix)

for i in range(0, N):
    p.append(numpy.dot(m, p[-1]))

print(m)


#Reliability
# R(t) = P0(t) + P1(t) = [1 1 0] dot P
R = list(map(lambda pt: numpy.dot(numpy.matrix([1,1,0]), pt).item(0,0), p))
plt.title("Reliability") 
plt.xlabel("Time (minutes)") 
plt.ylabel("R") 
plt.plot(R) 
plt.show()
