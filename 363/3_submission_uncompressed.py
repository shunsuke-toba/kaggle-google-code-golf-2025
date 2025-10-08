def p(g):
 r=range(110);h=[i for i in g for i in i+[1]]+[1]*36;s=[i for i in r if h[i]&2];p=[i for i in r if all(h[j+i-s[0]]<1 for j in s)]
 p[1:3]*=p>p[5:];p=p[p==[14,61]:]
 for i in p:
  for j in s:k=j+i-s[0];g[k//11][k%11]=2
 return g