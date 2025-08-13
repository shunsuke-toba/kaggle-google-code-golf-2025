def p(g):
 for b in range(18):k,r=b//9,b%9//3;g[b%3][6+k*4-r]=g[r][k*4+b%3]
 return g