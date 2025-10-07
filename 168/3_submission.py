def p(g):
 for r in range(81):
  c=r%9;r//=9;v=g[r][c:c+2]+g[r+1][c:c+2];p=v.index(0);q=p%2
  while-1<(r:=r+p+~q)<9>(c:=c-1+q*2)>-1<v.count(0)<2:g[r+p//2][c+q]=v[~p]
 return g