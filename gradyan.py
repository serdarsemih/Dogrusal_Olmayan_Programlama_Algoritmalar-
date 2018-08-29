'''
========================================================================================
Gradyan (En dik artış) metodu
========================================================================================

Örnek: Zmax = f(x,y) = -(x-2)**2 - x - y**2   (x,y)eR**2  Başlangıç noktası = (2.5, 1.5) olsun.

İşlem adımları:
1.Adım: Kütüphanelerin yüklenmesi
2.Adım: Z fonksiyonunun tanımlanması
3.Adım: Extremum noktayı, extremum noktadaki eğimin büyüklüğünü ve z fonksiyonunun yüzey grafiğini
verecek olan ekdik() fonksiyonunun tanımlanması
4.Adım: (a,b) başlangıç değerleri yerine yeni değerlerin atanması
'''
#1. Adım: Kütüphanelerin yüklenmesi
import numpy as np
from sympy import *
from sympy.abc import *
from sympy.interactive import *
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import contour
init_printing(pretty_print=True)

#2.Adım: Z fonksiyonunun tanımlanması
def fonksiyon(x,y): return -pow(x-2,2)-x-pow(y,2)

#3.Adım: Extremum noktayı, extremum noktadaki eğimin büyüklüğünü ve 
# z fonksiyonunun yüzey grafiğini verecek fonksiyonun tanımlanması
# (a,b) başlangıç noktası koordinatlarıdır.
def endik(a,b):
    #3.1.Adım: Z fonksiyonunun yüzey grafiğinin tanımlanması
    x = np.arange(-5, 5, 0.25)
    y = np.arange(-5, 5, 0.25)
    x, y = np.meshgrid(x, y)
    z = fonksiyon(x,y)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.viridis)
    yüzey = plt.show() #endik fonksiyonu yüzey'i döndürecek
    #3.2.Adım: Bulunduğu noktada z fonksiyonunun eğimini veren gradyan fonksiyonunun tanımlanması
    z = fonksiyon(x,y)    
    for i in range(1,100): #Algoritma eğim sıfıra yaklaşana kadar dönecek
        def gradyan(z,a,b): #gradyan; z fonksiyonunun (a,b) noktasındaki yönlü türevini verir
            ktx = Derivative(z,x) #z'nin x'e göre kısmi türevi
            kty = Derivative(z,y) #z'nin y'ye göre kısmi türevi
            nabla_vek = [ktx.doit(), kty.doit()] #gradyan vektörünün cebirsel hali
            nabla_vek = [nabla_vek[0].subs(x,a),nabla_vek[1].subs(y,b)] #grad. vekt. hesaplanmış hali 
            return nabla_vek
        
        nf = np.array(gradyan(z,a,b)) #hesaplanmış gradyan vektörünü array'e dönüştürdük
        
        büyüklük = root(pow(nf[0],2)+pow(nf[1],2),2) #Grad. vektörünün (eğimin)büyüklüğünü hesapladık
    
        if round(büyüklük,3) == 0: #eğer eğimin büyüklük sıfıra yakınsa zirvedeyiz demektir
            break

      #3.3. Adım: Yeni (a,b) noktasını belirleyerek zirveye bir adım daha yaklaşıyoruz      
        def adım(a,b,nf):
            t = Symbol("t")
            d1 = np.array([a,b]) + t*nf #taylor denklemi
            d2 = fonksiyon(d1[0],d1[1]) #fonksiyonda yerine koyuyoruz
            d3 = diff(d2,t) #birinci türevini alıp 
            d4 = solve(d3,t) #sıfıra eşitliyoruz ve çözüyoruz
            d5 = np.array([a,b]) + d4[0]*nf  #yeni a,b noktalarımızı buluyoruz
            return d5[0],d5[1]
        d6 = adım(a,b,nf) #adım fonskiyonunu çalıştırıp bir adım ilerliyoruz
        a = d6[0] 
        b = d6[1]
    #4. Adım: a,b'ye yeni değerlerini atıyoruz.
    return ("son a noktası: {}, son b noktası: {}, extremum nokta: {}, eğim: {}".format(a,b,fonksiyon(a,b),büyüklük))