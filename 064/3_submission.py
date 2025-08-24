def p(g):
 a=sum(g,[]);d,b=sorted(sorted({*a}),key=a.count)[:2]
 for _ in[0]*4:
  for r in g:
   try:p=r.index;i=p(d);r[i:p(b)]=[d]*(p(b)-i)
   except:0
  g=[*map(list,zip(*g[::-1]))]
 return g
