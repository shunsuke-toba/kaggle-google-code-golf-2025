p=lambda g:[exec('r[i]=4')for r,m in zip(g,(224,65,2051))for i in range(len(r))if m>>i%12&1]and g
