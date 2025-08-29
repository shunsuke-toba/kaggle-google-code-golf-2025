def p(g):
 b=bytes(sum(g,[]));r=c=()
 for k in{*b}-{0}:i,j=b.find(k),b.rfind(k);r+=i//10,j//10;c+=i%10,j%10
 s=sorted;x,y=s(r)[1:3];c,d=s(c)[1:3]
 for r in g[x+1:y]:r[c+1:d]=[8]*(d+~c)
 return g