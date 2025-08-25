p=lambda g:[b:=[g[i:i+3]if g[3:]else[r[i:i+3]for r in g]for i in range(0,len(g+g[0])-3,3)],m:=[str(x).count('0')for x in b],b[m.index(min(m,key=m.count))]][2]
