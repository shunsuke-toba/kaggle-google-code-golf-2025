def p(o,e=enumerate):
 (i,a),(f,z)=[(i,a)for i,r in e(o)for a,n in e(r)if n];h=z-a>>1
 if i-f:return[*map(list,zip(*p(list(map(list,zip(*o))))))]
 n,e=a,1
 for r in o[i-2:i+3]:o[i-2][f:=n+e*h]=o[i+2][f]=r[f-e]=o[i][n];o[i][n:f:e]=[o[i][n]]*h
 n,e=z,-1
 for r in o[i-2:i+3]:o[i-2][f:=n+e*h]=o[i+2][f]=r[f-e]=o[i][n];o[i][n:f:e]=[o[i][n]]*h
 return o