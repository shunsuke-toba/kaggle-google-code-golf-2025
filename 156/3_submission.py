def p(g):
 t=a=[0];b=[0];y=0
 for r in g:
  if s:=sum(r)//4:t+=y,r.index(4),s;t[0]+=s
  elif t[0]:t=b
  y+=1
 for t in a,b:
  for r in g[-~t[1]:t[-3]]:r[t[2]+1:t[2]+t[3]-1]=[1+((a[0]>b[0])^(t==b))]*(t[3]-2)
 return g