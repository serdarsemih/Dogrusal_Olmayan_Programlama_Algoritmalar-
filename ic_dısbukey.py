def f(x) : return pow(x,2) - 3

def içdış_bükey():
    import numpy as np
    import matplotlib.pyplot as plt
    import time
    
    print("Lütfen bir aralık belirleyin. Seçeceğiniz sayılar tamsayı olmalıdır. Ayrıca seçim yaparken lütfen ilgili fonksiyonun tanım aralığına dikkat edin.")
    x1 = int(input("Alt sınır: "))
    x2 = int(input("Üst Sınır: "))
    time.sleep(1)
    
    x = np.linspace(x1-1,x2+1,(x2-x1)*100)
    fig = plt.figure()
    ax = fig.add_axes([0.1,0.1,0.8,0.8])
    ax.set_xlabel("x ekseni")
    ax.set_ylabel("y ekseni")
    ax.set_title("fonksiyon grafiği")
    ax.plot(x,f(x),"red")
    plt.show()
    
    c = np.random.rand(1)
    c = c[0].astype(float)
    if f(c*x1+(1-c)*x2)<=c*f(x1)+(1-c)*f(x2):   
        return "Bu Bir İçbükey (Konveks) Fonksiyondur."
    return "Bu Bir Dışbükey (Konkav) Fonksiyondur."