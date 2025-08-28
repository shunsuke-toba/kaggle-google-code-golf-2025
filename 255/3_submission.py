def p(g,n=30,T=lambda x:[*map(list,zip(*x[::-1]))]):
 R=range(n);k=max(sum(g,[]))
 for _ in[0]*4:
  a=[i for i in R if k in g[i][5:]]
  for i in R:
   d=next((t for t in a if t>i),0);u=next((t for t in a[::-1]if t<i),n)
   if(d-i>1<i-u)*d-u>6:g[i][5:]=[n]*25
  g=T(g)
 for _ in[0]*4:
  for i in R:
   if all(next((v for v in r if(v-3)*v),0)>9for r in(g[i-(i>0)],g[i],g[i+(i+1<n)])):p=next((j for j,x in enumerate(g[i])if x));g[i][:p]=[3]*p
  g=T(g)
 return[[(x,3)[x>9]for x in r]for r in g]