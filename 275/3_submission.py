def p(g):
 n=len(g+g[0])//3;a=[r[:n]for r in g[:n]];b=[r[-n:]for r in g[-n:]]
 if'8'in str(a):a,b=b,a
 return[[x*y//8for x in r for y in s]for r in a for s in b]