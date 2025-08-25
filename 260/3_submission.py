def p(g,a=9,b=-9,r=range(10)):
 for i in r:
  for j in r:
   v=g[i][j];e=j-i
   if 0<v!=5:c=v;d=e
   elif v:a=min(a,e);b=max(b,e)
 return[[c*(j-i in([d]+[b+2]*(b>d)+[a-2]*(a<d)))for j in r]for i in r]