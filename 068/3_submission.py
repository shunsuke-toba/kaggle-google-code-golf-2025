def p(g):
 b=min(g:=sum(g,[]),key=g.count);a=[0]*100;a[i:=g.index(b)]=b
 for j in 1,9,10,11:a[i+j]=a[i-j]=2
 return*zip(*[iter(a)]*10),