'''
==================================================================
Tek değişkenli fonksiyonlarda Newton-Raphson Algoritması
==================================================================

Belirli bir başlangıç noktasında göre en iyi çözüme yakınsar.
'''


#Fonksiyon denklemi ve türevi tanımlanır
def f(x) : return pow(x,3) - 2*x - 5 
def dfdx(x) : return 3*pow(x,2) - 2
def nr(x): return x - f(x)/dfdx(x)

x = int(input("Başlangıç noktası: "))
y = nr(x)

#Algoritma 1000 iterastona kadar çalışır. Hassasisyet düzeyi 0.001'dir.
while True:
    for i in range(1000):
        x,y = y,nr(y)
    if (y - x < 0.001):
        break
print(y)