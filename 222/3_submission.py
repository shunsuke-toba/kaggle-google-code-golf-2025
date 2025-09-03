def p(g):
 for _ in g:z=[[0]*16];g=[*map(list,zip(*[[c*((l==c or r==c)*(l+sum(m)>0))for c,l,r,*m in zip(r,[0]+r,r[1:]+[0],a,r[2:]+[0]*2,b)]for r,a,b in zip(g,z+g,g[2:]+z*2)]))]
 return g