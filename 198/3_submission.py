def p(g):
 L=len;R=range;z=zip;x=max(map(max,g));Z=[*z(*g)];h=L(g);w=L(Z)
 H=[i for i in R(h)if g[i].count(x)*2>w]
 V=[i for i in R(w)if Z[i].count(x)*2>h]
 o=[*map(list,g)];A=-1,*H,h;B=-1,*V,w
 for i,j in z(A,A[1:]):
  for k,l in z(B,B[1:]):
   t=(i>=0 and 0 in g[i][k+1:l] or j<h and 0 in g[j][k+1:l] or k>=0 and 0 in Z[k][i+1:j] or l<w and 0 in Z[l][i+1:j])+3
   for y in R(i+1,j):
    for x in R(k+1,l):o[y][x]=o[y][x]or t
 for r in H:o[r]=[x or 4 for x in o[r]]
 for r in o:
  for c in V:r[c]=r[c]or 4
 return o
