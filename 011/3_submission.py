p=lambda g,R=range(11):next([[5*(x&3>2 or y&3>2)or g[i+x//4][j+y//4]for y in R]for x in R]for i in(0,4,8)for j in(0,4,8)if sum(8in r[j:j+3]for r in g[i:i+3])<1)
