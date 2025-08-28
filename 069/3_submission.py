def p(g):
 g=sum(g,[]);p=[];r=range(100)
 for i in r:
  if(v:=g[i])%8:p+=i*16+v,;g[i]=0
 for i in r:
  for j in p*(g[i]==8):g[i+j//16-p[0]//16]=j&15
 return[g[i:i+10]for i in r[::10]]