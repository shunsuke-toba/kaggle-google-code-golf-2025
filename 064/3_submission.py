def p(g):
 s=sum(g,[]);c=sorted({*s},key=s.count,reverse=True);b,d=c[1:3]
 for _ in[0]*4:
  for r in g:
   try:i=r.index(d);j=r.index(b);r[i:j]=[d]*(j-i)
   except:0
  g=[*map(list,zip(*g[::-1]))]
 return g
