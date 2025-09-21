def p(g):
 n=len(g);r=range(n);(a,c),*_,(b,d)=[(i,j)for i in r for j in r if g[i][j]]
 if g[a][c+2]:return[*zip(*p([*zip(*g)][::-1])[::-1])]
 return[[4*(i<b)*(c+(i<=a)<j<d-(i<=a) or (i<=a)*(j in (i+c+2-a,d+a-2-i))) or g[i][j]for j in r]for i in r]