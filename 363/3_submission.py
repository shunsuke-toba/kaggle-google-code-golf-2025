def p(g):
 r=range(110);h=sum((x+[1]for x in g),[])+[1]*36;p=[i for i in r if h[i]&2];v=[k for k in r if max(h[i+k-p[0]]for i in p)<1];v=v[v==[14,61]:];v[1:3]*=v>v[5:]
 for k in v:
  for i in p:j=i+k-p[0];g[j//11][j%11]=2
 return g