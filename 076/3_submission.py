def p(g):
 L=len;R=range;e=enumerate;s=[divmod(sum(g,[]).index(3),w:=L(g[0]))]
 for y,x in s:s+=[(Y,X)for Y in R(y-1,y+2)for X in R(x-1,x+2)if L(g)>Y>-1<X<w and g[Y][X]and(Y,X)not in s]
 r,c=zip(*s);t=[g[i][min(c):max(c)+1]for i in R(min(r),max(r)+1)]
 for i in R(8):
  for y in R(L(g)-L(t)+1):
   for x in R(w-L(t[0])+1):
    if all(g[y+a][x+b]==u for a,r in e(t)for b,u in e(r)if u&1<1<u):
     for a,r in e(t):
      for b,u in e(r):g[y+a][x+b]=u
  t=[*zip(*t[::-1])];i-3 or t.reverse()
 return g
