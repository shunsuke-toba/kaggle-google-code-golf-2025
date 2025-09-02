def p(g):
 T=[[],[]];i=d=0
 for r in g:
  if s:=sum(r)>>2:T[i]+=r,;d+=s-s*2*i
  elif T[i]:i=1
 for i in 0,1:
  for r in T[i][1:-1]:x=r.index(4);w=sum(r)>>2;r[x+1:x+w-1]=[-~((d>0)^i)]*(w-2)
 return g