p=lambda g:(a:=[*zip(*filter(sum,zip(*filter(sum,g))))],r:=range(9),[[a[i//3][j//3]and a[i%3][j%3]for j in r]for i in r])[2]
