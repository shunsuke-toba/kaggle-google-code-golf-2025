def p(g):
 r=range(110);h=[i for i in g for i in i+[1]]+[1]*36;p=[i for i in r if h[i]&2];v=[i for i in r if all(h[j+i-p[0]]<1 for j in p)]
 v[1:3]*=v>v[5:];v=v[v==[14,61]:]
 for i in v:
  for j in p:k=j+i-p[0];g[k//11][k%11]=2
 return g