def p(o):
 f=[]
 for t in range(len(o)):
  for n in range(len(o[0])):
   p=0
   for l in range(t+1,len(o)+1):
    for s in range(n+1,len(o[0])+1):
     if len({*sum(w:=[l[n:s]for l in o[t:l]],[0])})*all(map(sum,w+[*zip(*w)]))>4:q=w;p=len(q);e=len(q[0])
   if p:f+=q,
   for l in range(p):o[t+l][n:n+e]=[0]*e
 for q in f:
  for l in range(8):
   p=len(q);e=len(q[0])
   for t in range(len(o)+1-p):
    for n in range(len(o[0])+1-e):
     if all((str(q).count(str(f:=q[l//e][l%e]))<2)*f==o[t+l//e][n+l%e]for l in range(p*e)):
      for l in range(p):o[t+l][n:n+e]=q[l]
   q=[*zip(*q[::-1])];l^3or q.reverse()
 return o
