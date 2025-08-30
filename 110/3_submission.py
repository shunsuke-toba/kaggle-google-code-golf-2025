def p(g):
 o=[]
 for r in g:s=r;[s:=t for t in o if all((a^b)*a*b<1for a,b in zip(r,t))];o+=s,;s[:]=map(max,s,r)
 return o