def p(j):
 A=min(len(j),len(j[0]));p,c=[r[:A]for r in j[:A]],[r[-A:]for r in j[-A:]]
 if 8 in sum(p,[]):p,c=c,p
 return[[c[y%A][x%A]and p[y//A][x//A]for x in range(A*A)]for y in range(A*A)]
