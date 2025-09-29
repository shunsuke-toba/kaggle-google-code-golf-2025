def p(g,b=99,h=0):
 v=g[r:=b//10][c:=b%10]
 while~r%11>0<5>g[r][c]:g[r][c]|=v;r+=v%2^h or-1
 if b:p(g,b-1,h|v//3);return g