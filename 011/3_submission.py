p=lambda g:next([[5*(x%4>2 or y%4>2)or g[i+x//4][j+y//4]for y in range(11)]for x in range(11)]for i in(0,4,8)for j in(0,4,8)if all(8>max(q[j:j+3])for q in g[i:i+3]))
