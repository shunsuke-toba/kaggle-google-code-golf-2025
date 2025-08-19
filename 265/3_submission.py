def p(g):
 r=[*map(list,g)]
 for a,b,s,t in zip(g,g[1:],r,r[1:]):
  for j in range(17):
   if(sum(a[j:j+2]+b[j:j+2])<1)*(j%16<1or a[j-1]+b[j-1]|a[j+2]-5|b[j+2]-5):s[j:j+2]=t[j:j+2]=2,2
 return r
