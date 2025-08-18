def p(g):
 n=len(g);T=[0,1,2];t=[]
 for y in range(n-2):
  for x in range(len(g[0])-2):
   if len(s:=set(sum(b:=[r[x:x+3]for r in g[y:y+3]],[])))<3 and 0 not in s and s>{2}:
    t+=b,
    for r in g[y:y+3]:r[x:x+3]=0,0,0
 f=lambda a:(R:=[i for i,r in enumerate(a)if any(r)],C:=[i for i,c in enumerate(zip(*a))if any(c)],[r[C[0]:C[-1]+1]for r in a[R[0]:R[-1]+1]])[-1]
 n=len(g:=f(g));Y=range(n-2);X=range(len(g[0])-2)
 t.sort(key=lambda b:-str(b).count('2'))
 for b in t:
  for _ in[0]*4:
   for y in Y:
    for x in X:
     if all((b[i][j]==2)==(g[y+i][x+j]<1)for i in T for j in T):
      for i in T:g[y+i][x:x+3]=b[i]
      break
    else:continue
    break
   else:b=[*zip(*b[::-1])];continue
   break
 return f(g)
