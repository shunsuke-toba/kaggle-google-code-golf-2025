def p(g,R=range):
 S=len(g);f=sum(g,[]);i=f.index(1);k=f[::-1].index(1);m=[tuple(x&4 for x in r[i%S+1:~k%S])for r in g[i//S+1:S-1-k//S]];r=[*map(list,g)]
 for _ in R(4):
  for q in m,m[::-1]:
   h=len(q);w=len(q[0])
   for y in R(S-h+1):
    for x in R(S-w+1):
     if [tuple(g[x:x+w])for g in g[y:y+h]]==q:
      for V in R(y-1,y+h+1):
       for U in R(x-1,x+w+1):
        if S>V>=0<=U<S and g[V][U]-4:r[V][U]=1
  m=[*zip(*m[::-1])]
 return r