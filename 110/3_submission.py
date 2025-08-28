def p(g):
 o=[]
 for r in g:
  for s in o+[r]:
   if all((a^b)*a*b<1for a,b in zip(r,s)):
    s[:]=map(max,s,r);o+=s,;break
 return o