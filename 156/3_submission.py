def p(g):
 T=[[],[]];i=d=0
 for r in g:
  if s:=sum(r)>>2:T[i]+=(r,s-2),;d+=s-s*2*i
  i+=d>1>s
 for i in 0,1:
  for r,w in T[(d>0)^i][1:-1]:x=r.index(4)+1;r[x:x+w]=w*[i+1]
 return g