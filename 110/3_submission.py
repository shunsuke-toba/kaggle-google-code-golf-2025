def p(g):
 t=[]
 for i,r in enumerate(g):
  for s in t:
   if all(a==b or a*b<1 for a,b in zip(r,s)):break
  else:t+=r,;s=r
  s[:]=[x or y for x,y in zip(s,r)];g[i]=s
 return g
