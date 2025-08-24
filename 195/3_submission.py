p=lambda g,A=range(9):(w:=len(g[0]),x:=sum(g,[]).index(5)//w,y:=min([*r,5].index(5)for r in g),[[g[x+i-i%3][y+j-j%3]&g[x+i*3%9][y+j*3%9]for j in A]for i in A])[3]
