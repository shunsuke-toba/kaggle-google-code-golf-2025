def p(g,a=9,b=-9,r=range(10)):
 for i in r:
  for j in r:
   if(v:=g[i][j])%5:c=v;d=j-i
   elif v:a=min(a,j-i);b=max(b,j-i)
 return[[c*(j-i in[d]+[b+2]*(b>d)+[a-2]*(a<d))for j in r]for i in r]