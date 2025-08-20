def p(g):
 d={};[x and d.setdefault(x,set()).add(divmod(i,10))for i,x in enumerate(sum(g,[]))];f=lambda s:{(x-a,y-b)for a,b in[map(min,zip(*s))]for x,y in s};(a,A),(b,B)=d.items();A=f(A);B=f(B)
 while 1:
  if f({(i//3,i%3)for i in range(9)}-A)==B:
   o=[[b]*3,[b]*3,[b]*3]
   for x,y in A:o[x][y]=a
   return o
  a,b,A,B=b,a,B,A
