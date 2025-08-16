def p(j):
 c=len(j);j=[[x or 4 for x in r]for r in j]
 d=1,0,-1,0,1
 for z in range(c**4):
  r,q,i=z%c,z//c%c,z//c//c%4
  if j[r][q]>3:x,y=r+d[i],q+d[i+1];j[r][q]*=0<=x<c>y>=0<j[x][y]
 return j
