def p(p):
 q=eval(str(p));n=2;a=range
 while 1:
  b,f,h,n=max((sum((-6,0,3,0,0,0)[q[f+n][h]]+(n and 0<=h+n<len(q[0]) and(-6,0,3,0,0,0)[q[f][h+n]])for n in a(-n,n+1))-n,f,h,n)for n in a(n,4)for f in a(n,len(q)-n)for h in a(len(q[0])))
  if b<3:return p
  for n in a(-n,n+1):
   q[f+n][h]//=5;p[f+n][h]+=q[f+n][h]*3;q[f][h+n]//=5;p[f][h+n]+=q[f][h+n]*3