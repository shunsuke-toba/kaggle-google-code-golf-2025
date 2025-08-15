def p(g):
 r=[*map(list,g)];h=len(g)-1;w=len(g[0])-1
 for i in range(h):
  a=g[i];b=g[i+1];s=r[i];t=r[i+1]
  for j in range(w):
   if a[j]==a[j+1]==b[j]==b[j+1]==0 and(j<1 or j+2>w or a[j-1]+b[j-1] or a[j+2]-5 or b[j+2]-5):
    s[j]=s[j+1]=t[j]=t[j+1]=2
 return r
