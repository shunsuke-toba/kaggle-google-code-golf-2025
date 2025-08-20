def p(a):
 for r,s in zip(a,a[1:]):s[1:]=map(lambda x,y:4*(x==y>0)or y,r,s[1:])
 return a
