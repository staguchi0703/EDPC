# at_coder_template

## はじめに

* atcoderで[DPが学べるコンテスト](https://atcoder.jp/contests/dp)がある。
* C++での解答や解説は多いが、初心者（筆者）向けのpyhton記事が見つからなかった。


## 目的

* DPを勉強がてら解説しながら実装する
* 初心者が躓くであろうポイントを備忘録的にまとめる。


##　解答

### [A - Frog 1](https://atcoder.jp/contests/dp/tasks/dp_a)



### [B - Frog 2](https://atcoder.jp/contests/dp/tasks/dp_b)

#### 方針

* Kのループが必要になるが、numpyの配列計算を使えばKのループ分を高速化できる


#### 実装

* 配列の最大値を`max1 = min(N, i+K)`とすればif分で値の場合分けがいらない
* 処理系をmain()関数としておくと、ちょっと早くなる
* importは上記main()の外にだす
* 答えの出力もmain()の中に入れておくと早い



### [C - Vacation](https://atcoder.jp/contests/dp/tasks/dp_c)

#### 方針

* dpテーブルを日付と選ぶ活動で定義する
* 今日の活動を決めて、昨日の活動候補を列挙する
* 併せて最大となる値を選ぶ漸化式を作成する


#### 実装

* 日にちの加算値を`act[i][j]`と書きたかったので、hのindexの頭に[0]を加える
* 日にちのfor loopは`for i in range(1, N+1)`としiは日にちとする



### [F - LCS](https://atcoder.jp/contests/dp/tasks/dp_f)

#### 方針

* 二重ループだと間に合わないのでnumpyを活用する
* dpテーブルを求めてからさかのぼるって解のうち一つを見つける


#### 実装
* 加算可能な組み合わせ行列をあらかじめ作る
  * `eq = s[:,None] == t[None, :]`
* numpyの技
  * `i,j+1`と`i,j`に+1したもののうち大きいほうを選ぶ
    * `np.maximum(dp[i,j+1], dp[i,j] + 加算可能な場合1)`
  * `i+1, j`と`i+1, j+1`の大きいほうを採用する
    * `np.maximum.accumulate(dp[i+1])`

#### 補足
* 二重ループでの漸化式は以下

``` python
for i in range(num_s):
    for j in range(num_t):
        if s[i] == t[j]:
            dp[i+1, j+1] = max([dp[i, j] + 1, dp[i+1, j], dp[i, j+1]])
        else:
            dp[i+1, j+1] = max([dp[i+1, j], dp[i, j+1]])
```

* これをnumpyの行列処理にすると・・・

```python

for i in range(num_s):
    np.maximum(dp[i, 1:], dp[i, :-1] + eq[i], out=dp[i+1, 1:])
    # eq[i] = 加算可能な組み合わせを行列であらわしたもの
    np.maximum.accumulate(dp[i+1], out=dp[i+1])
```



### [I - COIN](https://atcoder.jp/contests/dp/tasks/dp_i)

#### 方針

* 何個目のコインと表の数をIndexにとってDP

#### 実装
* N=2999 なので2重ループが間に合わない
* numpyの行列計算を使って、ループを減らす