def p(g):
 t=a=[];b=[];y=0
 for r in g:
  if s:=sum(r)//4:t+=y,r.index(4),s
  elif t:t=b
  y+=1
 for t in a,b:
  for r in g[-~t[0]:t[-3]]:r[t[1]+1:t[1]+t[2]-1]=[1+((len(a)*a[2]>len(b)*b[2])^(t==b))]*(t[2]-2)
 return g