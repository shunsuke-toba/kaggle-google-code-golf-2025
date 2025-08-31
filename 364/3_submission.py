def p(g):
 for _ in g:z=[[0]*len(g[0])];g=[[(c>0)*(a|b|d|e|((v:=a+b+d+e&3)<2)*4|(v>2)*(((-a-e)%4)*16+((-b-d)%4)*8))for a,b,c,d,e in zip(s,[0]+t,t,t[1:]+[0],u)]for s,t,u in zip(z+g,g,g[1:]+z)]
 return[[{15:2,23:2,27:1,11:6,19:6}.get(c,c)for c in r]for r in g]