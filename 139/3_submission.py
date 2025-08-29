def p(g):
 a=any(g[8])*2
 for k in range(18):R=g[(1,4+a)[k>8]+k%9//3];c=(a,5)[k>8]+k%3;R[c]=R[c]or 7
 return g