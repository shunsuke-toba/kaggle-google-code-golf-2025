def p(g):
 a=sum(g,[]);d,b,_=sorted(sorted({*a}),key=a.count)
 exec('for r in g:\n try:p=r.index;r[p(d):p(b)]=[d]*(p(b)-p(d))\n except:0\ng[:]=map(list,zip(*g[::-1]))\n'*4)
 return g