t=lambda a:[*map(list,zip(*a))]
def p(a):
 h=len(a);w=len(a[0])
 if w>h:return t(p(t(a)))
 s=a.index;r=s([2]*w);g=[r for r in a if 3 in r]
 return s(g[0])<r and p(a[::-1])[::-1]or a[:r+1]+g+[[8]*w]+[[0]*w]*(h-r-len(g)-2)