def p(g):
 a=0
 while g[a]<[1]:a+=1;b=sum(g[a])//2+a
 for y in range(b):g[y][:b-y]=[2+(y<a)-(y>a)]*(b-y)
 return g