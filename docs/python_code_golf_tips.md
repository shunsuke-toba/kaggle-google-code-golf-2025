# Python Code Golf テクニック集

最終更新: 2025 年 8 月 - submission の実測（diff≦10 中心）から抽出・更新（今回: 024, 039, 047, 060, 061, 082, 106, 114, 128, 136, 143, 175, 189, 211, 221, 223, 229, 231, 288, 297, 301, 307, 311, 316, 324, 328, 339, 345, 357, 359, 360, 367, 370, 371, 373, 380, 383, 396, 399, 400 を反映）

## 目次

1. [究極の短縮パターン](#究極の短縮パターン)
2. [基本テクニック](#基本テクニック)
3. [変数とデータ型](#変数とデータ型)
4. [制御構造](#制御構造)
5. [グリッド操作](#グリッド操作)
6. [高度なテクニック](#高度なテクニック)
7. [実戦パターン](#実戦パターン)

---

## 究極の短縮パターン

### ウォルラス演算子の高度な活用

```python
# task313.py: 状態管理とループ変数を同時制御
p=lambda g,j=1:[(g[j:=1-j][1:len({*g[0]})]*9)[:len(g)]for _ in g]

# task041.py: 累積演算
p=lambda g,a=0:[[c|(a:=a^c)for c in r]for r in g]

# task071.py: 条件判定と代入の同時実行
if a<1 and (a:=max(r)):s=r.index(a)+len(r)+~r[::-1].index(a)
```

### eval+str 変換による究極短縮

```python
# task309.py: 最短の値置換
p=lambda g:eval(str(g).replace(*'75'))  # replace('7','5')の短縮

# task337.py: 複数文字の同時置換（swap）
p=lambda g:eval(str(g).translate({53:56,56:53}))  # '5'↔'8' を一度に

# task030.py: divmodとsum()を使った座標検出（diff +0）
r,c=divmod(sum(g,[]).index(8),10)  # 2D座標を1行で取得
```

### 複素数による 2D 座標管理

```python
# task370.py
z=k//w+1j*(k%w)  # 座標を複素数で表現
P-max(Z,key=lambda z:(abs((z:=P-z).real),abs(z.imag)))  # 距離計算

# 比較連鎖での境界チェック（短い）
len(g)>z.real>-1<z.imag<w  # task370.py
```

---

## 基本テクニック

### 空白と改行の削減

```python
# Bad (12 bytes)
number = 3

# Good (3 bytes)
n=3
```

### 変数名の短縮

- 常に 1 文字の変数名を使用
- 大文字も活用（小文字が既に使用済みの場合）
- 関数名も 1 文字に固定（例: `p=lambda g:...` が最短の定型）

### インデントを 1 にする

```python
# Bad (インデント4)
for i in r:
    print(i)

# Good (インデント1)
for i in r:
 print(i)
```

---

## 変数とデータ型

### セイウチ演算子（:=）

```python
# 代入と使用を同時に
if(n:=len(s))>5:print(n)

# リスト内包表記内での使用
[x for x in data if(y:=f(x))>0]

# 累積演算での状態保持（task041.py）
p=lambda g,a=0:[[c|(a:=a^c)for c in r]for r in g]

# lambdaの引数で状態管理（task313.py）
p=lambda g,j=1:[(g[j:=1-j][1:len({*g[0]})]*9)[:len(g)]for _ in g]

# セイウチ演算子の多重代入（task328.py）
(s:=sorted(((u:=abs(y-i))+(w:=abs(x-j)),max(u,w)&1,v)...))[0][2]
```

### リスト生成の短縮

```python
# Bad (19 bytes)
s=['a','b','c','d']

# Better (15 bytes)
s=list('abcd')

# Best (11 bytes)
*s,='abcd'

# 10x10グリッドの初期化（task030.py）
[[0]*10for _ in g]  # 既存グリッドgを使って行数を決定
```

### range()の代替

```python
# Bad (20 bytes)
for i in range(8):

# Good（動的回数）
for _ in [0]*n:  # n回反復

# Good（小さな固定回数）
for _ in '1234':  # range(4)と同等（task361.py）

# 単ループで2次元を走査（divmodが最短）
for k in range(n*m):
 i,j=divmod(k,m)  # task020.py
```

### デフォルト引数での関数/値エイリアス

```python
# 同一関数を複数回使うとき短縮（task039.py）
p=lambda g,f=filter:[*zip(*[*f(any,zip(*f(any,g)))][:3])][:3]

# 反復回数もエイリアス化（task061.py, task033.py）
p=lambda g,r=range(18):[[i*j%max(max(g))+1for j in r]for i in r]
p=lambda g,R=range(17):[[g[r%6][c%6]for c in R]for r in R]
```

---

## 制御構造

### 三項演算子の短縮

```python
# Standard (21 bytes)
x='Y'if c else'N'

# List indexing (13 bytes)
x=['N','Y'][c]

# Slicing trick (14 bytes)
x='YNeos'[c::2]
```

### 条件付き値の選択パターン

```python
[0,y][b]    → y*b        # bが真ならy、偽なら0
[1,y][b]    → y**b       # bが真ならy、偽なら1
[x,1][b]    → b or x     # bが真なら1、偽ならx

# task003.py: 条件による乗算
j[(j[1]!=j[4])*2:]  # False=0, True=1を利用

# task052.py: 条件による値設定
[5*(r==r[:1]*3)]*3  # 条件が真なら5、偽なら0

# task072.py: 差分検出
[(a!=b)*3for a,b in zip(*r)]  # 異なれば3、同じなら0

# and/or連鎖で二者択一（ifの代替）
cond and X or Y  # condが真ならX、偽ならY（task146.py）

# 走査しながら末尾まで（長さ判定代替）
while a[i:]: ...; i+=1  # a[i:]が空になるまで（task084.py）

# ブールを負にして末尾/先頭を選択
g[-(i>=n/2)][-(j>=n/2)]  # True→-1, False→0 を活用（task183.py）
```

### XOR 条件判定の短縮

```python
# task110.py: 複合条件の短縮
if all((a^b)*a*b<1 for a,b in zip(r,s)):break
# これは a==b or a==0 or b==0 と同等

# task252.py: toggle変数の短縮（diff +6）
(t:=1)and[(x,x and 4)[t:=1-t]for x in r]  # t=1-tでトグル

# ビットでのトグル（より短い）
d^=cond  # condが真のときだけdを反転（task357.py）

# 短絡評価で一度だけ反転（4回目だけflip）
t=[*zip(*t[::-1])];i-3 or t.reverse()  # task076.py

# 連鎖比較で範囲チェック（行・列を同時に）
r<10>c>-1<r  # 0<=r<10 and 0<=c<10 と同等（task136.py）

# 乗算での同時条件（andの短縮）
while x*y: ...  # x and y と同等（task345.py）

# 真偽を差にして符号/方向を出す
dx=(a>b)-(a<b)  # -1,0,1 を1式で（task256.py）
```

---

## グリッド操作

### 基本変換

```python
# 1次元化
sum(g,[])  # 9 bytes

# 転置（最短）
[*map(list,zip(*g))]  # 20 bytes
[*zip(*g)]  # さらに短い

# 90度回転（時計回り）
[*zip(*g[::-1])]  # 16 bytes

# 90度回転（反時計回り）
[*zip(*g)][::-1]  # 転置して逆順（task380.py）

# 循環シフト（task053.py）
g[2:]+g[:2]  # 行を上に2つシフト

# 1次元→2次元の分割（grouper）
[*zip(*[iter(r)]*w)]  # 長さwで分割（task044.py）

# 先頭列/行の即取得
next(zip(*g))  # 先頭列（転置の最初の列）

# 対称要素の同時処理（半分だけ計算）
[*map(max,r,r[:p:-1])]  # 端からpまでを鏡映結合（task360.py）

# 行/列の非ゼロの最初の位置（矩形検出）
[*map(any,g)].index(1), [*map(any,zip(*g))].index(1)  # task020.py

# 1列（回転転置）を各行に連結してから鏡映で拡張
(G:=[i+[*j]for i,j in zip(g,zip(*g[::-1]))])+[r[::-1]for r in G[::-1]]  # task106.py

# 0の高速カウント（数値グリッドに有効）
str(g).count('0')  # ネストを気にせず '0' を数える（task221.py）

# 文字列表現からパターンをカウントして配列生成
(str(g).count('1, 1')*[1]+9*[0])[:9:2]  # カウント×リストで繰返し（task038.py）

# 1セル枠のパディング（境界判定を省略）
[[0]*(len(g[0])+2)] + [[0,*r,0]for r in g] + [[0]*(len(g[0])+2)]  # task114.py
```

### グリッドの統計

```python
# 非ゼロ要素のカウント
sum(map(bool,sum(g,[])))  # 24 bytes

# 要素の種類数
len({*sum(g,[])})  # 17 bytes

# sorted()のkey関数活用（task078.py）
sorted(c,key=0 .__eq__)  # lambda x: x==0 の短縮（スペース必要）

# 最頻値などの頻度順ソート
sorted(set(s:=sum(g,[])),key=s.count)  # 値の頻度で並べ替え（task393.py）

# 最頻値（モード）の取得
max(s:=sum(g,[]),key=s.count)  # 最頻値を1行で（task304.py）

# 2D配列の最大値（短縮）
max(max(g))  # max(map(max,g)) より短い（task061.py）

# ユニークな行列合体の合計
sum({*r,*c})  # set(r)∪set(c) を短く（task047.py）

# ユニーク要素の総和
sum({*sum(g,[])})  # set化してから合計（task290.py）

# 二重インデックスアクセス（task108.py, diff +8）
g[i//2|1][j//2|1]  # ビットORで奇数化して境界処理

# 最後のインデックス（右側）
~r[::-1].index(x)  # 最後のxの位置を -1 変換で短縮（task071.py）

# 最後の0の位置（存在確認と組み合わせ）
0 in r and ~r.index(0)  # 右側からの0位置（task242.py）

# filter(sum,...) は filter(any,...) の短縮代替（数値グリッド）
[*zip(*filter(sum,zip(*filter(sum,g))))]  # 行・列の全0を落とす（task057.py）

# 順序を保った重複削除
[*{}.fromkeys(sum(g,[]))]  # setより短く元順序を保持（task115.py）

# zipタプルのsum平坦化（ゴルフ定番）
sum(zip(r,r),())        # 2重化しつつ平坦化（task307.py）
sum(zip(r,r,r),())      # 3重化の平坦化（task223.py）

# 先頭/末尾のタイル化と切り詰め
(r[:6]*4)[:len(r+r)]  # 乗算+スライスで長さを合わせる（task231.py）

# 先頭のユニーク値を直接アンパック
_,a,b = {}.fromkeys(sum(g,[]))  # 先頭3種類を一発取得（task383.py）
```

### 要素の操作パターン

```python
# 2つの要素の積（task006.py）
2*a*b for a,b in zip(r,r[4:])  # 隣接要素の積

# 集合和の合計（task047.py）
sum({*r,*c})%13  # 行rと列cのユニーク値合計をモジュロ

# ネストループの簡潔化（task001.py）
[[x&y for x in r for y in s]for r in j for s in j]  # 2重ループを1行で

# 非ゼロだけ残す（0を除去）
[*filter(None,r)]  # rから0だけ落とす（task177.py）

# 0を落とす別解（数値のみ）
[*filter(int,r)]  # int(0)==0を利用（task339.py）

# 非ゼロを一定値に置換
[c and r[0]for c in r]  # 0→0, それ以外→r[0]（task312.py）

# 2列/2行の要素ごとの最大
[*map(max,*z)]  # z=(rowA,rowB)に対して要素ごと最大（task372.py）

# indexで位置を取得して並べ替え
[r[g[1].index(c)]for c in g[1]]  # 見本行の順に列を並べ替え（task197.py）

# 行列ブロックをまとめて検査（行+列）
all(map(sum, t+[*zip(*t)]))  # tの行と転置tの行（=列）を一括評価（task079.py）

# 行と列を合体して多数決
max(v:=r+[*c],key=v.count)  # rと列cの合体リストで最頻値（task359.py）

# 列方向の累積和（先頭i行の合計）
[*map(sum,zip(*g[:i]))]  # i∈{1,2,3}などで使う（task322.py）
```

---

## 高度なテクニック

### タプルアンパックと\*演算子

```python
# task032.py: map結果の即座の展開
p=lambda g:(*zip(*map(sorted,zip(*g))),)

# リスト乗算による拡張と切り詰め
[r[:1]*10,r][r[0]!=r[9]]  # 条件によるリスト選択
g[:1]*3  # リストの繰り返し

# task295.py: ウォルラス演算子とタプル展開の組み合わせ（diff +8）
(x:=g[0])and[(x,x:=x[:1]+x[:-1])[0]for _ in x[::2]]
# xを更新しながら前の値を返す高度なテクニック

# 複数代入を and で繋いで本体を返す
(a:=expr1,b:=expr2)and body  # 2つの代入を1式に（task189.py）

# スライス/インデックス内でのセイウチ（task128.py）
c[-(h:=c.count(0)):]+c[:-h]  # hを使って回転量を一発導入

# タプルを返すと[]が不要（JSON化で自動的に配列化）
(*zip(*map(sorted,zip(*g))),)  # 末尾の , でタプル化（task032.py）

# タプルの繰り返しで行を一括生成
(r:=g[0],[*map(max,r[1:]+[0],[0]+r)])*3  # 2行×3セット=6行（task082.py）
```

### スライスの高度な活用

```python
# task376.py: 逆順スライスとの組み合わせ
p=lambda j:(j+j[-2:0:-1])*2+j[:1]

# task067.py: 正方形化
p=lambda g:[r[:len(g)]for r in g]

# 両軸ミラーの一括生成
[r+r[::-1]for r in g+g[::-1]]  # 上下に連結して各行を左右ミラー（task083.py）

# 対称性判定（転置と一致するか）
(b:=g[:3])==[*map(list,zip(*b))]  # 自己転置と比較（task146.py）

# 1行から正方形を作る
[*zip(*[g[0]]*len(g[0]))]  # 行を列に複製して正方形（task297.py）
```

### 負インデックス・ビット反転の活用

```python
# トーラス境界の簡潔表現（負インデックスで巻き戻す）
g[r+d[s+~i]-h][(c+d[s-i])%w]  # 行は-hで負にして末尾へ（task367.py）

# 直交方向の取得（ビット反転）
x,y=d[s]+r,d[~s]+c  # ~s で軸を入れ替え（task367.py）

# 対称位置への同時代入（末尾側は ~i）
r[i]=r[~i]=a  # task288.py

# 走査しながら左右対称位置を更新
for r in g: r[j]=r[~j]=0; j+=1  # ~j で右側の対称位置（task375.py）
```

### eval+str+replace パターン

```python
# 数値の一括置換（最短）
p=lambda g:eval(str(g).replace(*'75'))  # 7→5に置換

# 正規表現で隣接パターンを書換
import re; eval(re.sub('1, 0(?=, 1)','1,2',str(g)))  # '1,0,1'→'1,2,1'（task258.py）
```

### シフト演算の小技

```python
# 2のべきでの割り算・平均
(a+b)>>1  # (a+b)//2 より短い（task371.py）
sum(sum(g,[]))>>3  # 合計を8で割る（task399.py）
sum(sum(g,[]))     # 数値グリッドの総和を最短で

# 半分のインデックス
len(g)>>1  # len(g)//2 より短い（task329.py）
```

### バイト列による走査と最長区間

```python
# 0/1ブール配列→bytesにして区間を抽出（最短）（task396.py）
b=bytes(i==t for r in g for i in r+[0])
e=max(b.split(b'\0'))  # 最長の連続1区間（各行末の[0]で区切る）
t=b.find(e);L=len(e)    # 先頭位置と長さ
```

### 短いトグルと符号操作

```python
# 2要素トグル（~ 演算子）
t=~t  # 0↔-1 を切替（インデックスや真偽に応用: task252.py）

# 真偽を足し引きに利用（方向分岐を1行で）
y-=1-a; x+=a  # a∈{0,1}で上下/左右（task345.py）
```

### 関数エイリアスによる短縮

```python
# task071.py: パラメータでのエイリアス
def p(g,E=enumerate):
    for i,x in E(r):

# task324.py: 変数でのエイリアス
e=enumerate
for i,r in e(g):

# よく使うエイリアス（複数回使うとき）
R=range;E=enumerate;Z=zip;d=divmod  # `range, enumerate, zip, divmod`

# ラムダのデフォルト引数での別名（1回限りでも有効: task039.py）
p=lambda g,f=filter:[*f(any,g)]

# callableの短名化（sorted→S）
S=sorted; S(map(S,g))  # 行をsortしてから全体をsort（task301.py）

# よく使うインデックス列を事前定義
T=0,4,8  # 3ステップの走査インデックス（task149.py）

# リスト自体を反復回数として複製
for r in g*2: ...  # 同じ行集合を2回なめる（task388.py）
```

### モジュロ演算による座標生成

```python
# task367.py: 複数の値を単一ループ変数から生成
for k in range(9**5):
    r,c,s=k%97%h,k%89%w,k%4  # 行、列、状態を生成

# task020.py: divmodを使った定番の単ループ分解
for k in range(25):
 j,i=divmod(k,5)  # i=k%5; j=k//5 より短い
```

### and 連鎖で値を返す

```python
(k:=sum(g,[])) and[k[~k.index(1)-24*i::-1][:5]for i in range(5)]  # task400.py
# 左が真値のときだけ右を返す（if不要）

# 真偽値は整数（0/1）として使えるので配列生成に便利
((1,0,k>1),(0,k>2,0),(k>3,0,k>4))  # task399.py

# タイリング/繰り返し参照に i%h, j%w
g[i%3][j%3]  # 3×3タイルを敷き詰める（task221.py）

# 値×条件 で「条件なら値、偽なら0」に
g[i][j]*(cond)  # ブールを乗算してマスク（task221.py）

# 0/1に対する線形変換で値を作る
A+B*x  # x∈{0,1} を A または A+B に写像（例: 5-4*x: 0→5,1→1: task073.py）

# 三角波で折り返しインデックス
w-abs(i%(w+w)-w)  # 0..w..0.. の往復（task248.py）
```

### 複素数での座標・回転

```python
# 座標表現
z=i+1j*j  # (i,j)

# 回転（点pを中心に90°回転）
s=(s-p)*1j+p  # task361.py, task370.py

# 距離比較のkey内でのセイウチ活用
max(Z,key=lambda z:(abs((z:=P-z).real),abs(z.imag)))
```

### タプル返却の活用（外側[]を節約）

```python
# 行列はタプルでもJSON化で配列になるため短縮可
return((*zip(*g),),)  # または (row1,row2,...) を直接返す（task373.py）
```

### エラー処理の短縮

```python
# task367.py: 例外を無視
try:g[x][y]=value
except:0  # passより短い

# 条件チェックとして除算エラーを利用
0/~(x|y)  # x|y == -1 の時のみ成功
```

### filter+max パターン

```python
# task316.py: 非ゼロ要素の抽出
[*map(max,filter(max,zip(*g)))]  # 0以外の要素だけを取得

# 列/行の全0を落として圧縮
[*zip(*filter(any,zip(*filter(any,g))))]  # task218.py

# 列の最大値を取りつつ0列を除去（数値グリッド）
(*filter(int,map(max,*g)),)  # 結果を即タプルに（task316.py）
```

### ビット演算の活用

```python
# XORでの条件判定
(a^b)*a*b<1  # a==bまたはa,bのどちらかが0

# ~演算子で負のインデックス
g[~i][0]  # ~0 → -1, ~1 → -2 として逆順アクセス
-~n  # n+1の短縮形
~-n  # n-1の短縮形

# ビットORでフラグ設定
g[x][y]|=t&4  # ビットORで値を追加

# task317.py: ビットORと算術演算の組み合わせ（diff +8）
g[-~r-r%3][-~c-c%3]>0  # -~r == r+1の短縮形を活用

# 値比較の短縮
c^5  # c!=5 の短縮（0で等価, 非0で不等: task044.py）

# ビットANDでの偶奇・格子の色判定
max(u,w)&1  # チェビシェフ距離の偶奇（task328.py）

# 偶奇かつ値域の判定（偶数かつ>1 → 2や4）
u&1<1<u  # task076.py

# ビットマスクで値選択
[x,y][m>>i%k&1]  # i番目のビットでx/yを選択（task176.py）

# or連鎖でのフォールバック（最初の真値を取る）
g[i][j]or g[j][i]or g[0][i!=j]  # 0を飛ばして次善策（task175.py）

# バイト列を添字配列として使う（bytesは整数の列）
S=b'\1\1\1\4\4\4\7\7\7'; [[g[r][c]&1 for c in S]for r in S]  # task317.py
```

---

## 実戦パターン

### 超短縮パターン（18-40 バイト）

#### 最短パターン（18-21 バイト）

```python
# 単純反転（task155.py, 18 bytes）
p=lambda j:j[::-1]

# 反転結合（task116.py, 20 bytes）
p=lambda j:j[::-1]+j

# 結合反転（task172.py, task210.py, 20 bytes）
p=lambda j:j+j[::-1]

# 転置（task241.py, 21 bytes）
p=lambda g:[*zip(*g)]
```

#### リスト操作（21-40 バイト）

```python
# 循環シフト（task053.py, 23 bytes）
p=lambda g:g[2:]+g[:2]

# 各要素2倍（task249.py, 26 bytes）
p=lambda j:[E*2for E in j]

# スライス結合（task113.py, 26 bytes）
p=lambda g:g[:5]+g[4::-1]

# 複雑な回転（task376.py, 33 bytes）
p=lambda j:(j+j[-2:0:-1])*2+j[:1]

# 転置してソート（task032.py, 40 bytes）
p=lambda g:(*zip(*map(sorted,zip(*g))),)

# 各行を左右対称に拡張（task311.py, 32 bytes）
p=lambda j:[R+R[::-1]for R in j]
```

### 特殊な短縮イディオム

#### **setitem**による代入（task030.py, diff +0）

```python
# リスト内包表記で副作用を起こす高度なテクニック
[n[i+t[1]-t[v]].__setitem__(j,v)for i,r in e(g)for j,v in e(r)if v]
# 通常の代入文の代わりにメソッドを使用
```

#### `+=,` での append 短縮（tuple で 1 要素に）

```python
q+=m,  # q.append(m) より短い（task044.py）
Z+=z,  # 同上
```

#### dict.get + 真偽インデックスで条件選択

```python
(x, m.get(x,x))[cond]  # condが真ならmap値、偽ならx（task324.py）
```

#### セット内包表記による要素数取得

```python
len({*g[0]})  # ユニーク要素数を取得
```

#### リスト結合の短縮

```python
sum(g,[])  # 2Dリストのフラット化

# bytes化で index/rfind を短縮
b=bytes(sum(g,[])); b.rfind(1)  # 末尾から検索（task030.py）

# 2箇所へ同時代入（クロス形など）
g[y+k][x]=g[y][x+k]=3  # 代入を連鎖（task371.py）

# 走査しながらリストを拡張してBFS風に広げる
for y,x in s:s+=[(Y,X)for Y in R(y-1,y+2)for X in R(x-1,x+2)if H>Y>-1<X<W and g[Y][X]and(Y,X)not in s]  # task076.py
```

#### インデックス計算の工夫

```python
# task059.py: 2D座標を1Dインデックスから計算
i//44*3+i%11//4  # 複雑な座標変換を1行で
```

#### ~演算子による-1 変換

```python
~n  # -n-1 と同等（1バイト短い）
r[::-1].index(a)  # 逆順からのインデックス

# task219.py: any()を条件として使う新パターン
while~-any(g[i]):i+=1  # ~-any(g[i]) == not any(g[i])

# 境界のクランプを条件式で短縮
i-(i>0)  # max(i-1,0) 相当（スライス境界に有効: task379.py）
```

---

## チェックリスト

最短コードを書くための確認事項：

- [ ] **変数名は 1 文字か？**
- [ ] **空白・改行は最小限か？**
- [ ] **[*zip(*g)]で転置できないか？**
- [ ] **eval+str+replace が使えないか？**
- [ ] **セイウチ演算子で状態管理できないか？**
- [ ] **スライス[::-1]で反転できないか？**
- [ ] **複素数で 2D 座標を管理できないか？**
- [ ] **XOR 条件判定で短縮できないか？**
- [ ] **関数エイリアスを使えないか？**
- [ ] **ビット演算(&,|,^)で条件を短縮できないか？**

### 真偽値を指数・乗算に使う

```python
# a**b は b∈{0,1} で 1 または a（task103.py）
7**(g[0]!=g[2])  # 等しい→1, 異なる→7

# 値×条件 で条件成立時のみ値（既出応用: task161.py）
c*(cond)  # condが真ならc、偽なら0
```

- [ ] **filter(max,...)で非ゼロ要素を抽出できないか？**
- [ ] **try-except:0 でエラー処理を短縮できないか？**
- [ ] **タプルアンパック(\*)で即座展開できないか？**

---

## まとめ

コードゴルフでは、可読性やパフォーマンスを犠牲にしてでもバイト数を削減することが重要です。これらのテクニックを組み合わせることで、大幅な短縮が可能になります。

**最重要テクニック（実測で効果的）:**

1. **`[*zip(*g)]`** - 転置の最短パターン（21 バイト）
2. **スライス `[::-1]`** - 反転の基本（最小 5 バイト追加）
3. **ウォルラス演算子 `:=`** - 代入と使用を同時実行
4. **ビット演算(&,|,^)** - 条件判定の短縮
5. **eval+str+replace** - データ変換の究極短縮
6. **`__setitem__`** - リスト内包表記内での代入
7. **`divmod()`** - 2D 座標の計算
8. **`-~n`/`~-n`** - ±1 の最短形

実際の diff≤10 のソリューションでは、これらのテクニックが巧妙に組み合わされ、驚異的な短縮を実現しています。
