def p(g):
 c=len(g);g=[[x or 4for x in r]for r in g];d=1-c,0,-1,0
 for z in range(9**5):r,q=z%97%c,z%89%c;g[r][q]*=g[r+d[z&3]][q+d[~z&3]]*r*q*(r-c+1)+g[r][q]%2!=0
 return g
