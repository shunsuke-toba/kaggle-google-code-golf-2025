def p(g):
 r=range;S=r(6,11);l=len;_,a,b,c,d=max((i*j,y,y+i,x,x+j)for i in S for j in S for y in r(l(g)-i+1)for x in r(l(g[0])-j+1)if l({y for R in g[y:y+i] for y in R[x:x+j]})<3);g=[R[c:d]for R in g[a:b]]
 for R,x,v in[(R,x,R[x])for R in g for x in r(l(R))if R[x]-g[0][0]]:
  for L in g:L[x]=v;R[:]=[v]*l(R)
 return g
