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

* dpテーブルを位置のインデクスで定義する
* dp=0であれば`dp[i] = dp[i-k] + cost`
* dp != 0であれば、`dp[i] = min(dp[i], dp[i-k] + cost)`


#### 実装

* 位置iでコスト計算を`cost = abs(h[i] - h[i-k])`と書きたかったので、hのindex0にダミーの[0]を加えた。
* pythonだとTLEした。
* pypy3だと1テストケース通らなかった。


### [C - Vacation](https://atcoder.jp/contests/dp/tasks/dp_c)

#### 方針

* dpテーブルを日付と選ぶ活動で定義する
* 今日の活動を決めて、昨日の活動候補を列挙する
* 併せて最大となる値を選ぶ漸化式を作成する


#### 実装

* 日にちの加算値を`act[i][j]`と書きたかったので、hのindexの頭に[0]を加える
* 日にちのfor loopは`for i in range(1, N+1)`としiは日にちとする
