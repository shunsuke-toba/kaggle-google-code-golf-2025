def p(g):
 b=[1]*12;R=range(144);h=sum(([1]+r+[1]for r in g),b)+b*4;p=[i for i in R if h[i]&2];a=p[0];v=[k for k in R if max(h[i+k-a]for i in p)<1];v=v[v==[28,79]:];v[1:3]*=v[5:]<v
 for k in v:
  for i in p:h[i+k-a]=2
 return[h[i:i+10]for i in R[13:133:12]]