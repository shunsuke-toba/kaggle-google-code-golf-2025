p=lambda g:[g[(x:=sum(g,[]).index(5))//10+i][x%10-1:x%10+2]for i in(1,2,3)]
