def p(g):
 r=[[],[],[]];o=e=3;s=[]
 for t in (*zip(*g),(0,0,0)):
  if any(t):s+=t,
  elif s:
   d=sum({*sum(s,())})-5
   o+=(*s[0],5).index(5)-e;e=(*s[-1],5).index(5)
   for y in 0,1,2:r[y-o%3]+=[c[y]and d for c in s]
   s=[]
 return r