def p(g,r=range(10)):
 a=[]
 for i in r:
  for j in r:
   if(v:=g[i][j])%5:c=v;d=j-i
   elif v:a+=j-i,
 m=min(a);M=max(a);return[[c*(j-i in[d]+[M+2]*(M>d)+[m-2]*(m<d))for j in r]for i in r]