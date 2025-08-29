def p(g):
 o=[]
 for r in g:s=[t for t in o+[r] if all((a^b)*a*b<1for a,b in zip(r,t))][0];o+=s,;s[:]=map(max,s,r)
 return o