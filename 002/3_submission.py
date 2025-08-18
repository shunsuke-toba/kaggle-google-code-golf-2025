def p(j):
 c=len(j);j=[[x or 4 for x in r]for r in j]
 d=1,0,-1,0
 for z in range(9**5):
  r,q,i=z%97%c,z%89%c,z%4
  if j[r][q]>3:x,y=r+d[i],q+d[i-3];j[r][q]*=0<=x<c>y>=0<j[x][y]
 return j
