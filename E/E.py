# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\E\E_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
N, W = [int(item) for item in input().split()]
item = [[int(item) for item in input().split()] for _ in range(N)]

dp = [[0 for _ in range(W+1)] for _ in range(2)]

for i in range(N):
    odd_even = i % 2
    for w in range(W+1):
        dp[odd_even^1][w] = max(dp[odd_even^1][w], dp[odd_even][w])
        if w - item[i][0] <= W:
            dp[odd_even ^ 1][w] = max(dp[odd_even^1][w], dp[odd_even][w - item[i][0]] + item[i][1])
        print(dp)
print(dp[N%2][W])
