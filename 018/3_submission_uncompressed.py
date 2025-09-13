def p(g):
 S=[]
 for y in range(len(g)):
  for x in range(len(g[0])):
   a=0
   for i in range(y+1,len(g)+1):
    for j in range(x+1,len(g[0])+1):
     if len({*sum(m:=[r[x:j]for r in g[y:i]],[0])})*all(map(sum,m+[*zip(*m)]))>4:a,b,s=i,j,m
   if a:S+=s,
   for r in g[y:a]:r[x:b]=[0]*(b-x)
 for s in S:
  for z in range(8):
   a=len(s);b=len(s[0])
   for y in range(len(g)+1-a):
    for x in range(len(g[0])+1-b):
     if all((str(s).count(str(c:=s[i//b][i%b]))<2)*c==g[y+i//b][x+i%b]for i in range(a*b)):
      for r in range(a):g[y+r][x:b+x]=s[r]
   s=[*zip(*s[::-1])];z^3or s.reverse()
 return g
