def p(c):
 f=[]
 for t in range(len(c)):
  for n in range(len(c[0])):
   p=0
   for l in range(t+1,len(c)+1):
    for m in range(n+1,len(c[0])+1):
     if len({*sum(x:=[l[n:m]for l in c[t:l]],[0])})*all(map(sum,x+[*zip(*x)]))>4:p,e,u=l,m,x
   if p:f+=u,
   for l in c[t:p]:l[n:e]=[0]*len(u[0])
 for u in f:
  for l in range(8):
   p=len(u);e=len(u[0])
   for t in range(len(c)+1-p):
    for n in range(len(c[0])+1-e):
     if all((str(u).count(str(f:=u[l//e][l%e]))<2)*f==c[t+l//e][n+l%e]for l in range(p*e)):
      for l in range(p):c[t+l][n:e+n]=u[l]
   u=[*zip(*u[::-1])];l^3or u.reverse()
 return c