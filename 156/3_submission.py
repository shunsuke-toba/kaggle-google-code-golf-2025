def p(g):
 t=a=[];b=[]
 for y,r in enumerate(g):
  if s:=sum(r)//4:t+=y,r.index(4),s
  elif t:t=b
 c=(len(a)*a[2]>len(b)*b[2])+1
 for t,c in(a,c),(b,3-c):
  for r in g[-~t[0]:t[-3]]:r[t[1]+1:t[1]+t[2]-1]=[c]*(t[2]-2)
 return g