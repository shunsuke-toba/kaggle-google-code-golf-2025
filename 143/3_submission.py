def p(g):
 P={(i,j)for i in range(4)for j in range(4)if g[i][j]not in(0,5)}
 def C(S):
  S=set(S);R=[]
  while S:
   t=[S.pop()];c=[]
   while t:
    y,x=t.pop();c+=[(y,x)]
    for a,b in(1,0),(-1,0),(0,1),(0,-1):
     u=(y+a,x+b)
     if u in S:S.remove(u);t+=[u]
   R+=[c]
  return R
 def N(c):
  a=min(y for y,x in c);b=min(x for y,x in c)
  return frozenset((y-a,x-b)for y,x in c)
 T={N(c)for c in C(P)}
 for v in range(10):
  if v*(v-5):
   S={(i,j)for i,r in enumerate(g)for j,x in enumerate(r)if x==v and max(i,j)>3}
   for c in C(S):
    if N(c)in T:
     for y,x in c:g[y][x]=5
 return g
