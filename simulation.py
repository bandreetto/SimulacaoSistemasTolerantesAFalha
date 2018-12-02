#!/usr/bin/env python

from matplotlib import pyplot as plt
import numpy


legends = []
N = 1000000
mttf = 300*60
mttr = 1*60
u = 1/mttr

#uc = 1/mttr # A
uc = 0      # R
dt = 5

xValues = numpy.arange(N+1)*dt;

#plt.title("Availability") 
plt.title("Reliability") 


plt.xlabel("Time (minutes)") 

#plt.ylabel("A") 
plt.ylabel("R") 

for k in range(5):
    print('Plot ' + str(k))
    
    lamb = 1/mttf    
    c1 = 1 - 0.05*k
    c2 = .9

    markovMatrix = [
        [1 - 2*lamb*dt,                 u*dt,  uc*dt],
        [lamb*dt*(c1+c2), 1 - 2*lamb*dt - u*dt,          0],
        [lamb*dt*(2 - c1 - c2),                 2*lamb*dt, 1 - uc*dt]
    ]
    
    
    p = [numpy.matrix([[1], [0], [0]])]
    m = numpy.matrix(markovMatrix)
    
    for i in range(0, N):
        p.append(numpy.dot(m, p[-1]))
        if i%10000 == 0:
            print(i)
    
    #print(m)
    print('done')
    
    
    #Reliability
    # R(t) = P0(t) + P1(t) = [1 1 0] dot P
    R = list(map(lambda pt: numpy.dot(numpy.matrix([1,1,0]), pt).item(0,0), p))
    
    mttf = numpy.trapz(R, x = xValues) # Valores espaçados de 1 minuto
    mttf_hours =mttf/60.0

    #plt.plot(R, label="C1 = {0:.4f}, C2={1:.4f}, Ass = {2:.5f}".format(c1, c2, R[-1]), markevery=100)
    plt.plot(xValues, R, label="C1 = {0:.4f}, C2={1:.4f}, MTTF = {2:.1f} hours".format(c1, c2, mttf_hours), markevery=1000)
    
    #plt.legend(handles=[line_R])
    #legends.append(R)
plt.legend(loc='upper right', frameon=False)
plt.show()
