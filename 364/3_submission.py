def p(g):
 for _ in g:z=[[0]*30];g=[[c and(a|b|d|e|((v:=a+b+d+e&3)<2)*4|(v>2)*(8*(b+d>0)+16*(a+e>0)))for a,b,c,d,e in zip(s,[0]+t,t,t[1:]+[0],u)]for s,t,u in zip(z+g,g,g[1:]+z)]
 return[[c and[2,6,1,2,6][c%5]for c in r]for r in g]