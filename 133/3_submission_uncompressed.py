def p(s):
 i=len(s);w=len(s[0])
 def l(t,x):
  g=[(t,x,s[t][x])];s[t][x]=0
  for t,x in(t+1,x),(t,x+1),(t-1,x),(t,x-1):
   if w>x>-1<t<i>s[t][x]>0:g+=l(t,x)
  return g
 i=[l(t,x)for t in range(i)for x in range(w)if s[t][x]]
 d=min((len(i)<3,len(i),i)for i in i)[2]
 r,c,o=min((sum(v==i[2]for t,x,v in d),i)for i in d)[1]
 for i in i:
  g=[(t,x)for t,x,v in i if v==o];m=int(len(g)**.5);q=min(v for t,x,v in i if v^o)
  for t,x,v in d:
   for i,p in g:s[(t-r)*m+i][(x-c)*m+p]=(q,o)[v==o]
 return s