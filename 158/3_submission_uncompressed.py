def p(e,t=0):
 while len(set(i:=sum(p:=[r[t//-~len(e[0]):][:3]for r in e[t%-~len(e[0]):][:3]],[])))<4:t+=1
 h=i.count
 for _ in range(4):
  for k in 3,2,1:
   for t in range(-~len(e[0])-3*k):
    for s in range(-~len(e)-3*k):
     if all((e[-1][0],p[b//k][v//k])[h(p[b//k][v//k])<2]==e[s+b][t+v]for v in range(3*k)for b in range(3*k)):
      for b in range(3*k):e[s+b][t:t+3*k]=[p[b//k][v//k]for v in range(3*k)]
  p=[*zip(*p[::-1])]
 return e