'''
========================================================================================
Altın Kesit Araştırması
========================================================================================


'''

def f(x):
    return pow(x,2)+2*x

def altın_kesit(a,b,r,s):

    x = b-r*(b-a) #x1
    y = a+r*(b-a) #x2


    for i in range(s):
        if (f(x) < f(y)):
            # tanım aralığı: (x1,b]
            y = x+r*(b-x)
            x = b-r*(b-x)
            l = b-x
            çk = {"üst sınır":b,"alt sınır":x,"aralık":l}
        else:
            #tanım aralığı: [a,x2)
            x = y-r*(y-a)
            y = a+r*(y-a)
            l = (y-a)
            çk = {"üst sınır":y,"alt sınır":a,"aralık":l}
    return çk

k = altın_kesit(-3,5,0.618,10)
print(k)




