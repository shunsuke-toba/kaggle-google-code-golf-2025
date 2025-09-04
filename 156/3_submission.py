def p(g):
 T=[[],[]];i=d=0
 for r in g:
  if s:=sum(r)//4:T[i]+=[(r,s-2)];d+=s-s*2*i
  elif d:i=1
 i=d>0
 for t in T:
  for r,w in t[1:-1]:x=r.index(4)+1;r[x:x+w]=[i+1]*w
  i^=1
 return g