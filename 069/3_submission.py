def p(g):
 g=sum(g,[]);p=[];r=range(100)
 for i in r:
  if(v:=g[i])%8:p+=i*10+v,;g[i]=0
 a=p[0]//10
 for i in r:
  if g[i]==8:
   for j in p:g[i+j//10-a]=j%10
 return[g[i:i+10]for i in r[::10]]