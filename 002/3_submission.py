def p(j):
 A=range;c=len(j);R=A(c)
 for r in j:r[:]=[x or 4 for x in r]
 d=1,0,-1,0,1
 for z in A(64*c*c):
  r,q,i=z%c,z//c%c,z//c//c%4
  if j[r][q]==4:
   x,y=r+d[i],q+d[i+1]
   if not(0<=x<c and 0<=y<c and j[x][y]!=0):j[r][q]=0
 return j