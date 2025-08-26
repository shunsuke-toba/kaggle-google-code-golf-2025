r=range(9);p=lambda g:(a:=[*filter(sum,zip(*filter(sum,g)))])and[[a[j//3][i//3]&a[j%3][i%3]for j in r]for i in r]
