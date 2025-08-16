def f(A):
 for r in A:
  for c in set(r)-{0}:
   try:a=r.index(c);b=r.index(c,a+1);r[a:b+1]=[c]*-~(b-a)
   except:0

def p(g,r=range):
 n=len(g);m=len(g[0]);N=-~n//3;M=-~m//3;B=[[g[3*i][3*j]for j in r(M)]for i in r(N)]
 H=[*map(list,B)];f(H);V=[*map(list,zip(*B))];f(V);V=[*map(list,zip(*V))]
 H=[[B[i][j]or H[i][j]or V[i][j]for j in r(M)]for i in r(N)];return[[H[i//3][j//3]if i%3<2>j%3 else g[i][j]for j in r(m)]for i in r(n)]
