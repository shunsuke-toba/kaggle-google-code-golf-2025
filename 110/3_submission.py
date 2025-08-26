def p(g):
 t=[];o=[]
 for r in g:
  for s in t:
   if all((a^b)*a*b<1for a,b in zip(r,s)):break
  else:t+=[s:=r]
  o+=s,;s[:]=map(max,s,r)
 return o
