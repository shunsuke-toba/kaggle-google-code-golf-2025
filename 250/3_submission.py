def p(j):
 d=-1,0,1;E=enumerate;z=[(i,k)for i,r in E(j)for k,v in E(r)if v>4]
 for i,k in z:
  for a in d:
   for b in d:
    if a|b:
     x=i+a;y=k+b
     while 0<=x<len(j)and 0<=y<len(j[0]):
      if j[x][y]-2:x+=a;y+=b
      else:j[x-a][y-b]=5;break
  j[i][k]=0
 return j
