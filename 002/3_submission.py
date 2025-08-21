def p(j):
 c=len(j);j=[[x or 4 for x in r]for r in j];d=1-c,0,-1,0
 for z in range(9**5):r,q=z%97%c,z%89%c;j[r][q]*=j[r+d[z%4]][q+d[~z%4]]*r*q*(r-c+1)+(j[r][q]&1)!=0
 return j
