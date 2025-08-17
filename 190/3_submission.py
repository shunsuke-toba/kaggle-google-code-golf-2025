def p(g):
 n=len(g);s={(i,j)for i in range(n)for j in range(n)if g[i][j]}
 for a,b in s:
  if{(a+1,b),(a,b+1),(a+1,b+1)}<=s:break
 c=g[a][b];A=a+1;B=b+1;s-={(a,b),(A,b),(a,B),(A,B)}
 for i,j in s:
  while n>(i:=i+((i>A)-(i<a)))>=0<= (j:=j+((j>B)-(j<b)))<n:g[i][j]=c
 return g
