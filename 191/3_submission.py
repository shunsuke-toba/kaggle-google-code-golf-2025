def p(g,R=range):
 n=23;f=sum(g,[]);i=f.index(1);k=~f[::-1].index(1);m=[[x&4 for x in r[i%n+1:k%n]]for r in g[i//n+1:n+k//n]];f=[*map(list,g)]
 for _ in R(4):
  for q in m,m[::-1]:
   h=len(q);w=len(q[0])
   for y in R(n-h+1):
    for x in R(n-w+1):
     if [g[x:x+w]for g in g[y:y+h]]==q:
      for V in R(y-1,y+h+1):
       for U in R(x-1,x+w+1):
        if n>V>=0<=U<n and g[V][U]^4:f[V][U]=1
  m=[*map(list,zip(*m[::-1]))]
 return f