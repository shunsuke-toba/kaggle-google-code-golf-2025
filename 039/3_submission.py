E=enumerate
def p(a):y,x=map(min,zip(*[(i,j)for i,r in E(a)for j,v in E(r)if v]));return[a[y+i][x:x+3]for i in range(3)]
