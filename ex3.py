from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np
def f(u,x):
    return (u[1],(2*(u[0]-4)*u[1])+x)
y0 = [0,0]
xs = np.linspace(1,1,1)
us = odeint(f,y0,xs)
ys = us[-100:100]
plt.plot(xs,ys,'-')
plt.plot(xs,ys,'r*')
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('(D**2+2*D+2)*y = cos(2*x)')
plt.show()
