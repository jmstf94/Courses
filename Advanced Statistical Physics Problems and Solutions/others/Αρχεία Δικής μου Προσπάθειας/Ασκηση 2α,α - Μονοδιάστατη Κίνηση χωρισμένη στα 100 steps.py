import random
random.seed(14277)
i=0
t=[100,200,300,400,500,600,700,800,900,1000]
RX=[]
h=1
a100=[]
a200=[]
a300=[]
a400=[]
a500=[]
a600=[]
a700=[]
a800=[]
a900=[]
a1000=[]
while i<10000:  
    x=0
    n=1
    while n<=1000:
            prosimo=random.random()
            if prosimo < 0.5:
                x+=1
            else:
                x-=1
            if n%100==0:
                if n==100:
                     a100+=[(x**2)]
                elif n==200:
                    a200+=[(x**2)]
                elif n==300:
                    a300+=[(x**2)]
                elif n==400:
                    a400+=[(x**2)]
                elif n==500:
                    a500+=[(x**2)]
                elif n==600:
                    a600+=[(x**2)]
                elif n==700:
                    a700+=[(x**2)]
                elif n==800:
                    a800+=[(x**2)]
                elif n==900:
                    a900+=[(x**2)]
                elif n==1000:
                    a1000+=[(x**2)]
            n+=1
    RX+=[x**2]
    i+=1
j=0
s100=0
s200=0
s300=0
s400=0
s500=0
s600=0
s700=0
s800=0
s900=0
s1000=0
while j<10000:
    s100+=(a100[j]/10000)
    s200+=(a200[j]/10000)
    s300+=(a300[j]/10000)
    s400+=(a400[j]/10000)
    s500+=(a500[j]/10000)
    s600+=(a600[j]/10000)
    s700+=(a700[j]/10000)
    s800+=(a800[j]/10000)
    s900+=(a900[j]/10000)
    s1000+=(a1000[j]/10000)
    j+=1
s=[s100,s200,s300,s400,s500,s600,s700,s800,s900,s1000]
import numpy as np
xi=np.array([100,200,300,400,500,600,700,800,900,1000])
yi=np.array([s100,s200,s300,s400,s500,s600,s700,s800,s900,s1000])
m, b = np.polyfit(xi,yi,1)
print(s,'\n',a100,'\n',a200,'\n',a300,'\n',a400,'\n',a500,'\n',a600,'\n',a700,'\n',a800,'\n',a900,'\n',a1000,'\n',t,'\n',RX,'\n',m,b)
import matplotlib.pyplot as plt
xticks=np.arange(0,1100,100)
plt.xticks(xticks)
yticks=np.arange(0,1050,100)
plt.yticks(yticks)
plt.plot([t],[s],'bo')
plt.plot(xi,xi*m+b,'r')
plt.xlabel('Time (time steps)')
plt.ylabel('<R²> (steps²)')
plt.title('<R²> vs. Time')
plt.grid(True)
plt.text(200,850,r'<R²> increase rate: m=<dR²/dt>=0.98')
#plt.text(200,750,r'Initial Position: b=R0=5.17')
plt.show()