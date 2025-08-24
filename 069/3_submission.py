def p(g):
 g=sum(g,[]);r=range(100);p=[]
 for i in r:
  if(v:=g[i])%8:p+=[(i,v)];g[i]=0
 a=p[0][0]
 for i in r:
  try:
   if{g[i+d-a]for d,_ in p}=={8}:
    for d,v in p:g[i+d-a]=v
  except:0
 return[g[i:i+10]for i in r[::10]]
