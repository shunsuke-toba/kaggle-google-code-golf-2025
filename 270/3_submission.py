def p(g):
 s=sum(g,[]);r=[0]*225
 for t in 7,3:
  p=s.index(7//t);r[p]=7//t
  for j in range(225):
   if s[j]==t:r[p+(k:=j-p)//(abs(k)//15 or abs(k))]=t
 return[r[i:i+15]for i in range(0,225,15)]
