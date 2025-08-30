def p(g):
 for k in range(18):a=any(g[8])*2;R=g[k//3+1+a*(k>8)];c=(a,5)[k>8]+k%3;R[c]=R[c]or 7
 return g