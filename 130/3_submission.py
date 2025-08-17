t=0,3,6;p=lambda g:[[max(b:=sum((g[r+i][c:c+3]for i in(0,1,2)),[]),key=b.count)for c in t]for r in t]
