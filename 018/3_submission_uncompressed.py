def p(g):
 R=range;L=len;h,w=L(g),L(g[0]);S=[]
 for y in R(h):
  for x in R(w):
   a=0
   for i in R(y+1,h+1):
    for j in R(x+1,w+1):
     if L({*sum(m:=[r[x:j]for r in g[y:i]],[0])})*all(map(sum,m+[*zip(*m)]))>4:a,b,s=i,j,m
   if a:S+=s,
   for r in g[y:a]:r[x:b]=[0]*(b-x)
 for s in S:
  for z in R(8):
   k=str(s);a=L(s);b=L(s[0])
   for y in R(h-a+1):
    for x in R(w-b+1):
     if all((k.count(str(c:=s[i//b][i%b]))<2)*c==g[y+i//b][x+i%b]for i in R(a*b)):
      for r in R(a):g[y+r][x:x+b]=s[r]
   s=[*zip(*s[::-1])];z^3or s.reverse()
 return g
