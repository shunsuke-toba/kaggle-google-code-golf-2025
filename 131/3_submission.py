t=lambda a:[*map(list,zip(*a))]
def p(a):
 w=len(a[0]);h=len(a)
 if w>h:return t(p(t(a)))
 r=a.index([2]*w);g=[r for r in a if 3 in r]
 return g[0]in a[:r] and p(a[::-1])[::-1]or a[:r+1]+g+[[8]*w]+[[0]*w]*(h-r-len(g)-2)