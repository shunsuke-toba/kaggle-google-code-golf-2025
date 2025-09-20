def p(g):
 n=len(g);(a,c),*_,(b,d)=[(i,j)for i in range(n)for j in range(n)if g[i][j]]
 if g[a][c+2]:return[*zip(*p([*zip(*g)][::-1])[::-1])]
 return[[4*(i<b and (c+(i<=a)<j<d-(i<=a) or (i<=a)*(j-i==c+2-a or j+i==d+a-2))) or g[i][j]for j in range(n)]for i in range(n)]