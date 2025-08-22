def p(g):
 d={};[d.setdefault(x,set()).add(divmod(i,10))for i,x in enumerate(sum(g,[]))if x]
 (a,A),(b,B)=d.items()
 f=lambda s:{(x-a,y-b)for a,b in[map(min,zip(*s))]for x,y in s}
 A=f(A);B=f(B)
 if f({divmod(i,3)for i in range(9)}-A)^B:a,b,A=b,a,B
 o=[[b]*3,[b]*3,[b]*3]
 for x,y in A:o[x][y]=a
 return o
