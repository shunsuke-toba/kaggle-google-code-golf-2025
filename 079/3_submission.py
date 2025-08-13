def p(g):
 h,w=len(g),len(g[0]);P={}
 for k in range((h-2)*(w-2)):
  i,j=k//(w-2),k%(w-2);b=[[g[i+x][j+y]for y in range(3)]for x in range(3)]
  if sum(b[x][y]>0 for x in range(3)for y in range(3))>=4:
   k=tuple(tuple(r)for r in b)
   if k not in P:
    c={};z=9
    for m in range(9):
     v=b[m//3][m%3]
     if v:c[v]=c.get(v,0)+1;z-=1
    d=max(c.items(),key=lambda x:x[1])[0]if c else 0
    P[k]=[0,z,b,d,c.get(d,0)]
   P[k][0]+=1
 C={}
 for k,v in P.items():
  c=v[3]
  if c not in C:C[c]=[]
  C[c]+=[(k,v)]
 F={}
 for c,g in C.items():
  m=max(v[4]for k,v in g)
  for k,v in g:
   if v[4]==m:F[k]=v
 return max(F.items(),key=lambda x:(x[1][0],-x[1][1]))[1][2]
