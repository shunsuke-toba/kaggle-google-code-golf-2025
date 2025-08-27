def p(g):
 o=[]
 for r in g:
  o+=r,
  for s in o:
   if all((a^b)*a*b<1for a,b in zip(r,s)):
    s[:]=map(max,s,r);o[-1]=s;break
 return o