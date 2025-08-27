def p(g):
 a=sum(g,[]);d,b,_=sorted(sorted({*a}),key=a.count)
 for _ in[0]*4:
  for r in g:
   try:p=r.index;r[p(d):p(b)]=[d]*(p(b)-p(d))
   except:0
  g=[*map(list,zip(*g[::-1]))]
 return g