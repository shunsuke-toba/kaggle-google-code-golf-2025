p=lambda g,R=lambda z:[*zip(*z[::-1])]:[i+[*j]for i,j in zip(g,R(g))]+[[*i,*j]for i,j in zip(R(R(R(g))),R(R(g)))]
