from __future__ import division
from numpy import loadtxt
from pylab import scatter,show, plot, linspace, savefig, xlabel, ylabel, figtext
e = 1.602*pow(10,-19)

data = loadtxt("millikan.txt",float)
x = data[:,0]
y = data[:,1]
scatter(x,y)

ex = sum(x)/len(x)
ey = sum(y)/len(y)
exx = sum(x*x)/len(x)
exy = sum(x*y)/len(x)
m = (exy-ex*ey)/(exx-ex**2)
c = (exx*ey-ex*exy)/(exx-ex**2)
print m*e
print m
print c

x1 = linspace(min(x),max(x),10)
y1 = m*x1+c
plot(x1,y1)
xlabel("Frequency")
ylabel("Voltage")
savefig('fig3.pdf')