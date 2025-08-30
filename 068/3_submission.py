def p(g):
 a=sum(g,[]);g=[0]*100;i=a.index(b:=min(a,key=a.count))
 for j in 1,9,10,-~10:g[i+j]=g[i-j]=2
 g[i]=b;return[*zip(*[iter(g)]*10)]