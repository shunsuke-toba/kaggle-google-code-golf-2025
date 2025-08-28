def p(g):
 exec('a=next(r for r in g if(s:=[*filter(int,r)])[1:]);a[:]=(s*8)[-a.index(s[0])%len(s):];g[:]=map(list,zip(*g));'*2)
 return g