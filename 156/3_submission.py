def p(g):
 t=a=[y:=0];b=[0]
 for r in g:
  if s:=sum(r)>>2:t+=y,r.index(4),s;t[0]+=s
  elif t[0]:t=b
  y+=1
 for t in a,b:
  for r in g[-~t[1]:t[-3]]:r[t[2]+1:t[2]+t[3]-1]=[1+(t>min(a,b))]*(t[3]-2)
 return g