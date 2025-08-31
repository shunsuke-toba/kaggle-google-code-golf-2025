def p(g):
 R=range(144);h=sum(([1]+r+[1]for r in g),[1]*12)+[1]*48;p=[i for i in R if h[i]&2];v=[k for k in R if max(h[i+k-p[0]]for i in p)<1];v=v[v==[28,79]:];v[1:3]*=v>v[5:]
 for k in v:
  for i in p:h[i+k-p[0]]=2
 return[h[i:i+10]for i in R[13:133:12]]