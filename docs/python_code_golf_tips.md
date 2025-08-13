## 概要

python のコードゴルフのテクニックをまとめてこれを読ませることで生成 AI がコードを短くするときの

## 基本テクニック

### 変数名を 1 文字にする

変数名を一文字にしましょう。

### 余計な空白を無くす

一般的なコードでは、可読性（コードの読みやすさ）を上げるために、空白や改行を使い見やすくしますが、Code Golf では必要ありません。

### 余計な改行を無くす

if 文や for 文などの、中身が一行の場合は、コロン : の隣に記述できます。

### インデントを 1 にする

実は、インデントは 1 でもプログラムを動かすことが出来ます。

## 変数への代入テクニック

### 同じ値を複数の変数に代入したい場合

基本イミュータブルの型だったら何でも、このテクニックを使えると思います！

```python
x=y=z=0
```

### アンパック代入

リストや文字列などのイテラブルなオブジェクトは、複数の変数へ一気に代入することが出来ます。

```python
# 変更前
# A=list(map(int,input().split()))
# print(A[1:])
_,*A=map(int,input().split())
print(A)
```

### セイウチ演算子

セイウチ演算子とは「変数の代入と使用」を同時に行える演算子です。

```
# 変更前
# A=list(map(int,input().split()))
# l=len(A)
# s=sum(A)
# if(l>=5):print(s/l)
if(l:=len(A:=list(map(int,input().split()))))>=5:print(sum(A)/l)
```

## input 関数のテクニック

### eval 関数を利用する

```python
# 変更前
# A=list(map(int,input().split()))
# B=list(map(int,input().split()))
S="list(map(int,input().split()))"
A=eval(S)
B=eval(S)
```

## スライス と "YNeos" 関係

```python
# print("Yes" if x<3 else "No")
print("YNeos"[x>2::2])
```

## good tips

before

```
for i in range(m):
 for j in range(n):
  do_stuff(i,j)
```

after

```
for k in range(m*n):
 do_stuff(k/n,k%n)
```

```
while n-1:  # bad
while~-n:   # good
```

```
c/(n-1) # bad
c/~-n   # good
```

```
or f(n)+1 # bad
or-~f(n)  # good
```

```
(n-1)/10+(n-1)%10 # bad
~-n/10+~-n%10     # good
```

```
# bad
if i==4 and j==4:
    pass

# good
if i==4and j==4:
    pass
```

```
s=['a','b','c','d','e'] # bad
s=list('abcde')         # bad
*s,='abcde'             # good
```

```
a=list(range(10)) # bad
*a,=range(10)     # good
```

Getting the last element from a list

```
a=L[-1] # bad
*_,a=L  # good
```

In some situations, this can also be used for getting the first element to save on parens:

```
a=(L+[1])[0] # bad
a,*_=L+[1]   # good
```

Assigning an empty list and other variables

```
a=1;b=2;c=[] # bad
a,b,*c=1,2   # good
```

Instead of range(x), you can use the \* operator on a list of anything, if you don't actually need to use the value of i:

```
for i in range(8):pass # bad
for i in[1]*8:pass     # good
```

You can use the good old alien smiley face to reverse sequences:

```
[1, 2, 3, 4][::-1] # => [4, 3, 2, 1] good
```

## 参考文献

- https://qiita.com/Totosuki/items/4f032585e4a51ad7f289
- https://codegolf.stackexchange.com/questions/54/tips-for-golfing-in-python
