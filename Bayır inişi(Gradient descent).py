'''
============================================
Bayır inişi (Gradient descent) yöntemi
============================================

Örnek: Zmax = f(x,y) = (x-2)**2 + x + y**2   (x,y)eR**2  Başlangıç noktasından bağımsız olarak 
cebirsel çözüm üretir.
'''

import numpy as np
from sympy import *
from sympy.abc import *
from sympy.interactive import *
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import contour
init_printing(pretty_print=True)

def fonksiyon(x,y): 
    return pow(x-2,2)+x+pow(y,2)

z = fonksiyon(x,y)

def kısmi_türev(z): 
        ktx = Derivative(z,x) 
        kty = Derivative(z,y) 
        return [ktx.doit(), kty.doit()]
nv = kısmi_türev(z)


def optimum(a,b):

    nnv = np.array([nv[0].subs(x,a), nv[1].subs(y,b)])
    büyüklük = root(pow(nnv[0], 2) + pow(nnv[1], 2), 2)
    
    d1 = np.array([a,b]) + t*nnv
    d2 = solve(diff(fonksiyon(d1[0],d1[1]),t),t)
    d3 = float(d2[0])
    d4 = np.array([a,b]) + d3*nnv 
    
    a = d4[0]
    b = d4[1]
    
    return np.array([a,b,büyüklük])

yeni_adım = optimum(a,b)
for i in range(100):
    yeni_adım = optimum(a,b)
    basamak = yeni_adım[2]
    if basamak == 0:
        break
    
sonuç = fonksiyon(yeni_adım[0],yeni_adım[1])
print("son a noktası: {}, son b noktası: {}, extremum nokta: {}".format(yeni_adım[0],yeni_adım[1],sonuç))

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
z = fonksiyon(x,y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.viridis)
plt.show() "