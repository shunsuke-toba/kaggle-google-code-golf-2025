J=lambda a:(b:=[i for i,r in enumerate(a)if any(r)])and(b[0],b[-1])
def p(a):
 c,e=J(a);k,w=J(zip(*a))
 for i in 1,-1:a[c+i][k+i],a[e+i][w+i],a[c+i][w-i],a[e+i][k-i]=a[e+i][w+i],a[c+i][k+i],a[e+i][k-i],a[c+i][w-i]
 return a
