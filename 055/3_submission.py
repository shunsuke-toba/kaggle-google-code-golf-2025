def p(g):
 i=g[0].index;c=i(8);d=i(8,c+1);k=0
 return[(r[0]and(k:=k+1)and r)or[k%2*4]*c+[8]+[(4*k+2)%9]*(d+~c)+[8]+[k%2*3]*(len(r)+~d)for r in g]