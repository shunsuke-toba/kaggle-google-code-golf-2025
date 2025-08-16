def p(g):
 s=[]
 for y,l in enumerate(g):
  for x,c in enumerate(l):
   if c:
    l[x]=0;q=[(y,x)];m=x;n=0
    while q:
     i,j=q.pop();n+=1;m=min(m,j)
     for a,b in(i+1,j),(i-1,j),(i,j+1),(i,j-1):
      if 0<=a<10>b>=0 and g[a][b]==c:g[a][b]=0;q+=[(a,b)]
    s+=[(m,n,c)]
 s.sort();t=max(b for _,b,_ in s);return[[c for a,b,c in s if b==t]]*t
