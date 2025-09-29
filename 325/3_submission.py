def p(g,o=[]):
 while g:
  r,*g=g
  while 8in r:
   o=[R+[0]for R in o]+[[0]*len(o)+[8]];x=r.index(8)
   for R in r,*g[:3]:R[x-2*(x>1):x+4]=[0]*6
 return o