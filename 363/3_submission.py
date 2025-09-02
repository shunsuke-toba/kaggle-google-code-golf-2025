def p(g):
 r=range(120);h=sum(([5,*x,5]for x in g),[])+[5]*36;p=[i for i in r if h[i]&2];v=[k for k in r if max(h[i+k-p[0]]for i in p)<1];v=v[v==[16,67]:];v[1:3]*=v>v[5:]
 for k in v:
  for i in p:j=i+k-p[0];g[j//12][j%12-1]=2
 return g