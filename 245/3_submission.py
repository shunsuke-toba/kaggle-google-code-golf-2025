def p(g):
 y=[];x=[];s=t=0
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v==2:y+=i,;x+=j,
   if v==3:s+=i;t+=j
 d=s//4-(min(y)+max(y))//2;e=t//4-(min(x)+max(x))//2
 for i,j in zip(y,x):g[i][j]=0
 for i,j in zip(y,x):g[i+d][j+e]=2
 return g
