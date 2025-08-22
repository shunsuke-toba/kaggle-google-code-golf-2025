def p(g):
 f=sum(g,[]);c,h,w=min(f,key=f.count),len(g),len(g[0]);d=-1,0,1,0;r=[0]*h
 for k in range(h*w*9):
  i,j=k//w%h,k%w
  if(n:=[g[i+d[t]][j+d[t-3]]for t in range(4)if h>i+d[t]>-1<j+d[t-3]<w>c==g[i][j]])and n.count(s:=max(n,key=n.count))>1:g[i][j]=s;r[s]+=1
 return[[r.index(max(r))]]
